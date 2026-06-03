# Plan de Clase Detallado: Sesión 12
**Materia:** Herramientas Multicriterio para Toma de Decisiones  
**Programa:** Doctorado en Logística y Cadena de Suministro, FIME – UANL  
**Duración:** 3 horas (180 minutos)  
**Profesor:** Dr. Leonardo Gabriel Hernández Landa  
**Tema General:** Toma de Decisiones Multicriterio con Big Data, Machine Learning y XAI  

---

## 🎯 Objetivos de la Sesión
Al finalizar esta duodécima sesión, el estudiante de doctorado será capaz de:
1. **Comprender la convergencia** entre el Machine Learning (ML), el análisis de datos masivos y los métodos MCDM en la logística moderna.
2. **Analizar metodologías de aprendizaje de preferencias** para deducir pesos de criterios a partir de decisiones históricas (enfoque data-driven).
3. **Evaluar el concepto de Inteligencia Artificial Explicable (XAI)** y su rol en la construcción de modelos MCDM transparentes y responsables.
4. **Diseñar un framework básico** para la selección dinámica de rutas o transportistas en tiempo real utilizando flujos de datos masivos.

---

## ⏱️ Estructura del Tiempo (180 minutos en total)

| Bloque | Actividad | Tiempo | Porcentaje |
| :--- | :--- | :---: | :---: |
| **Bloque 1** | Exposición Teórica (Data-driven MCDM, aprendizaje de pesos con ML, taxonomía XAI de Arrieta) | 90 min | 50% |
| **Bloque 2** | Debate Socrático de Literatura (Doumpos \& Figueira 2019, Arrieta et al. 2020) | 45 min | 25% |
| **Bloque 3** | Taller Aplicado y Ejercicios (Resolución de caso de clasificación de transportistas usando Machine Learning y SHAP) | 45 min | 25% |

---

## 📚 Preparación Previa Requerida (Flipped Classroom)
*Los estudiantes debieron leer con antelación los siguientes recursos:*
1. **Artículo:** Arrieta, A. B., et al. (2020). *Explainable Artificial Intelligence (XAI): Concepts, taxonomies, opportunities and challenges toward responsible AI*. Information Fusion, 58, 82–115. [S12_Arrieta_et_al_2020_Explainable_Artificial_Intelligence_XAI.pdf](file:///Users/leonardohernandez/Academica/Clase_MULTICRITERIO_DOCTORADO/literatura/articulos/S12_Arrieta_et_al_2020_Explainable_Artificial_Intelligence_XAI.pdf)
2. **Artículo:** Doumpos, M., \& Figueira, J. R. (2019). *Learning approaches to criteria weights in MCDM: a literature review*. Omega, 84, 176–194. `[Omega / Biblioteca UANL]`
3. **Guía de Lectura Asignada:** 
   * ¿Cómo se clasifican las técnicas XAI según Arrieta et al. (ej. transparencia intrínseca vs. explicabilidad post-hoc)?
   * En el aprendizaje de pesos (Doumpos \& Figueira), ¿cuál es la diferencia entre aprender de forma activa (interactiva) vs. pasiva (datos históricos)?

---

## 📖 Contenido Temático y Desarrollo de la Sesión

### BLOQUE 1: Exposición Teórica (90 min)
* **El Paradigma Data-Driven en Logística:**
  * Uso de grandes volúmenes de datos transaccionales de sistemas TMS y WMS para alimentar modelos MCDM.
* **Aprendizaje de Preferencias y Pesos (Preference Learning):**
  * Modelado de clasificación ordinal mediante algoritmos de ML (ej. Support Vector Machines para clasificación y ordenamiento - RankSVM).
* **Explainable AI (XAI) y Decisiones Responsables:**
  * La necesidad de justificar las decisiones de la IA en comités regulatorios logísticos (ej. desadjudicación de licitaciones).
  * Uso de modelos explicativos post-hoc como SHAP (SHapley Additive exPlanations) y LIME.

---

### BLOQUE 2: Discusión de Literatura - Debate Socrático (45 min)
* **Pregunta Detonante 1:** *Si un algoritmo de Machine Learning aprende de forma autónoma los pesos de los criterios para despachar camiones basándose en las decisiones pasadas de los coordinadores humanos, ¿no corremos el riesgo de automatizar e inmortalizar las ineficiencias y sesgos subjetivos de esos coordinadores? ¿Cómo puede el XAI mitigar este problema?*
* **Pregunta Detonante 2:** *En el contexto de la revisión de Arrieta et al. (2020), ¿qué implicaciones tiene la explicabilidad de la IA para la aceptación de algoritmos de optimización de rutas por parte de los operadores de transporte de carga?*

---

### BLOQUE 3: Taller Práctico - Ejercicios (45 min)

#### 3.1. Ejercicio Guiado (Profesor): Explicabilidad SHAP en Decisiones
El profesor demostrará un script de Python en el que un modelo de bosque aleatorio (Random Forest) clasifica a 100 proveedores logísticos en base a 6 criterios cuali/cuantitativos. El profesor guiará la visualización de explicabilidad utilizando SHAP para mostrar qué criterios (ej. costo, lead time, reputación) determinaron la clasificación de los mejores proveedores.

#### 3.2. Caso Práctico Alumno (Trabajo Autónomo)
El alumno analizará un dataset de selección dinámica de transportistas. Entrenará un árbol de decisión y mapeará las reglas resultantes para compararlas con un modelo AHP determinista tradicional.
* **Entregable:** Árbol de decisión visualizado, reglas de decisión extraídas y comparación crítica de la concordancia de la selección de transportistas.

---

## 🎓 Plan de Evidencias (Evaluación)
* **Avance del PIA:** Los alumnos deben presentar el borrador del artículo conteniendo Abstract, Introducción, Marco Teórico y Metodología para revisión de estructura por parte del profesor.
