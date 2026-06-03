---
type: case-example
tags: [ejemplo, resuelto, actividad_1, MCDM]
---
# 📚 Ejemplo Resuelto de la Actividad Práctica 1: El Dilema del Decisor

Este documento contiene un ejemplo completamente resuelto y explicado paso a paso para servir como guía matemática e institucional a los estudiantes del doctorado. Se ha seleccionado la **Opción A (Selección de Operador Logístico 3PL)** para ilustrar el proceso completo.

---

## 1. Planteamiento y Estructuración del Problema

Se evalúa la contratación de un operador logístico (3PL) para la distribución de mercancía de e-commerce desde Monterrey. El modelo formal se define de la siguiente manera:

*   **Alternativas ($m=4$):**
    *   $A_1$: Transportista Consolidado Nacional
    *   $A_2$: Proveedor Regional Especializado
    *   $A_3$: Startup Logística Tecnológica
    *   $A_4$: Transportista Tradicional de Carga General
*   **Criterios ($n=5$):**
    *   $C_1$: Costo de flete por envío (Minimizar, cuantitativo, en MXN)
    *   $C_2$: Tiempo de tránsito promedio (Minimizar, cuantitativo, en horas)
    *   $C_3$: Nivel de cumplimiento / OTIF (Maximizar, cuantitativo, en \%)
    *   $C_4$: Visibilidad y rastreo (Maximizar, cualitativo, escala Likert 1--5)
    *   $C_5$: Flexibilidad ante urgencias (Maximizar, cualitativo, escala Likert 1--5)

---

## 2. Matriz de Decisión Original ($X$)

A partir de estimaciones de mercado y cotizaciones reales, construimos la matriz $X_{4 \times 5}$:

| Alternativa / Criterio | $C_1$ (Costo: Min) | $C_2$ (Tiempo: Min) | $C_3$ (OTIF: Max) | $C_4$ (Tech: Max) | $C_5$ (Flex: Max) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **$A_1$ (Nacional)** | \$11,000 | 30 h | 88\% | 2 | 1 |
| **$A_2$ (Regional)** | \$18,000 | 18 h | 95\% | 3 | 4 |
| **$A_3$ (Startup)** | \$24,000 | 14 h | 97\% | 5 | 5 |
| **$A_4$ (Tradicional)** | \$9,000 | 36 h | 82\% | 1 | 2 |

---

## 3. Normalización de Desempeños ($R$) Paso a Paso

Utilizamos el método de **Normalización Lineal Max-Min**. Este paso elimina las unidades físicas (MXN, horas, \%, escala ordinal) y proyecta el desempeño de cada alternativa en un rango uniforme $[0, 1]$, donde $1$ representa el mejor desempeño teórico del grupo y $0$ el peor.

### 3.1. Criterios de Costo (Minimizar): $C_1$ y $C_2$
Fórmula:
$$r_{ij} = \frac{\max_{k} x_{kj} - x_{ij}}{\max_{k} x_{kj} - \min_{k} x_{kj}}$$

*   **Para el criterio $C_1$ (Costo):**
    *   $\max_{k} x_{k1} = \$24,000$ (Startup)
    *   $\min_{k} x_{k1} = \$9,000$ (Tradicional)
    *   Denominador (Rango): $24,000 - 9,000 = 15,000$
    *   Calculamos las puntuaciones normalizadas:
        *   $r_{11} = \frac{24,000 - 11,000}{15,000} = \frac{13,000}{15,000} \approx \mathbf{0.867}$
        *   $r_{21} = \frac{24,000 - 18,000}{15,000} = \frac{6,000}{15,000} = \mathbf{0.400}$
        *   $r_{31} = \frac{24,000 - 24,000}{15,000} = \frac{0}{15,000} = \mathbf{0.000}$ (Peor opción en costos)
        *   $r_{41} = \frac{24,000 - 9,000}{15,000} = \frac{15,000}{15,000} = \mathbf{1.000}$ (Mejor opción en costos)

*   **Para el criterio $C_2$ (Tiempo):**
    *   $\max_{k} x_{k2} = 36$ h (Tradicional)
    *   $\min_{k} x_{k2} = 14$ h (Startup)
    *   Denominador (Rango): $36 - 14 = 22$
    *   Calculamos:
        *   $r_{12} = \frac{36 - 30}{22} = \frac{6}{22} \approx \mathbf{0.273}$
        *   $r_{22} = \frac{36 - 18}{22} = \frac{18}{22} \approx \mathbf{0.818}$
        *   $r_{32} = \frac{36 - 14}{22} = \frac{22}{22} = \mathbf{1.000}$ (Mejor opción en velocidad)
        *   $r_{42} = \frac{36 - 36}{22} = \frac{0}{22} = \mathbf{0.000}$ (Peor opción en velocidad)

---

### 3.2. Criterios de Beneficio (Maximizar): $C_3$, $C_4$ y $C_5$
Fórmula:
$$r_{ij} = \frac{x_{ij} - \min_{k} x_{kj}}{\max_{k} x_{kj} - \min_{k} x_{kj}}$$

*   **Para el criterio $C_3$ (OTIF):**
    *   $\max_{k} x_{k3} = 97\%$
    *   $\min_{k} x_{k3} = 82\%$
    *   Denominador: $97 - 82 = 15$
    *   Calculamos:
        *   $r_{13} = \frac{88 - 82}{15} = \frac{6}{15} = \mathbf{0.400}$
        *   $r_{23} = \frac{95 - 82}{15} = \frac{13}{15} \approx \mathbf{0.867}$
        *   $r_{33} = \frac{97 - 82}{15} = \frac{15}{15} = \mathbf{1.000}$
        *   $r_{43} = \frac{82 - 82}{15} = \frac{0}{15} = \mathbf{0.000}$

*   **Para el criterio $C_4$ (Tech) y $C_5$ (Flex):**
    *   En ambos criterios, la escala cualitativa tiene $\max = 5$ y $\min = 1$.
    *   Denominador: $5 - 1 = 4$.
    *   **Criterio $C_4$ (Tecnología):**
        *   $r_{14} = \frac{2 - 1}{4} = \mathbf{0.250}$
        *   $r_{24} = \frac{3 - 1}{4} = \mathbf{0.500}$
        *   $r_{34} = \frac{5 - 1}{4} = \mathbf{1.000}$
        *   $r_{44} = \frac{1 - 1}{4} = \mathbf{0.000}$
    *   **Criterio $C_5$ (Flexibilidad):**
        *   $r_{15} = \frac{1 - 1}{4} = \mathbf{0.000}$
        *   $r_{25} = \frac{4 - 1}{4} = \mathbf{0.750}$
        *   $r_{35} = \frac{5 - 1}{4} = \mathbf{1.000}$
        *   $r_{45} = \frac{2 - 1}{4} = \mathbf{0.250}$

---

### 3.3. Matriz Normalizada ($R$) Resultante

Juntando los valores normalizados calculados en una matriz única:

| Alternativa / Criterio | $C_1$ (Min) | $C_2$ (Min) | $C_3$ (Max) | $C_4$ (Max) | $C_5$ (Max) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **$A_1$ (Nacional)** | 0.867 | 0.273 | 0.400 | 0.250 | 0.000 |
| **$A_2$ (Regional)** | 0.400 | 0.818 | 0.867 | 0.500 | 0.750 |
| **$A_3$ (Startup)** | 0.000 | 1.000 | 1.000 | 1.000 | 1.000 |
| **$A_4$ (Tradicional)** | 1.000 | 0.000 | 0.000 | 0.000 | 0.250 |

---

## 4. Ponderación y Cálculo de Puntuaciones Globales ($S_i$)

Mostramos la sensibilidad del ranking final ante dos escenarios de preferencias subjetivas distintas:

### Escenario 1: Decisor Equitativo (Pesos Homogéneos)
Suponemos que el decisor asigna el mismo nivel de importancia a las 5 dimensiones:
$$W_{eq} = [0.20, 0.20, 0.20, 0.20, 0.20]^T$$

Aplicamos la ecuación $S_i = \sum_{j=1}^5 w_j r_{ij}$:
*   **$S(A_1)$** $= 0.20(0.867 + 0.273 + 0.400 + 0.250 + 0.000) = 0.20(1.790) = \mathbf{0.358}$
*   **$S(A_2)$** $= 0.20(0.400 + 0.818 + 0.867 + 0.500 + 0.750) = 0.20(3.335) = \mathbf{0.667}$
*   **$S(A_3)$** $= 0.20(0.000 + 1.000 + 1.000 + 1.000 + 1.000) = 0.20(4.000) = \mathbf{0.800}$
*   **$S(A_4)$** $= 0.20(1.000 + 0.000 + 0.000 + 0.000 + 0.250) = 0.20(1.250) = \mathbf{0.250}$

**Ranking Resultante (Escenario 1):**
$$A_3 \succ A_2 \succ A_1 \succ A_4$$
*La Startup ($A_3$) es la mejor opción debido a su desempeño excepcional en tiempo de entrega, OTIF, tecnología y flexibilidad, lo cual compensa por completo su elevado costo.*

---

### Escenario 2: Decisor Altamente Enfocado en Costos
El decisor tiene un presupuesto severamente restringido y otorga el 80\% del peso al costo de flete ($C_1$), distribuyendo el 20\% restante equitativamente entre los demás criterios (5\% cada uno):
$$W_{costo} = [0.80, 0.05, 0.05, 0.05, 0.05]^T$$

*   **$S(A_1)$** $= 0.80(0.867) + 0.05(0.273 + 0.400 + 0.250 + 0.000) = 0.6936 + 0.05(0.923) \approx \mathbf{0.740}$
*   **$S(A_2)$** $= 0.80(0.400) + 0.05(0.818 + 0.867 + 0.500 + 0.750) = 0.3200 + 0.05(2.935) \approx \mathbf{0.467}$
*   **$S(A_3)$** $= 0.80(0.000) + 0.05(1.000 + 1.000 + 1.000 + 1.000) = 0.0000 + 0.05(4.000) = \mathbf{0.200}$
*   **$S(A_4)$** $= 0.80(1.000) + 0.05(0.000 + 0.000 + 0.000 + 0.250) = 0.8000 + 0.05(0.250) = \mathbf{0.813}$

**Ranking Resultante (Escenario 2):**
$$A_4 \succ A_1 \succ A_2 \succ A_3$$
*El ranking se invierte por completo. La alternativa tradicional de bajo costo ($A_4$) se convierte en la ganadora, seguida del operador nacional ($A_1$). La startup ($A_3$) cae al último lugar.*

---

## 5. Respuestas a las Preguntas de Reflexión Académica

1.  **La Paradoja de la Inconmensurabilidad (Impacto de omitir la Normalización):**
    Si no normalizáramos, estaríamos sumando valores en unidades y escalas dispares de forma directa:
    $$S_i = w_1 (\text{MXN}) + w_2 (\text{horas}) + w_3 (\text{\%}) + w_4 (\text{escala}) + w_5 (\text{escala})$$
    Debido a que el Criterio 1 se expresa en miles de pesos (\$9,000 a \$24,000) y los otros criterios están expresados en números pequeños (como 12--36 horas, u 80--99\%, u ordinales de 1--5), el valor de $C_1$ es del orden de $10^4$ veces mayor que los demás. Matemáticamente, el flete dominaría el 99.9\% de la suma ponderada independientemente del peso asignado. La normalización de desempeños es indispensable para aislar la dimensionalidad física del valor numérico de desempeño relativo.

2.  **Sensibilidad a las preferencias:**
    Como se demostró en los cálculos del apartado anterior, variar los pesos de un esquema equitativo a uno sesgado al costo alteró la jerarquía de alternativas:
    *   Bajo $W_{eq}$: $A_3 \succ A_2 \succ A_1 \succ A_4$ (Startup como opción dominante).
    *   Bajo $W_{costo}$: $A_4 \succ A_1 \succ A_2 \succ A_3$ (Tradicional como opción dominante).
    Esto prueba que la ayuda a la decisión multicriterio (MCDM) no persigue encontrar un "óptimo de Pareto abstracto y único", sino una solución que sea matemáticamente coherente con el sistema de valores subjetivos de un decisor en un momento y contexto específico (racionalidad procedimental).

3.  **Límites de la Optimización Clásica en MCDM:**
    La optimización matemática clásica (ej. Programación Lineal por Simplex) requiere definir una sola función objetivo (ej. minimizar costos) sujeta a restricciones rígidas (ej. tiempo $\le 20$ horas). Si intentamos resolver este caso mediante ese paradigma:
    *   El modelo descartaría por completo la startup ($A_3$) y el transportista regional ($A_2$) si el límite de tiempo fuera rigurosamente $\le 15$ horas o la tarifa máxima $\le \$12,000$, impidiendo la exploración de soluciones intermedias robustas.
    *   Ignoraría el valor de la flexibilidad y la tecnología al no ser ecuaciones lineales explícitas de costo/tiempo, simplificando de forma artificial un problema organizativo complejo y dinámico en un simple problema numérico de cotización.
