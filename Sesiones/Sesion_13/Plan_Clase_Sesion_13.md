# Plan de Clase Detallado: Sesión 13
**Materia:** Herramientas Multicriterio para Toma de Decisiones  
**Programa:** Doctorado en Logística y Cadena de Suministro, FIME – UANL  
**Duración:** 3 horas (180 minutos)  
**Profesor:** Dr. Leonardo Gabriel Hernández Landa  
**Tema General:** Sostenibilidad, Logística Verde y Criterios ESG en Toma de Decisiones  

---

## 🎯 Objetivos de la Sesión
Al finalizar esta decimotercera sesión, el estudiante de doctorado será capaz de:
1. **Modelar e integrar** las dimensiones de la sostenibilidad (*Triple Bottom Line*: económico, ambiental, social) en matrices de decisión complejas.
2. **Definir y normalizar** criterios ESG (Environmental, Social, Governance) y métricas de Análisis de Ciclo de Vida (LCA) en la logística.
3. **Manejar los conflictos inherentes** entre costos logísticos operativos tradicionales e impacto social/huella ecológica.
4. **Diseñar marcos de evaluación multicriterio** aplicados a la logística inversa, la economía circular y la electrificación de flotas urbanas.

---

## ⏱️ Estructura del Tiempo (180 minutos en total)

| Bloque | Actividad | Tiempo | Porcentaje |
| :--- | :--- | :---: | :---: |
| **Bloque 1** | Exposición Teórica (Triple Bottom Line en logística, criterios ESG en cadena de suministro, LCA e integración en MCDM) | 90 min | 50% |
| **Bloque 2** | Debate Socrático de Literatura (Banaeian et al. 2017, Zhou \& Xu 2018) | 45 min | 25% |
| **Bloque 3** | Taller Aplicado y Ejercicios (Formulación de marco MCDM para economía circular en un caso de logística inversa) | 45 min | 25% |

---

## 📚 Preparación Previa Requerida (Flipped Classroom)
*Los estudiantes debieron leer con antelación los siguientes recursos:*
1. **Artículo:** Banaeian, N., et al. (2017). *Green Supplier Evaluation and Selection in Apparel Manufacturing Using a Fuzzy Multi-Criteria Decision-Making Approach*. Sustainability, 9(4), 650. [S13_Green_Supplier_Evaluation_Selection_Apparel_Fuzzy_MCDM_2017.pdf](file:///Users/leonardohernandez/Academica/Clase_MULTICRITERIO_DOCTORADO/literatura/articulos/S13_Green_Supplier_Evaluation_Selection_Apparel_Fuzzy_MCDM_2017.pdf)
2. **Artículo:** Zhou, X., \& Xu, Z. (2018). *An Integrated Sustainable Supplier Selection Approach Based on Hybrid Information Aggregation*. Sustainability, 10(7), 2543. [S13_Zhou_Xu_2018_Integrated_Sustainable_Supplier_Selection_Hybrid_Info_Aggregation.pdf](file:///Users/leonardohernandez/Academica/Clase_MULTICRITERIO_DOCTORADO/literatura/articulos/S13_Zhou_Xu_2018_Integrated_Sustainable_Supplier_Selection_Hybrid_Info_Aggregation.pdf)
3. **Guía de Lectura Asignada:** 
   * ¿Cómo operacionalizan los autores el concepto de la sustentabilidad en la evaluación de proveedores verdes? ¿Qué criterios son más difíciles de cuantificar empíricamente?
   * ¿De qué manera el enfoque de "agregación de información híbrida" de Zhou \& Xu (2018) ayuda a representar datos inciertos cualitativos y cuantitativos simultáneamente?

---

## 📖 Contenido Temático y Desarrollo de la Sesión

### BLOQUE 1: Exposición Teórica (90 min)
* **La Sostenibilidad en la Cadena de Suministro (SSCM):**
  * Tendencias globales en regulación ambiental e impuestos al carbono en el transporte.
* **Criterios ESG y su Operacionalización:**
  * **Ambiental:** Huella de carbono ($gCO_2e/ton-km$), consumo de agua, reciclabilidad de materiales, generación de residuos peligrosos.
  * **Social:** Derechos humanos de conductores, equidad laboral, certificaciones éticas (ISO 26000), seguridad vial (tasa de accidentes).
  * **Gobernanza:** Políticas anticorrupción de proveedores 3PL, transparencia financiera.
* **Integración del Análisis de Ciclo de Vida (LCA) en MCDM:**
  * Modelado del impacto de la cuna a la tumba del producto como criterios en conflicto.

---

### BLOQUE 2: Discusión de Literatura - Debate Socrático (45 min)
* **Pregunta Detonante 1:** *En el estudio de Banaeian et al. (2017), los autores aplican Fuzzy MCDM a la industria de manufactura textil. ¿Cuáles son los mayores retos de medir la sustentabilidad social del proveedor en países en desarrollo? ¿Cómo mitiga la lógica difusa la falta de auditorías formales?*
* **Pregunta Detonante 2:** *En el diseño de una red de logística inversa para baterías de vehículos eléctricos, ¿qué criterios son de carácter crítico (vetos obligatorios de outranking) y cuáles son compensables?*

---

### BLOQUE 3: Taller Práctico - Ejercicios (45 min)

#### 3.1. Ejercicio Guiado (Profesor): Diseño de Marco MCDM ESG
El profesor guiará un ejercicio práctico para formular la matriz de decisión de un problema de logística inversa (recolección y reciclaje de empaques plásticos). Se modelarán 4 alternativas de red de recolección evaluando Costo logístico, Huella de carbono del transporte y Tasa de inclusión social de recolectores locales.

#### 3.2. Caso Práctico Alumno (Trabajo Autónomo)
El alumno formulará y resolverá en Python un modelo MCDM para evaluar la compra de camiones de reparto urbano (eléctricos vs. híbridos vs. diésel estándar).
* **Entregable:** Matriz de decisión modelada con criterios ESG y justificación analítica de la compra de flota óptima de bajas emisiones.

---

## 🎓 Plan de Evidencias (Evaluación)
* **Hito de Avance PIA:** Los alumnos deben presentar el borrador final del artículo completo en formato Word o LaTeX listo para el proceso de revisión por pares interna que se llevará a cabo en la Sesión 14.
