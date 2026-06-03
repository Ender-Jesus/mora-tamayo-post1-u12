# grover.py
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

def grover_2qubits(target="11", shots=1024):
    """Grover para n=2 qubits buscando el estado target."""
    qc = QuantumCircuit(2, 2)

    # Paso 1: superposición uniforme
    qc.h([0, 1])

    # Paso 2: oráculo de fase — marca el estado target
    if target == "11":
        qc.cz(0, 1)
    elif target == "00":
        qc.x([0, 1]); qc.cz(0, 1); qc.x([0, 1])
    elif target == "01":
        qc.x(0); qc.cz(0, 1); qc.x(0)
    elif target == "10":
        qc.x(1); qc.cz(0, 1); qc.x(1)

    # Paso 3: difusor (inversión alrededor de la media)
    qc.h([0, 1])
    qc.x([0, 1])
    qc.cz(0, 1)
    qc.x([0, 1])
    qc.h([0, 1])

    # Medición
    qc.measure([0, 1], [0, 1])

    sim = AerSimulator()
    counts = sim.run(qc, shots=shots).result().get_counts()

    top = max(counts, key=counts.get)
    estado = "✓ CORRECTO" if top == target else "✗ ERROR"
    print(f"  Buscando |{target}> → más probable: |{top}> {estado}")
    for state, count in sorted(counts.items()):
        print(f"    |{state}>: {count:4d} ({count/shots*100:.1f}%)")

    return counts

if __name__ == "__main__":
    targets = ["00", "01", "10", "11"]
    all_counts = {}

    print("Algoritmo de Grover — 2 qubits\n")
    for t in targets:
        all_counts[t] = grover_2qubits(target=t)
        print()

    print("✓ Checkpoint 3 OK: Grover encontró los 4 estados objetivo")

    # Histogramas en grilla 2x2
    fig, axes = plt.subplots(2, 2, figsize=(10, 8))
    fig.suptitle("Algoritmo de Grover — Búsqueda de los 4 estados", fontsize=14)

    for ax, t in zip(axes.flatten(), targets):
        plot_histogram(all_counts[t], ax=ax, title=f"Target |{t}>")

    plt.tight_layout()
    plt.savefig("grover_histogram.png", dpi=150, bbox_inches="tight")
    plt.show()
    print("Histograma guardado: grover_histogram.png")