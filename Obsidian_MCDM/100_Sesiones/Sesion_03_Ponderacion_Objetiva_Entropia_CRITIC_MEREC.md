---
type: session
tags: [sesion, clase, mcdm, ponderacion, objetiva]
session_title: "Ponderación Objetiva: Entropía, CRITIC y MEREC"
---
# 📚 Sesión 03: Ponderación Objetiva: Entropía, CRITIC y MEREC

**[[Mapa del curso (MOC)|<< Volver al Mapa del Curso]]**

## 🎯 Objetivos de la Sesión
*   **Analizar la filosofía matemática** de la ponderación objetiva basada en la variabilidad e interacción de los datos en lugar de la opinión de expertos.
*   **Formular e implementar** el cálculo de pesos a través de la **Entropía de Shannon** para medir el contenido de información de cada criterio.
*   **Calcular pesos óptimos** utilizando el método **CRITIC**, incorporando tanto la desviación estándar como la correlación lineal (Pearson) entre criterios.
*   **Evaluar la influencia del método MEREC** en la asignación de pesos a través del efecto de remoción de criterios.
*   **Contrastar críticamente** los resultados de pesos subjetivos (Sesión 2) y objetivos (Sesión 3) aplicados a un mismo conjunto de datos operativos de la cadena de suministro.

---

## 📝 Contenidos y Resumen

### 1. Filosofía de la Ponderación Objetiva
A diferencia de los métodos subjetivos (AHP, BWM) que capturan la preferencia del decisor o experto, los métodos objetivos deducen los pesos a partir de la **estructura matemática e intensidad de los datos empíricos** en la matriz de decisión.
*   **Principio de Discriminación:** Si todas las alternativas tienen el mismo valor en un criterio, ese criterio no ayuda a discriminar y su peso matemático debe tender a cero, sin importar lo importante que sea operativamente.
*   **Peligro metodológico:** El peso depende de la muestra. Si cambian las alternativas bajo evaluación, los pesos de los criterios cambian completamente. Se sugiere el uso de **pesos combinados** ($w_j = \alpha w_j^{sub} + (1-\alpha) w_j^{obj}$).

### 2. Entropía de Shannon
*   **Idea central:** Adapta el concepto de entropía de la teoría de la información (Claude Shannon, 1948) para medir la uniformidad en un criterio. Mayor uniformidad implica mayor desorden/entropía (poca información discriminatoria) y, por tanto, menor peso.
*   **Algoritmo:**
    1.  *Normalización sumatoria:* $p_{ij} = \frac{x_{ij}}{\sum_{i=1}^m x_{ij}}$ (los datos deben ser estrictamente positivos).
    2.  *Cálculo de Entropía ($e_j$):* $e_j = -k \sum_{i=1}^m p_{ij} \ln(p_{ij})$, donde $k = \frac{1}{\ln(m)}$ y $m$ es el número de alternativas.
        *   *Caso especial:* Si $p_{ij} = 0$, se define $0 \ln(0) = 0$.
    3.  *Grado de Divergencia ($d_j$):* $d_j = 1 - e_j$.
    4.  *Pesos normalizados:* $w_j = \frac{d_j}{\sum_{j=1}^n d_j}$.

### 3. Método CRITIC (Criteria Importance Through Intercriteria Correlation)
*   **Idea central:** Desarrollado por Diakoulaki et al. (1995) para solventar limitaciones de la Entropía, que ignora las relaciones entre criterios. Evalúa simultáneamente el **contraste** (desviación estándar) y el **conflicto** (correlación lineal de Pearson) entre los criterios.
*   **Algoritmo:**
    1.  *Normalización Max-Min* para unificar escalas en $[0, 1]$ (hacia maximización).
    2.  *Cálculo de desviación estándar* $\sigma_j$ de cada criterio (contraste).
    3.  *Cálculo del coeficiente de correlación* $r_{jk}$ (Pearson) entre criterios.
    4.  *Cálculo de cantidad de información:* $C_j = \sigma_j \sum_{k=1}^n (1 - r_{jk})$.
    5.  *Pesos normalizados:* $w_j = \frac{C_j}{\sum_{k=1}^n C_k}$.

### 4. Método MEREC (Removal Effects of Criteria)
*   **Idea central:** Propuesto por Keshavarz-Ghorabaee en 2021. Mide la importancia de un criterio eliminándolo de la matriz de decisión y observando cuánto altera el rendimiento global de las alternativas. Criterios que causan más alteración al removerse reciben pesos más altos.

---

## 💻 Recursos Prácticos
*   **Notebook del Taller:** [Ejemplo_Entropia_CRITIC.ipynb](file:///Users/leonardohernandez/Academica/Clase_MULTICRITERIO_DOCTORADO/Sesiones/Sesion_03/Ejemplo_Entropia_CRITIC.ipynb) con implementaciones detalladas de los algoritmos usando Pandas y NumPy vectorizado (sin usar librerías de "caja negra").
*   **Actividad del Taller:** [Actividad_Sesion_3.pdf](file:///Users/leonardohernandez/Academica/Clase_MULTICRITERIO_DOCTORADO/Sesiones/Sesion_03/Actividad_Sesion_3.pdf) / [Código LaTeX de Actividad](file:///Users/leonardohernandez/Academica/Clase_MULTICRITERIO_DOCTORADO/Sesiones/Sesion_03/Actividad_Sesion_3.tex).
*   **Diapositivas y Guía:** [Guia_Diapositivas_Sesion_3.md](file:///Users/leonardohernandez/Academica/Clase_MULTICRITERIO_DOCTORADO/Sesiones/Sesion_03/Guia_Diapositivas_Sesion_3.md) y [Plan de Clase](file:///Users/leonardohernandez/Academica/Clase_MULTICRITERIO_DOCTORADO/Sesiones/Sesion_03/Plan_Clase_Sesion_3.md).

---

## 📖 Bibliografía Recomendada
*   **Diakoulaki, D., Mavrotas, G., & Papayannakis, L. (1995).** Determining objective weights in multiple criteria problems: the CRITIC method. *Computers & Operations Research*, 22(7), 763–770. [[Diakoulaki_1995_CRITIC|Ver Ficha de Lectura]].
*   **Keshavarz-Ghorabaee, M., et al. (2021).** Determination of Objective Weights Using a New Method Based on the Removal Effects of Criteria (MEREC). *Symmetry*, 13(4), 525. [PDF Local](file:///Users/leonardohernandez/Academica/Clase_MULTICRITERIO_DOCTORADO/literatura/articulos/S08_Keshavarz_Ghorabaee_et_al_2021_Determination_of_Objective_Weights_Using_MEREC.pdf) | [[Keshavarz_2021_MEREC|Ver Ficha de Lectura]].
*   **Shannon, C. E. (1948).** A mathematical theory of communication. *Bell System Technical Journal*, 27, 379–423.

---

## 🗣️ Preguntas para Debate Socrático
1.  **La paradoja de la licitación:** Si el "Costo de Flete" es el criterio más importante para un director financiero, pero todos los proveedores cotizan casi exactamente la misma tarifa, la Entropía le dará un peso cercano a cero al costo. ¿Tiene sentido metodológico en la toma de decisiones reales? ¿Cuáles son los riesgos?
2.  **Redundancia de KPIs:** En logística medimos variables altamente correlacionadas (como exactitud de inventario, merma y rotura). ¿Por qué CRITIC es superior a la Entropía para lidiar con este conflicto?
3.  **Filosofía MEREC:** ¿Por qué medir el efecto de remoción de un criterio proporciona una perspectiva más robusta de su impacto que simplemente medir la variabilidad de su columna aislada?

---

## ✍️ Tareas y Entregables
*   Completar el taller práctico de los 10 transportistas en Python.
*   Trabajar en el **[[CP1_Ponderacion|Caso Práctico 1]]** (Ponderación de Criterios: AHP vs. BWM vs. Entropía), cuya entrega vence en la **Sesión 4** (Ponderación: **15%**).

---

## 📝 Notas de Clase (Toma de Apuntes)
*Escribe tus notas adicionales aquí y conecta con otros métodos de la carpeta [[200_Metodos]].*
