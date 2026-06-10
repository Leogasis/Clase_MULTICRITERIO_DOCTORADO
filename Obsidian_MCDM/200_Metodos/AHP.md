---
type: method
tags: [metodo, teoria, mcdm, ponderacion, subjetiva]
method_name: "Analytic Hierarchy Process (AHP)"
creator: "Thomas L. Saaty"
---
# 🔧 Analytic Hierarchy Process (AHP)

**[[Mapa del curso (MOC)|<< Volver al Mapa del Curso]]**

## 📝 Descripción General
El **Proceso de Jerarquía Analítica (AHP)**, desarrollado por Thomas L. Saaty en la década de 1970, es uno de los métodos multicriterio más utilizados a nivel global. Permite estructurar problemas complejos de decisión mediante una jerarquía (Meta $\rightarrow$ Criterios $\rightarrow$ Subcriterios $\rightarrow$ Alternativas) y resolverlos a través de comparaciones pareadas basadas en juicios de expertos.

## 🏛️ Axiomas Fundamentales de Saaty
Para dar validez matemática y lógica al método, Saaty definió 4 axiomas clave:
1.  **Reciprocidad:** Si el criterio $C_i$ es $a$ veces más importante que $C_j$, entonces $C_j$ es $1/a$ veces tan importante como $C_i$ ($a_{ji} = 1/a_{ij}$).
2.  **Homogeneidad:** Los elementos que se comparan deben ser de magnitudes similares. Si un elemento es infinitamente superior a otro, la escala cognitiva se rompe y no pueden compararse en la misma matriz.
3.  **Dependencia:** Las prioridades de los elementos de un nivel de la jerarquía dependen exclusivamente de las prioridades del nivel superior inmediato.
4.  **Expectativas:** Los cambios en la estructura de la jerarquía (añadir o remover criterios/alternativas) requieren una reevaluación de los juicios para alinearlos con las expectativas del tomador de decisiones.

## 🧠 Justificación Cognitiva de la Escala de Saaty (1-9)
Saaty propuso una escala cualitativa-cuantitativa del 1 al 9 (donde 1 representa igual importancia y 9 importancia extrema). Esta escala está fundamentada en la psicología cognitiva, específicamente en la **Ley de Miller ($7 \pm 2$)**, que establece que la mente humana tiene un límite de capacidad para procesar y discriminar simultáneamente entre canales de información (entre 5 y 9 categorías de comparación).

---

## 📐 Estructura Matemática y Algoritmo

Dada una matriz de comparación pareada cuadrada y recíproca $\mathbf{A}_{n \times n}$:

### 1. Elicitación de Pesos
El cálculo exacto de pesos se realiza mediante el método del **Autovector Principal**:
$$\mathbf{A}\mathbf{w} = \lambda_{\max}\mathbf{w}$$
Donde:
*   $\mathbf{A}$ es la matriz de comparaciones pareadas.
*   $\mathbf{w}$ es el vector propio (pesos relativos normalizados).
*   $\lambda_{\max}$ es el valor propio (autovalor) máximo de la matriz $\mathbf{A}$. En una matriz perfectamente consistente, $\lambda_{\max} = n$.

### 2. Verificación de la Consistencia
Dado que el juicio humano puede ser inconsistente (ej. preferir $A > B$, $B > C$, pero luego $C > A$), es necesario medir el desvío de la consistencia lógica:

1.  **Índice de Consistencia ($CI$):**
    $$CI = \frac{\lambda_{\max} - n}{n - 1}$$
2.  **Razón de Consistencia ($CR$):**
    $$CR = \frac{CI}{RI}$$
    Donde $RI$ es el **Índice de Consistencia Aleatorio** obtenido empíricamente por Saaty para matrices de tamaño $n$:

| $n$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **$RI$** | 0.00 | 0.00 | 0.58 | 0.90 | 1.12 | 1.24 | 1.32 | 1.41 | 1.45 | 1.49 |

*   **Regla de decisión:** Si $CR < 0.10$ (10%), los juicios se consideran consistentemente aceptables. Si $CR \ge 0.10$, la matriz presenta inconsistencia lógica y debe ser revisada por los expertos.

---

## ⚠️ Límites y Consideraciones Críticas

### El Debate del Rank Reversal (Dyer vs. Saaty, 1990)
Una de las mayores críticas matemáticas al AHP es el fenómeno de **Rank Reversal (Inversión de Rangos)**: la introducción de una alternativa irrelevante o duplicada en la matriz de decisión puede provocar que el orden jerárquico de las alternativas existentes cambie.
*   **Crítica de Dyer (1990):** Señala que este comportamiento viola el axioma económico de *Independencia de Alternativas Irrelevantes (IIA)*, lo que representa un fallo metodológico en la normalización distributiva de AHP.
*   **Defensa de Saaty (1990):** Argumenta que la prioridad es relativa al grupo de alternativas disponibles y que cambiar la composición del grupo altera legítimamente las expectativas y la ponderación global del decisor (comportamiento natural de la psicología humana).

---

## 💻 Implementación en Python (NumPy)

Cálculo del autovector principal y consistencia sin librerías de caja negra:

```python
import numpy as np

# 1. Definición de la matriz recíproca (ejemplo 3x3)
A = np.array([
    [1.0,  3.0,  5.0],
    [1/3,  1.0,  2.0],
    [1/5,  1/2,  1.0]
])

# 2. Obtención de autovalores y autovectores
eig_vals, eig_vecs = np.linalg.eig(A)

# 3. Filtrar el autovalor máximo (y su autovector real asociado)
max_idx = np.argmax(np.real(eig_vals))
lambda_max = np.real(eig_vals[max_idx])
w = np.real(eig_vecs[:, max_idx])

# 4. Normalizar autovector para obtener los pesos
weights = w / np.sum(w)

# 5. Cálculo de Consistencia
n = A.shape[0]
CI = (lambda_max - n) / (n - 1)
RI_dict = {1: 0.0, 2: 0.0, 3: 0.58, 4: 0.90, 5: 1.12, 6: 1.24, 7: 1.32, 8: 1.41, 9: 1.45, 10: 1.49}
RI = RI_dict.get(n, 1.49)
CR = CI / RI if n > 2 else 0.0

print(f"Pesos calculados: {weights}")
print(f"Lambda Max: {lambda_max:.4f}")
print(f"Razón de Consistencia (CR): {CR:.4f} ({'Consistente' if CR < 0.10 else 'Revisar'})")
```

## 📄 Referencias Obligatorias
*   **Saaty, T. L. (1980).** *The Analytic Hierarchy Process*. McGraw-Hill.
*   **Dyer, J. S. (1990).** Remarks on the analytic hierarchy process. *Management Science*, 36(3), 249-258.
*   **Saaty, T. L. (1990).** An exposition of the AHP in reply to the paper "Remarks on the Analytic Hierarchy Process". *Management Science*, 36(3), 259-268.
