# deutsch_jozsa.py
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

def oracle_constante(n):
    """Oráculo constante f(x)=0: no hace nada."""
    return QuantumCircuit(n + 1)

def oracle_balanceada(n):
    """Oráculo balanceado: aplica CNOT de cada qubit al ancilla."""
    qc = QuantumCircuit(n + 1)
    for i in range(n):
        qc.cx(i, n)
    return qc

def deutsch_jozsa(oracle_qc, n, shots=1024):
    """Ejecuta el algoritmo Deutsch-Jozsa con el oráculo dado."""
    qc = QuantumCircuit(n + 1, n)

    # Inicializar ancilla en |-> = H|1>
    qc.x(n)
    qc.h(range(n + 1))

    # Aplicar oráculo
    qc.compose(oracle_qc, inplace=True)

    # Interferencia: H en qubits de entrada
    qc.h(range(n))

    # Medir solo qubits de entrada
    qc.measure(range(n), range(n))

    sim = AerSimulator()
    counts = sim.run(qc, shots=shots).result().get_counts()
    return counts

if __name__ == "__main__":
    n = 2

    # --- Oráculo CONSTANTE ---
    counts_c = deutsch_jozsa(oracle_constante(n), n)
    print("Oráculo CONSTANTE:")
    for state, count in sorted(counts_c.items()):
        print(f"  |{state}> : {count:4d} ({count/1024*100:.1f}%)")

    # --- Oráculo BALANCEADA ---
    counts_b = deutsch_jozsa(oracle_balanceada(n), n)
    print("\nOráculo BALANCEADA:")
    for state, count in sorted(counts_b.items()):
        print(f"  |{state}> : {count:4d} ({count/1024*100:.1f}%)")

    # Verificaciones
    assert "00" in counts_c, "ERROR: oráculo constante no retornó 00"
    assert "00" not in counts_b, "ERROR: oráculo balanceado retornó 00"
    print("\n✓ Checkpoint 2 OK: Deutsch-Jozsa verifica correctamente")

    # Histogramas
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
    plot_histogram(counts_c, ax=ax1, title="Oráculo Constante")
    plot_histogram(counts_b, ax=ax2, title="Oráculo Balanceada")
    plt.tight_layout()
    plt.savefig("deutsch_jozsa_histogram.png", dpi=150, bbox_inches="tight")
    plt.show()
    print("Histograma guardado: deutsch_jozsa_histogram.png")