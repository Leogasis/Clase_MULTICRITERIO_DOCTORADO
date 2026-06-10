---
type: method
tags: [metodo, teoria, mcdm, ponderacion, subjetiva]
method_name: "Best-Worst Method (BWM)"
creator: "Jafar Rezaei"
---
# 🔧 Best-Worst Method (BWM)

**[[Mapa del curso (MOC)|<< Volver al Mapa del Curso]]**

## 📝 Descripción General
El **Best-Worst Method (BWM)** es un método de ponderación subjetiva multicriterio desarrollado por Jafar Rezaei en 2015. Fue diseñado como una alternativa matemáticamente más eficiente y cognitivamente menos demandante que el Proceso de Jerarquía Analítica (AHP). 
*   **Ventaja clave:** En lugar de realizar una matriz completa de comparaciones pareadas (que requiere $n(n-1)/2$ comparaciones), BWM solo requiere **$2n - 3$ comparaciones**. Esto se logra comparando únicamente el mejor criterio ($C_B$) y el peor criterio ($C_W$) frente a todos los demás, reduciendo drásticamente la carga cognitiva y mitigando las inconsistencias de juicio.

---

## 🏛️ Algoritmo Paso a Paso
1.  **Identificación de Extremos:** Identificar el mejor criterio ($C_B$) y el peor criterio ($C_W$) del conjunto de criterios del problema.
2.  **Vector Best-to-Others ($A_B$):** Determinar la preferencia del mejor criterio ($C_B$) sobre todos los demás criterios ($C_j$), utilizando la escala del 1 al 9. El vector resultante es:
    $$A_B = (a_{B1}, a_{B2}, \dots, a_{Bn})$$
    *Donde $a_{BB} = 1$.*
3.  **Vector Others-to-Worst ($A_W$):** Determinar la preferencia de todos los criterios ($C_j$) sobre el peor criterio ($C_W$), utilizando la escala del 1 al 9. El vector resultante es:
    $$A_W = (a_{1W}, a_{2W}, \dots, a_{nW})^T$$
    *Donde $a_{WW} = 1$.*
4.  **Cálculo de Pesos:** Resolver un modelo de optimización para encontrar los pesos óptimos $(w_1^*, w_2^*, \dots, w_n^*)$ que minimicen la máxima desviación absoluta entre las relaciones de pesos calculadas y las preferencias declaradas por el decisor.

---

## 📐 Formulaciones Matemáticas

### 1. Modelo No Lineal Minimax (Rezaei, 2015)
El modelo original busca minimizar la desviación absoluta máxima ($\xi$):
$$\begin{aligned}
\min \quad & \xi \\
\text{s.t.} \quad & \left| \frac{w_B}{w_j} - a_{Bj} \right| \le \xi, \quad \forall j \\
& \left| \frac{w_j}{w_W} - a_{jW} \right| \le \xi, \quad \forall j \\
& \sum_{j=1}^n w_j = 1 \\
& w_j \ge 0, \quad \forall j
\end{aligned}$$

### 2. Modelo Linealizado Minimax (Rezaei, 2016)
Para garantizar una solución global única y evitar problemas de convergencia de los solvers no lineales, Rezaei linealizó el modelo de la siguiente manera:
$$\begin{aligned}
\min \quad & \xi^L \\
\text{s.t.} \quad & |w_B - a_{Bj}w_j| \le \xi^L, \quad \forall j \\
& |w_j - a_{jW}w_W| \le \xi^L, \quad \forall j \\
& \sum_{j=1}^n w_j = 1 \\
& w_j \ge 0, \quad \forall j
\end{aligned}$$
*Esta formulación lineal siempre produce una única solución global óptima y se puede resolver fácilmente con programación lineal simple.*

---

## 📊 Consistencia de Juicios en BWM
La Razón de Consistencia ($CR$) se calcula para evaluar la calidad lógica de los juicios provistos por el decisor:
$$CR = \frac{\xi^*}{CI_{bwm}}$$
Donde $\xi^*$ es el valor objetivo óptimo del modelo (desviación obtenida) y $CI_{bwm}$ es el **Índice de Consistencia** máximo teórico correspondiente al valor de preferencia $a_{BW}$ (comparación del mejor con el peor criterio) según la escala del 1 al 9:

| $a_{BW}$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **$CI_{bwm}$** | 0.00 | 0.44 | 1.00 | 1.63 | 2.30 | 3.00 | 3.73 | 4.47 | 5.23 |

*   **Regla de decisión:** Valores de $CR$ cercanos a 0.0 indican alta consistencia; valores superiores a 0.25-0.30 sugieren que se debe revisar la coherencia de las comparaciones Best-to-Others y Others-to-Worst.

---

## 💻 Implementación en Python (`PuLP`)

Resolución del modelo lineal minimax de BWM de forma declarativa utilizando la biblioteca de optimización `PuLP`:

```python
import pulp

# 1. Definir datos de entrada (ejemplo con 4 criterios)
# Supongamos C1 es Best (B) y C4 es Worst (W)
best_idx = 0
worst_idx = 3

a_B = [1.0, 2.0, 4.0, 8.0]  # Preferencias Best-to-Others
a_W = [8.0, 4.0, 2.0, 1.0]  # Preferencias Others-to-Worst

n = len(a_B)

# 2. Crear el problema de optimización lineal (Minimizar)
prob = pulp.LpProblem("BWM_Lineal", pulp.LpMinimize)

# 3. Definir variables de decisión (pesos w_j e inconsistencia xi_L)
w = [pulp.LpVariable(f"w_{i}", lowBound=0.0, upBound=1.0) for i in range(n)]
xi = pulp.LpVariable("xi_L", lowBound=0.0)

# 4. Función objetivo: Minimizar xi_L
prob += xi

# 5. Restricción de suma: w1 + w2 + ... + wn = 1
prob += pulp.lpSum(w) == 1.0

# 6. Restricciones de desviación absoluta (|w_B - a_Bj * w_j| <= xi_L y |w_j - a_jW * w_W| <= xi_L)
for j in range(n):
    # Restricciones de desviación Best-to-Others
    prob += w[best_idx] - a_B[j] * w[j] <= xi
    prob += -(w[best_idx] - a_B[j] * w[j]) <= xi
    
    # Restricciones de desviación Others-to-Worst
    prob += w[j] - a_W[j] * w[worst_idx] <= xi
    prob += -(w[j] - a_W[j] * w[worst_idx]) <= xi

# 7. Resolver el modelo
prob.solve(pulp.PULP_CBC_CMD(msg=False))

if pulp.LpStatus[prob.status] == "Optimal":
    weights = [pulp.value(w_var) for w_var in w]
    xi_optimal = pulp.value(xi)
    
    # Razón de Consistencia (CR) de BWM
    a_BW = a_B[worst_idx]
    ci_dict = {1: 0.0, 2: 0.44, 3: 1.0, 4: 1.63, 5: 2.30, 6: 3.0, 7: 3.73, 8: 4.47, 9: 5.23}
    CI = ci_dict.get(a_BW, 5.23)
    CR = xi_optimal / CI if CI > 0.0 else 0.0
    
    print(f"Pesos óptimos: {weights}")
    print(f"Desviación óptima (xi*): {xi_optimal:.4f}")
    print(f"Razón de Consistencia (CR): {CR:.4f}")
else:
    print("El optimizador no pudo encontrar una solución factible.")
```

## 📄 Referencias Obligatorias
*   **Rezaei, J. (2015).** Best-worst multi-criteria decision-making method. *Omega*, 53, 49-57. [[Rezaei_2015_BWM|Ver Ficha de Lectura]].
*   **Rezaei, J. (2016).** Non-linear and linear models in best-worst multiple criteria decision-making. *Computers & Industrial Engineering*, 96, 19-25.
