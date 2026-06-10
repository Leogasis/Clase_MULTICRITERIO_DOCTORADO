---
type: method
tags: [metodo, teoria, mcdm, ponderacion, objetiva]
method_name: "Criteria Importance Through Intercriteria Correlation (CRITIC)"
creator: "Diakoulaki, Mavrotas & Papayannakis"
---
# 🔧 Método CRITIC (Ponderación Objetiva)

**[[Mapa del curso (MOC)|<< Volver al Mapa del Curso]]**

## 📝 Descripción General
El método **CRITIC** (Diakoulaki et al., 1995) es una técnica de ponderación objetiva diseñada para resolver una limitación crítica de la Entropía: la omisión de las interrelaciones entre criterios. CRITIC determina el peso de un criterio combinando:
1.  **El contraste de la información (Variabilidad):** Representado por la desviación estándar ($\sigma_j$). A mayor desviación, mayor poder discriminatorio del criterio.
2.  **El conflicto intercriterio (Correlación):** Representado por el coeficiente de correlación lineal de Pearson ($r_{jk}$). Criterios fuertemente correlacionados positivamente son redundantes (conflicto bajo) y ven su peso penalizado; criterios independientes o negativamente correlacionados aportan información nueva y reciben más peso.

## 📐 Estructura Matemática Básica
Dada una matriz de decisión de $m$ alternativas y $n$ criterios:

1.  **Normalización Max-Min (hacia beneficio):**
    *   Para criterios de beneficio:
        $$r_{ij} = \frac{x_{ij} - x_j^{\min}}{x_j^{\max} - x_j^{\min}}$$
    *   Para criterios de costo:
        $$r_{ij} = \frac{x_j^{\max} - x_{ij}}{x_j^{\max} - x_j^{\min}}$$

2.  **Cálculo de la Desviación Estándar ($\sigma_j$):**
    Calculada sobre cada columna de la matriz normalizada $r_{ij}$.

3.  **Cálculo de la Matriz de Correlación ($r_{jk}$):**
    Coeficiente de Pearson entre la columna del criterio $j$ y la columna del criterio $k$.

4.  **Cálculo de la Cantidad de Información ($C_j$):**
    $$C_j = \sigma_j \sum_{k=1}^n (1 - r_{jk})$$

5.  **Cálculo de pesos ($w_j$):**
    $$w_j = \frac{C_j}{\sum_{k=1}^n C_k}$$

## ⚠️ Límites y Consideraciones
*   **Linealidad:** Al usar la correlación de Pearson, CRITIC solo evalúa relaciones lineales. Dependencias no lineales complejas entre criterios pueden ser omitidas.
*   **Sensibilidad a Outliers:** La normalización Max-Min inicial es muy sensible a datos atípicos, lo que puede distorsionar los valores de la desviación estándar y los pesos finales.
*   **Pesos Negativos en Correlaciones:** Si bien la fórmula $(1 - r_{jk})$ maneja correlaciones negativas de forma que incrementan la cantidad de información (lo cual es lógico), el analista debe cuidar la interpretación física de criterios que se oponen entre sí.

## 💻 Herramientas y Software
*   **Python:**
    *   Implementación directa con NumPy y Pandas:
        ```python
        norm_matrix = (df - df.min()) / (df.max() - df.min()) # Asumiendo todos beneficio
        std_devs = norm_matrix.std(ddof=0)
        corr_matrix = norm_matrix.corr(method='pearson')
        conflict = (1 - corr_matrix).sum(axis=1)
        C = std_devs * conflict
        weights = C / C.sum()
        ```
    *   Librería `pyDecision`: `from pyDecision.algorithm import critic_method`.

## 📄 Papers de Referencia Relacionados
*   **Diakoulaki, D., Mavrotas, G., & Papayannakis, L. (1995).** [[Diakoulaki_1995_CRITIC|Determining objective weights in multiple criteria problems: the CRITIC method]].
