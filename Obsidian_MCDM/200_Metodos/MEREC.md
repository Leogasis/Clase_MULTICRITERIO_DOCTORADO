---
type: method
tags: [metodo, teoria, mcdm, ponderacion, objetiva]
method_name: "Method Based on the Removal Effects of Criteria (MEREC)"
creator: "Keshavarz-Ghorabaee, Amiri, Zavadskas, Turskis & Antucheviciene"
---
# 🔧 Método MEREC (Ponderación Objetiva)

**[[Mapa del curso (MOC)|<< Volver al Mapa del Curso]]**

## 📝 Descripción General
El método **MEREC** (*Method Based on the Removal Effects of Criteria*), propuesto por Keshavarz-Ghorabaee et al. (2021), es una aproximación novedosa a la ponderación objetiva. A diferencia de la Entropía y CRITIC, que analizan directamente las variaciones dentro de cada columna, MEREC determina la importancia de un criterio midiendo el **efecto de su remoción** sobre la puntuación global de desempeño de las alternativas.
*   **Filosofía:** Si la eliminación de un criterio $C_j$ causa una gran desviación en la evaluación general de las alternativas, significa que ese criterio tiene una alta influencia en la matriz y, por ende, recibe un mayor peso. Si su remoción apenas altera las posiciones relativas, su peso es menor.

## 📐 Estructura Matemática Básica
Dada una matriz de decisión con $m$ alternativas y $n$ criterios:

1.  **Normalización no convencional:**
    En MEREC, la normalización busca que los peores desempeños tengan valores más cercanos a 1.
    *   Para criterios de beneficio (maximizar):
        $$n_{ij} = \frac{\min_k x_{kj}}{x_{ij}}$$
    *   Para criterios de costo (minimizar):
        $$n_{ij} = \frac{x_{ij}}{\max_k x_{kj}}$$

2.  **Cálculo del Desempeño Global de las Alternativas ($S_i$):**
    Utiliza una función logarítmica sumatoria de la matriz normalizada:
    $$S_i = \ln \left( 1 + \left( \frac{1}{n} \sum_{j=1}^n | \ln(n_{ij}) | \right) \right), \quad \forall i=1,\dots,m$$

3.  **Cálculo del Desempeño Global Removiendo el Criterio $j$ ($S'_{ij}$):**
    Para cada alternativa $i$, se recalcula su desempeño omitiendo el criterio $C_j$:
    $$S'_{ij} = \ln \left( 1 + \left( \frac{1}{n} \sum_{k \ne j} | \ln(n_{ik}) | \right) \right), \quad \forall i=1,\dots,m, \quad j=1,\dots,n$$

4.  **Cálculo del Efecto de Remoción Absoluto ($E_j$):**
    Suma de las desviaciones absolutas para el criterio $C_j$:
    $$E_j = \sum_{i=1}^m | S'_{ij} - S_i |$$

5.  **Cálculo de Pesos Normalizados ($w_j$):**
    $$w_j = \frac{E_j}{\sum_{k=1}^n E_k}$$

## ⚠️ Límites y Consideraciones
*   **Novedad:** Es un método muy reciente (2021), por lo que su adopción en la literatura de transporte y logística está creciendo pero aún no es tan ubicua como AHP o Entropía.
*   **Carga Computacional:** Requiere recalcular las puntuaciones de las alternativas $n$ veces (una por cada criterio removido), lo cual incrementa el esfuerzo de cómputo comparado con la Entropía, aunque para matrices típicas esto es instantáneo en Python.

## 💻 Herramientas y Software
*   **Python:** Implementación directa con operaciones vectorizadas.
    ```python
    # Normalización MEREC
    # (Asumiendo df con columnas identificadas por tipo)
    n_matrix = pd.DataFrame(index=df.index, columns=df.columns)
    for col in df.columns:
        if is_benefit[col]:
            n_matrix[col] = df[col].min() / df[col]
        else:
            n_matrix[col] = df[col] / df[col].max()
            
    # Desempeño general S_i
    ln_n = np.abs(np.log(n_matrix))
    S = np.log(1 + (1 / len(df.columns)) * ln_n.sum(axis=1))
    
    # Remoción y cálculo de E_j
    E = []
    n_crit = len(df.columns)
    for col in df.columns:
        cols_without = [c for c in df.columns if c != col]
        S_prime = np.log(1 + (1 / n_crit) * ln_n[cols_without].sum(axis=1))
        E_j = np.abs(S_prime - S).sum()
        E.append(E_j)
        
    weights = np.array(E) / sum(E)
    ```

## 📄 Papers de Referencia Relacionados
*   **Keshavarz-Ghorabaee, M., et al. (2021).** [[Keshavarz_2021_MEREC|Determination of Objective Weights Using a New Method Based on the Removal Effects of Criteria (MEREC)]].
