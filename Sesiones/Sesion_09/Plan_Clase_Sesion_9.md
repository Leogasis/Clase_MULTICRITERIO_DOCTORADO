# Plan de Clase Detallado: Sesión 9
**Materia:** Herramientas Multicriterio para Toma de Decisiones  
**Programa:** Doctorado en Logística y Cadena de Suministro, FIME – UANL  
**Duración:** 3 horas (180 minutos)  
**Profesor:** Dr. Leonardo Gabriel Hernández Landa  
**Tema General:** Métodos de Nueva Generación: MARCOS, EDAS, CODAS y CoCoSo  

---

## 🎯 Objetivos de la Sesión
Al finalizar esta novena sesión, el estudiante de doctorado será capaz de:
1. **Analizar la lógica evolutiva** de los métodos modernos que combinan distancias y outranking para mitigar las debilidades de los métodos clásicos.
2. **Implementar el algoritmo EDAS** calculando las distancias positivas y negativas al promedio (PDA y NDA).
3. **Formular el modelo de evaluación de MARCOS** basándose en la relación de compromiso frente a alternativas ideales y anti-ideales.
4. **Programar y contrastar** el método CoCoSo (Combined Compromise Solution) utilizando diferentes estrategias de agregación de compromiso.
5. **Aplicar estos métodos** en la selección tecnológica de sistemas de automatización (WMS) para bodegas de e-commerce.

---

## ⏱️ Estructura del Tiempo (180 minutos en total)

| Bloque | Actividad | Tiempo | Porcentaje |
| :--- | :--- | :---: | :---: |
| **Bloque 1** | Exposición Teórica (Árbol genealógico de métodos modernos, formulación de EDAS, MARCOS y CoCoSo) | 90 min | 50% |
| **Bloque 2** | Debate Socrático de Literatura (Keshavarz Ghorabaee et al. 2015, Wang et al. 2022) | 45 min | 25% |
| **Bloque 3** | Taller Aplicado y Ejercicios (Resolución de EDAS en Excel/Python y análisis de consistencia de rankings) | 45 min | 25% |

---

## 📚 Preparación Previa Requerida (Flipped Classroom)
*Los estudiantes debieron leer con antelación los siguientes recursos:*
1. **Artículo:** Keshavarz Ghorabaee, M., et al. (2015). *Multi-criteria inventory classification using a new method of evaluation based on distance from average solution (EDAS)*. Informatica, 26(3), 435–451. [S09_Keshavarz_Ghorabaee_et_al_2015_EDAS_Evaluation_based_on_Distance_from_Average_Solution.pdf](file:///Users/leonardohernandez/Academica/Clase_MULTICRITERIO_DOCTORADO/literatura/articulos/S09_Keshavarz_Ghorabaee_et_al_2015_EDAS_Evaluation_based_on_Distance_from_Average_Solution.pdf)
2. **Artículo:** Wang, C.-N., Nguyen, T. T. T., Dang, T.-T., \& Nguyen, N.-A.-T. (2022). *A Hybrid OPA and Fuzzy MARCOS Methodology for Sustainable Supplier Selection with Technology 4.0 Evaluation*. Processes, 10(11), 2351. [S09_Wang_Nguyen_Dang_Nguyen_2022_OPA_Fuzzy_MARCOS_Sustainable_Supplier_I40.pdf](file:///Users/leonardohernandez/Academica/Clase_MULTICRITERIO_DOCTORADO/literatura/articulos/S09_Wang_Nguyen_Dang_Nguyen_2022_OPA_Fuzzy_MARCOS_Sustainable_Supplier_I40.pdf)
3. **Guía de Lectura Asignada:** 
   * ¿Por qué el método EDAS utiliza la solución promedio en lugar de los extremos ideal/anti-ideal (como TOPSIS)? ¿Qué ventajas tiene esto cuando hay outliers en los datos?
   * Explica los tres índices de agregación utilizados por CoCoSo para combinar la suma ponderada y el producto ponderado.

---

## 📖 Contenido Temático y Desarrollo de la Sesión

### BLOQUE 1: Exposición Teórica (90 min)
* **La Evolución de los Métodos Multicriterio:**
  * Métodos de nueva generación: robustez y reducción de la inversión de rangos.
* **El Algoritmo EDAS:**
  * Solución promedio: $AV_j = \sum_{i=1}^m x_{ij} / m$.
  * Distancia Positiva del Promedio (PDA) y Distancia Negativa del Promedio (NDA) para criterios de beneficio y costo.
  * Suma ponderada de distancias: $SP_i = \sum w_j PDA_{ij}$, $SN_i = \sum w_j NDA_{ij}$.
  * Puntuación de valoración final: $AS_i = \frac{1}{2} (NSP_i + NSN_i)$.
* **El Algoritmo MARCOS:**
  * Generación de la matriz extendida con alternativas ideal (AI) y anti-ideal (AAI).
  * Relación de utilidad de alternativas respecto a ideales.
  * Función de utilidad de compromiso final.

---

### BLOQUE 2: Discusión de Literatura - Debate Socrático (45 min)
* **Pregunta Detonante 1:** *En el artículo de Wang et al. (2022), los autores proponen un enfoque híbrido OPA-Fuzzy MARCOS. ¿Por qué el uso de la lógica difusa complementa al método MARCOS en la evaluación de la madurez tecnológica industrial (Tecnología 4.0)?*
* **Pregunta Detonante 2:** *EDAS fue propuesto originalmente para clasificación de inventarios. ¿Por qué es un método adecuado para clasificar miles de productos en comparación con métodos que requieren comparaciones pareadas como AHP?*

---

### BLOQUE 3: Taller Práctico - Ejercicios (45 min)

#### 3.1. Ejercicio Guiado (Profesor): Implementación de EDAS vs. TOPSIS
El profesor modelará un problema de selección de un software WMS (Warehouse Management System) comparando 4 alternativas bajo 5 criterios operativos. Demostrará en Python cómo el método EDAS amortigua el efecto de valores extremos (outliers) en comparación con TOPSIS.

#### 3.2. Caso Práctico Alumno (Trabajo Autónomo)
El alumno resolverá la selección de un proveedor de montacargas eléctricos y autónomos (AGVs) para un CEDIS utilizando el método CoCoSo.
* **Entregable:** Matriz de decisión normalizada, cálculo de índices agregados y justificación del proveedor elegido.

---

## 🎓 Plan de Evidencias (Evaluación)
* **Paso de Control:** Los alumnos están desarrollando el **E4 (Caso Práctico 4: Incertidumbre difusa/gris)** que se entrega en la Sesión 11.
* **Avance del PIA:** Los alumnos deben presentar el borrador inicial de la introducción y la matriz de datos de su artículo de investigación para recibir feedback.
