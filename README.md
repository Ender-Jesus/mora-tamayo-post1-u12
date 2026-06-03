Checkpoint 1, Estado de Bell

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



Checkpoint 2, Algoritmo de Deutsch-Jozsa



Concepto:

El algoritmo de Deutsch-Jozsa demuestra la primera ventaja cuántica documentada: determinar si una función f: {0,1}^n → {0,1} es constante (mismo valor para todas las entradas) o balanceada (0 para la mitad de entradas, 1 para la otra mitad) con una sola evaluación del oráculo.

Clásicamente, en el peor caso se necesitan 2^(n-1) + 1 evaluaciones. Para n=2 eso equivale a 3 evaluaciones. El algoritmo cuántico lo resuelve con exactamente 1 evaluación del oráculo, sin importar el tamaño de n.

El resultado es determinista: si todos los qubits de entrada miden 0 (estado |00>), la función es constante. Si algún qubit mide 1, la función es balanceada. Esto es posible gracias a la interferencia cuántica, que cancela o refuerza amplitudes según el tipo de función.



Por qué 1 evaluación es suficiente



El circuito pone todos los qubits de entrada en superposición con Hadamard, lo que equivale a evaluar la función para todas las entradas simultáneamente. Después de aplicar el oráculo y una segunda capa de Hadamard, la interferencia destructiva elimina todas las amplitudes excepto la que indica el tipo de función. Por eso una sola pasada por el oráculo basta para obtener la respuesta con certeza absoluta.



Resultado



Oráculo		Estado medido		Interpretación

Constante	00 — 100%		Función constante

Balanceada	11 — 100%		Función balanceada



El oráculo constante retornó únicamente |00> en las 1024 mediciones. El oráculo balanceado nunca retornó |00>, confirmando el funcionamiento correcto del algoritmo.

