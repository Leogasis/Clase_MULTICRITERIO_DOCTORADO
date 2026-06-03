# Plan de Clase Detallado: Sesión 7
**Materia:** Herramientas Multicriterio para Toma de Decisiones  
**Programa:** Doctorado en Logística y Cadena de Suministro, FIME – UANL  
**Duración:** 3 horas (180 minutos)  
**Profesor:** Dr. Leonardo Gabriel Hernández Landa  
**Tema General:** Lógica Difusa y Conjuntos Difusos en MCDM: Fuzzy AHP y Fuzzy TOPSIS  

---

## 🎯 Objetivos de la Sesión
Al finalizar esta séptima sesión, el estudiante de doctorado será capaz de:
1. **Comprender los fundamentos matemáticos** de la lógica difusa y su rol en la modelación de la subjetividad y vaguedad lingüística en logística.
2. **Definir y operar con Números Difusos Triangulares (TFNs)**, ejecutando sumas, multiplicaciones y divisiones difusas de forma analítica.
3. **Implementar el algoritmo Fuzzy TOPSIS** utilizando variables lingüísticas para evaluar alternativas de transporte o almacenamiento.
4. **Aplicar metodologías de defuzzificación** (ej. Centro de Área o BNP) para proyectar resultados difusos a valores nítidos comprensibles.
5. **Modelar cualitativamente** los riesgos de disrupción de puertos internacionales utilizando juicios estructurados de expertos.

---

## ⏱️ Estructura del Tiempo (180 minutos en total)

| Bloque | Actividad | Tiempo | Porcentaje |
| :--- | :--- | :---: | :---: |
| **Bloque 1** | Exposición Teórica (Teoría de conjuntos de Zadeh, TFNs, variables lingüísticas, algoritmos Fuzzy) | 90 min | 50% |
| **Bloque 2** | Debate Socrático de Literatura (Zadeh 1965, Tronnebati et al. 2022) | 45 min | 25% |
| **Bloque 3** | Taller Aplicado y Ejercicios (Defuzzificación manual e implementación de Fuzzy TOPSIS en Python) | 45 min | 25% |

---

## 📚 Preparación Previa Requerida (Flipped Classroom)
*Los estudiantes debieron leer con antelación los siguientes recursos:*
1. **Artículo Fundacional:** Zadeh, L. A. (1965). *Fuzzy sets*. Information and Control, 8(3), 338–353. [S06_Zadeh_1965_Fuzzy_sets.pdf](file:///Users/leonardohernandez/Academica/Clase_MULTICRITERIO_DOCTORADO/literatura/articulos/S06_Zadeh_1965_Fuzzy_sets.pdf)
2. **Artículo:** Tronnebati, I., El Yadari, M., \& Jawab, F. (2022). *A Review of Green Supplier Evaluation and Selection Issues Using MCDM, MP and AI Models*. Sustainability, 14(24), 16714. [S06_Tronnebati_El_Yadari_Jawab_2022_Green_Supplier_Evaluation_Selection_Review.pdf](file:///Users/leonardohernandez/Academica/Clase_MULTICRITERIO_DOCTORADO/literatura/articulos/S06_Tronnebati_El_Yadari_Jawab_2022_Green_Supplier_Evaluation_Selection_Review.pdf)
3. **Guía de Lectura Asignada:** 
   * ¿Por qué Zadeh argumenta que la lógica binaria tradicional falla al modelar clases del mundo real (como "rutas seguras" o "tiempos de entrega cortos")?
   * Describe cómo se transforma una escala Likert cualitativa en números difusos triangulares según Tronnebati et al.

---

## 📖 Contenido Temático y Desarrollo de la Sesión

### BLOQUE 1: Exposición Teórica (90 min)
* **Introducción a la Lógica Difusa:**
  * Teoría de funciones de membresía $\mu_A(x)$. Conjuntos nítidos vs. conjuntos difusos.
* **Números Difusos Triangulares (TFNs):**
  * Definición de un TFN $A = (l, m, u)$ (límite inferior, valor medio, límite superior).
  * Aritmética difusa:
    * Suma: $(l_1, m_1, u_1) \oplus (l_2, m_2, u_2) = (l_1+l_2, m_1+m_2, u_1+u_2)$.
    * Multiplicación: $(l_1, m_1, u_1) \otimes (l_2, m_2, u_2) \approx (l_1 l_2, m_1 m_2, u_1 u_2)$ (para números positivos).
* **El Algoritmo Fuzzy TOPSIS (Chen, 2000):**
  * Agregación de opiniones de múltiples expertos directivos.
  * Normalización de la matriz difusa ponderada.
  * Determinación de las soluciones ideales difusas positivas ($A^*$) y negativas ($A^-$).
  * Distancia entre TFNs utilizando el método de distancia de vértice.

---

### BLOQUE 2: Discusión de Literatura - Debate Socrático (45 min)
* **Pregunta Detonante 1:** *En la evaluación de riesgo portuario, un experto califica la estabilidad geopolítica de un puerto como "Muy Inestable". En Fuzzy MCDM, esto se modela con un TFN con amplio traslape. ¿De qué manera la vaguedad matemática aporta mayor rigor científico al paper final de los alumnos en comparación con forzar un juicio numérico nítido?*
* **Pregunta Detonante 2:** *Tronnebati et al. (2022) señalan un incremento drástico de modelos híbridos Fuzzy + Inteligencia Artificial. ¿Qué sinergias existen entre la lógica difusa y los modelos predictivos en logística?*

---

### BLOQUE 3: Taller Práctico - Ejercicios (45 min)

#### 3.1. Ejercicio Guiado (Profesor): Operaciones y Defuzzificación
El profesor guiará la defuzzificación de un TFN $A = (3, 5, 8)$ utilizando el método del centroide:
\begin{equation*}
    x_0 = \frac{l + m + u}{3} = \frac{3 + 5 + 8}{3} = 5.33
\end{equation*}
Y contrastará el resultado con el promedio ponderado clásico.

#### 3.2. Caso Práctico Alumno (Trabajo Autónomo)
El alumno resolverá la evaluación cualitativa de 3 puertos (Houston, Lázaro Cárdenas, Manzanillo) bajo 3 riesgos de cadena de suministro utilizando Fuzzy TOPSIS.
* **Entregable:** Matriz difusa normalizada ponderada, distancias a ideales difusos y ranking de puertos final.

---

## 🎓 Plan de Evidencias (Evaluación)
* **Paso de Control:** Los alumnos están afinando la entrega de **E3 (CP3: Outranking)** que vence en la Sesión 8.
* **Asignación:** Se lanza el **E4 (Caso Práctico 4: Lógica Difusa o Sistemas Grises)**, con entrega programada para la **Sesión 11** (Ponderación **15%**).
