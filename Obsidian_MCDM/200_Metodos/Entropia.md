---
type: method
tags: [metodo, teoria, mcdm, ponderacion, objetiva]
method_name: "Entropía de Shannon"
creator: "Shannon"
---
# 🔧 Entropía de Shannon (Ponderación Objetiva)

**[[Mapa del curso (MOC)|<< Volver al Mapa del Curso]]**

## 📝 Descripción General
Es un método de ponderación **objetiva** que asigna pesos a los criterios basándose exclusivamente en la variabilidad de los datos de la matriz de decisión. Se fundamenta en la teoría de la información de Claude Shannon (1948). Un criterio con alta variabilidad entre alternativas aporta mayor información útil (baja entropía), por lo que recibe un mayor peso; un criterio con valores muy homogéneos aporta poca información (alta entropía) y recibe un peso bajo.

## 📐 Estructura Matemática Básica
Dada una matriz de decisión de $m$ alternativas y $n$ criterios:

1.  **Normalización sumatoria:**
    $$p_{ij} = \frac{x_{ij}}{\sum_{i=1}^m x_{ij}}, \quad \forall j$$
    *Nota: Todos los datos deben ser estrictamente positivos ($x_{ij} > 0$).*

2.  **Cálculo de la Entropía ($e_j$):**
    $$e_j = -k \sum_{i=1}^m p_{ij} \ln(p_{ij}), \quad \forall j$$
    Donde la constante de escala es $k = \frac{1}{\ln(m)}$, garantizando que $0 \le e_j \le 1$.
    *Tratamiento de indeterminación:* Si $p_{ij} = 0$, se define analíticamente como $\lim_{p \to 0} p \ln(p) = 0$.

3.  **Grado de Divergencia ($d_j$):**
    $$d_j = 1 - e_j, \quad \forall j$$

4.  **Cálculo de pesos ($w_j$):**
    $$w_j = \frac{d_j}{\sum_{j=1}^n d_j}, \quad \forall j$$

## ⚠️ Límites y Consideraciones
*   **Independencia de criterios:** Ignora por completo las correlaciones o dependencias entre criterios. Si se introducen tres criterios redundantes y altamente correlacionados (ej. costo de flete, costo de maniobra, costo de combustible), la Entropía les asignará un gran peso individual, duplicando/triplicando su importancia real.
*   **Dependencia de la muestra:** Si se añade o remueve una alternativa irrelevante, las proporciones cambian y con ello el peso final de todos los criterios.
*   **Alineación de objetivos:** Requiere que los criterios de costo sean invertidos previamente ($1/x_{ij}$) o mapeados a escalas de beneficio antes de la normalización sumatoria.

## 💻 Herramientas y Software
*   **Python:** Operaciones vectorizadas con `numpy` y `pandas`.
    ```python
    # Evitar indeterminación de logaritmo con p = 0
    p = decision_matrix / decision_matrix.sum(axis=0)
    entropy = - (p * np.log(p.replace(0, 1))).sum(axis=0) / np.log(len(p))
    divergence = 1 - entropy
    weights = divergence / divergence.sum()
    ```
*   **R:** Paquete `MCDM` (`entropy_method`).

## 📄 Papers de Referencia Relacionados
*   **Keshavarz-Ghorabaee, M. (2021).** [[Keshavarz_2021_MEREC|MEREC Method]] (contiene comparaciones conceptuales de entropía).
