# bell_state.py
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

def bell_state_experiment(shots=1024):
    """Prepara el estado de Bell |Φ+> y mide."""
    qc = QuantumCircuit(2, 2)

    # Hadamard en qubit 0 → superposición
    qc.h(0)
    # CNOT (control=0, target=1) → entrelazamiento
    qc.cx(0, 1)
    # Medir ambos qubits
    qc.measure([0, 1], [0, 1])

    simulator = AerSimulator()
    job = simulator.run(qc, shots=shots)
    counts = job.result().get_counts()

    print(f"Resultados Bell |Φ+> ({shots} shots):")
    for state, count in sorted(counts.items()):
        pct = count / shots * 100
        print(f"  |{state}> : {count:4d} ({pct:.1f}%)")

    # Verificación de correlación perfecta
    assert "01" not in counts and "10" not in counts, \
        "ERROR: aparecieron estados no entrelazados"
    print("\n✓ Checkpoint 1 OK: correlación perfecta verificada")

    # Diagrama del circuito en consola
    print("\nDiagrama del circuito:")
    print(qc.draw())

    # Histograma
    fig = plot_histogram(counts)
    plt.title("Estado de Bell |Φ+>")
    plt.savefig("bell_histogram.png", dpi=150, bbox_inches="tight")
    plt.show()
    print("Histograma guardado: bell_histogram.png")

    return counts

if __name__ == "__main__":
    bell_state_experiment()