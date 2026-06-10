---
type: session
tags: [sesion, clase, mcdm, ponderacion]
session_title: "Ponderación Subjetiva: AHP y BWM"
---
# 📚 Sesión 02: Ponderación Subjetiva: AHP (Saaty) y Best-Worst Method (BWM)

**[[Mapa del curso (MOC)|<< Volver al Mapa del Curso]]**

## 🎯 Objetivos de la Sesión
*   **Analizar críticamente** los axiomas matemáticos del Proceso de Jerarquía Analítica (AHP) de Thomas Saaty.
*   **Evaluar** la validez científica y el fenómeno de *Rank Reversal* en AHP (Debate Dyer-Saaty).
*   **Dominar el algoritmo** y la formulación de optimización minimax del Best-Worst Method (BWM) desarrollado por Jafar Rezaei.
*   **Modelar y resolver** problemas de ponderación subjetiva aplicados a la toma de decisiones estratégicas en logística y cadena de suministro.

---

## 📝 Contenidos y Resumen

### 1. El Proceso de Jerarquía Analítica (AHP)
*   **Estructura Jerárquica:** Meta $\rightarrow$ Criterios $\rightarrow$ Subcriterios $\rightarrow$ Alternativas.
*   **Axiomas de Saaty:**
    1.  *Reciprocidad:* $a_{ji} = 1/a_{ij}$.
    2.  *Homogeneidad:* Elementos comparados en la misma escala de magnitud.
    3.  *Dependencia:* Las prioridades dependen del nivel superior inmediato.
    4.  *Expectativas:* Modificaciones de estructura requieren revaluación de expectativas.
*   **Escala de Saaty (1-9):** Basada en psicología cognitiva (Ley de Miller, $7 \pm 2$).
*   **Elicitación del Peso:** Método del Autovector Principal ($\mathbf{A}\mathbf{w} = \lambda_{\max}\mathbf{w}$).
*   **Consistencia:**
    *   Índice de Consistencia: $CI = \frac{\lambda_{\max} - n}{n-1}$.
    *   Razón de Consistencia: $CR = \frac{CI}{RI}$ (donde $RI$ es el índice aleatorio para matriz de tamaño $n$).
    *   *Regla de decisión:* Si $CR < 0.10$, los juicios son consistentes; de lo contrario, se deben revisar.
*   **Debate Rank Reversal (Dyer vs. Saaty, 1990):** La adición de alternativas irrelevantes puede cambiar el orden de las originales. Dyer propone violar el axioma de independencia de alternativas irrelevantes como un fallo metodológico; Saaty argumenta que es comportamiento natural de la psicología humana.

### 2. Best-Worst Method (BWM)
*   **Filosofía:** Desarrollado por Rezaei (2015) para solventar limitaciones de AHP. Requiere únicamente $2n - 3$ comparaciones (frente a $n(n-1)/2$ de AHP), reduciendo la carga cognitiva y aumentando la consistencia.
*   **Algoritmo:**
    1.  Identificar el mejor criterio ($C_B$) y el peor ($C_W$).
    2.  Vector *Best-to-Others* ($A_B$): $a_{Bj}$ (preferencia de $C_B$ sobre $C_j$, escala 1-9).
    3.  Vector *Others-to-Worst* ($A_W$): $a_{jW}$ (preferencia de $C_j$ sobre $C_W$, escala 1-9).
*   **Formulación Linealizada:**
    $$\begin{aligned}
    \min \quad & \xi^L \\
    \text{s.t.} \quad & |w_B - a_{Bj}w_j| \le \xi^L, \quad \forall j \\
    & |w_j - a_{jW}w_W| \le \xi^L, \quad \forall j \\
    & \sum_{j=1}^n w_j = 1, \quad w_j \ge 0
    \end{aligned}$$
*   **Razón de Consistencia:** $CR = \frac{\xi^*}{CI_{bwm}}$, donde $CI_{bwm}$ es el índice de consistencia mínima de Rezaei según la preferencia de $a_{BW}$.

---

## 💻 Recursos Prácticos
*   **Ejemplo Resuelto:** [Ejemplo_Resuelto_AHP_BWM.tex](file:///Users/leonardohernandez/Academica/Clase_MULTICRITERIO_DOCTORADO/Sesiones/Sesion_02/Ejemplo_Resuelto_AHP_BWM.tex) y su PDF compilado [Ejemplo_Resuelto_AHP_BWM.pdf](file:///Users/leonardohernandez/Academica/Clase_MULTICRITERIO_DOCTORADO/Sesiones/Sesion_02/Ejemplo_Resuelto_AHP_BWM.pdf).
*   **Notebook del Taller:** [Ejemplo_AHP_BWM.ipynb](file:///Users/leonardohernandez/Academica/Clase_MULTICRITERIO_DOCTORADO/Sesiones/Sesion_02/Ejemplo_AHP_BWM.ipynb) con implementaciones paso a paso en Python (`numpy.linalg.eig` y `PuLP`).
*   **Caso de Reto:** Selección de Ubicación de un nuevo CEDIS, incluido al final del PDF del ejemplo resuelto.

---

## 📖 Bibliografía Recomendada
*   **Saaty, T. L. (1980).** *The Analytic Hierarchy Process*. McGraw-Hill.
*   **Rezaei, J. (2015).** Best-worst multi-criteria decision-making method. *Omega*, 53, 49-57.
*   **Rezaei, J. (2016).** Non-linear and linear models in best-worst multiple criteria decision-making. *Computers & Industrial Engineering*, 96, 19-25.
*   **Dyer, J. S. (1990).** Remarks on the analytic hierarchy process. *Management Science*, 36(3), 249-258.

---

## ✍️ Tareas y Entregables
*   Completar el **Caso de Reto** de localización del nuevo CEDIS comparando los pesos AHP y BWM mediante Python.
*   Entregable **E1** (Caso Práctico 1: Ponderación de Criterios con AHP, BWM y Entropía).

---

## 📝 Notas de Clase (Toma de Apuntes)
*Escribe tus notas adicionales aquí y conecta con otros métodos de la carpeta [[200_Metodos]].*
