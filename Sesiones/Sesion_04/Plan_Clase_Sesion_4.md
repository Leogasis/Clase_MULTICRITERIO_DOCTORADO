# Plan de Clase Detallado: Sesión 4
**Materia:** Herramientas Multicriterio para Toma de Decisiones  
**Programa:** Doctorado en Logística y Cadena de Suministro, FIME – UANL  
**Duración:** 3 horas (180 minutos)  
**Profesor:** Dr. Leonardo Gabriel Hernández Landa  
**Tema General:** Paradigma de Distancia Geométrica: TOPSIS, VIKOR y variantes  

---

## 🎯 Objetivos de la Sesión
Al finalizar esta cuarta sesión, el estudiante de doctorado será capaz de:
1. **Dominar los fundamentos geométricos** del concepto de compromiso y distancias a puntos ideales y anti-ideales.
2. **Implementar paso a paso** el algoritmo de TOPSIS utilizando normalización vectorial y distancias euclidianas.
3. **Modelar y resolver** problemas mediante el método VIKOR, distinguiendo la diferencia matemática entre la utilidad del grupo (mínimo arrepentimiento individual) y el arrepentimiento de la mayoría.
4. **Verificar la estabilidad** de los rankings resultantes empleando coeficientes de correlación de Spearman y de similitud de Kendall.
5. **Aplicar estos enfoques** al problema de localización estratégica de micro-hubs urbanos de última milla.

---

## ⏱️ Estructura del Tiempo (180 minutos en total)

| Bloque | Actividad | Tiempo | Porcentaje |
| :--- | :--- | :---: | :---: |
| **Bloque 1** | Exposición Teórica (Puntos ideales, métrica $L_p$, algoritmos de TOPSIS y VIKOR) | 90 min | 50% |
| **Bloque 2** | Debate Socrático de Literatura (Comparativa de similitud de rankings en papers Q1) | 45 min | 25% |
| **Bloque 3** | Taller Aplicado y Ejercicios (Resolución de TOPSIS en Excel/Python y validación de concordancia) | 45 min | 25% |

---

## 📚 Preparación Previa Requerida (Flipped Classroom)
*Los estudiantes debieron leer con antelación los siguientes recursos:*
1. **Artículo:** *A comparative case study of the VIKOR and TOPSIS rankings similarity*. Procedia Computer Science (2020). [S05_Comparative_Case_Study_VIKOR_TOPSIS_Rankings_Similarity_2020.pdf](file:///Users/leonardohernandez/Academica/Clase_MULTICRITERIO_DOCTORADO/literatura/articulos/S05_Comparative_Case_Study_VIKOR_TOPSIS_Rankings_Similarity_2020.pdf)
2. **Artículo:** *Comparative analyses of multi-criteria methods in supplier selection problem*. Procedia Computer Science, 207 (2022), 4593–4602. [S05_Comparative_Analyses_MCDM_Methods_Supplier_Selection_2022.pdf](file:///Users/leonardohernandez/Academica/Clase_MULTICRITERIO_DOCTORADO/literatura/articulos/S05_Comparative_Analyses_MCDM_Methods_Supplier_Selection_2022.pdf)
3. **Guía de Lectura Asignada:** 
   * ¿Cuál es la diferencia en la métrica de distancia de Minkowski ($L_p$) utilizada por TOPSIS ($p=2$, euclidiana) frente a VIKOR ($p=1$, distancia lineal y $p=\infty$, arrepentimiento máximo)?
   * ¿Qué representa el parámetro $v$ (peso de la estrategia de la mayoría de los criterios) en el cálculo del índice multiatributo $Q$ de VIKOR?

---

## 📖 Contenido Temático y Desarrollo de la Sesión

### BLOQUE 1: Exposición Teórica (90 min)
* **La Noción Matemática del Punto de Compromiso:**
  * Distancia de Minkowski y su rol en la toma de decisiones.
* **El Algoritmo TOPSIS (Hwang \& Yoon, 1981):**
  * Normalización vectorial y ponderación de la matriz.
  * Solución Ideal Positiva ($A^*$) e Ideal Negativa ($A^-$).
  * Distancias euclidianas $S_i^*$ y $S_i^-$.
  * Coeficiente de proximidad relativa: $C_i^* = S_i^- / (S_i^* + S_i^-)$.
* **El Algoritmo VIKOR (Opricovic, 1998):**
  * Determinación de los mejores ($f_j^*$) y peores ($f_j^-$) valores del dataset.
  * Medición de la utilidad global $S_i$ (distancia L1) y del arrepentimiento individual $R_i$ (distancia Chebyshev).
  * Cálculo del índice de compromiso: $Q_i = v \frac{S_i - S^*}{S^- - S^*} + (1-v) \frac{R_i - R^*}{R^- - R^*}$.
  * Condiciones de estabilidad aceptable y ventaja aceptable.

---

### BLOQUE 2: Discusión de Literatura - Debate Socrático (45 min)
* **Pregunta Detonante 1:** *En los dos artículos de Procedia Computer Science revisados, se observa que TOPSIS y VIKOR suelen generar rankings diferentes para un mismo dataset. Basado en sus lógicas de distancia, ¿cuál de los dos métodos es más propenso a seleccionar una alternativa mediocre pero balanceada frente a una alternativa excelente en la mayoría de los criterios pero deficiente en uno?*
* **Pregunta Detonante 2:** *En un problema de localización de CEDIS, ¿cómo afecta el cambio del parámetro de peso de la mayoría $v$ en VIKOR al consenso del consejo corporativo?*

---

### BLOQUE 3: Taller Práctico - Ejercicios (45 min)

#### 3.1. Ejercicio Guiado (Profesor): Formulación y Resolución de TOPSIS
El profesor modelará un problema de localización de un almacén refrigerado en Monterrey comparando 3 sitios con 4 criterios (costo del terreno, accesibilidad, tiempo de respuesta a clientes, consumo de energía) resolviéndolo en Python mediante código matricial explícito.

#### 3.2. Caso Práctico Alumno (Trabajo Autónomo)
El alumno resolverá un problema de selección de modo de transporte intermodal transfronterizo evaluando 5 rutas con pesos precalculados en la Sesión 3 utilizando TOPSIS y VIKOR.
* **Entregable:** Matriz normalizada, cálculo de distancias y concordancia de rankings mediante coeficiente de Spearman.

---

## 🎓 Plan de Evidencias (Evaluación)
* **Entrega:** En esta sesión se recopila y califica el **E1 (Caso Práctico 1: Ponderación de Criterios: AHP, BWM y Entropía)** (15%).
* **Asignación:** Se abre la convocatoria para el **E2 (Caso Práctico 2: Jerarquización por Distancias: TOPSIS vs. VIKOR)**, a entregarse en la **Sesión 6** (Ponderación **20%**).
