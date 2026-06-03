Checkpoint 1 — Estado de Bell

Concepto

El estado de Bell |Φ+> = (|00> + |11>) / √2 es el estado cuántico entrelazado más simple. Se prepara aplicando una puerta Hadamard al qubit 0 para crear superposición, seguida de una puerta CNOT con el qubit 0 como control y el qubit 1 como objetivo. El entrelazamiento cuántico implica que al medir ambos qubits siempre coinciden: si uno es 0 el otro también lo es, y lo mismo para 1. Nunca pueden aparecer los estados |01> ni |10>.

Circuito

q\_0: --H--\*--M--

&#x20;         |

q\_1: -----X--M--



Resultado: Se ejecutaron 1024 mediciones (shots).



Estado		Conteo		Porcentaje

00		531		51.9%

11		493		48.1%



Los estados |01> y |10> no aparecieron en ninguna medición, lo que confirma la correlación perfecta del entrelazamiento cuántico. La distribución \~50/50 entre |00> y |11> es el comportamiento esperado para este estado.

