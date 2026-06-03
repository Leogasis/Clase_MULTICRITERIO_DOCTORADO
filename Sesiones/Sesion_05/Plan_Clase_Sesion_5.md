# Plan de Clase Detallado: Sesión 5
**Materia:** Herramientas Multicriterio para Toma de Decisiones  
**Programa:** Doctorado en Logística y Cadena de Suministro, FIME – UANL  
**Duración:** 3 horas (180 minutos)  
**Profesor:** Dr. Leonardo Gabriel Hernández Landa  
**Tema General:** Paradigma de Superación (Outranking): Métodos ELECTRE y PROMETHEE  

---

## 🎯 Objetivos de la Sesión
Al finalizar esta quinta sesión, el estudiante de doctorado será capaz de:
1. **Diferenciar la lógica no compensatoria** de la escuela europea frente a la lógica compensatoria clásica (SAW, TOPSIS).
2. **Formular umbrales de preferencia ($p$), indiferencia ($q$) y veto ($v$)** para representar de manera realista los límites de aceptación del decisor.
3. **Calcular flujos de salida ($\Phi^+$), flujos de entrada ($\Phi^-$) y flujos netos ($\Phi$)** en PROMETHEE I y II.
4. **Analizar la visualización del plano GAIA** para interpretar conflictos entre criterios y perfiles de alternativas.
5. **Aplicar relaciones de superación** para resolver un problema de contratación de flota verde sujeto a penalizaciones por huella de carbono.

---

## ⏱️ Estructura del Tiempo (180 minutos en total)

| Bloque | Actividad | Tiempo | Porcentaje |
| :--- | :--- | :---: | :---: |
| **Bloque 1** | Exposición Teórica (Filosofía de Bernard Roy, concordancia/discordancia, ELECTRE y PROMETHEE) | 90 min | 50% |
| **Bloque 2** | Debate Socrático de Literatura (Brans \& Vincke 1985, Wang \& Rangaiah 2025) | 45 min | 25% |
| **Bloque 3** | Taller Aplicado y Ejercicios (Cálculo manual de flujos en PROMETHEE y parametrización de funciones) | 45 min | 25% |

---

## 📚 Preparación Previa Requerida (Flipped Classroom)
*Los estudiantes debieron leer con antelación los siguientes recursos:*
1. **Artículo Clásico:** Brans, J. P., \& Vincke, P. (1985). *A preference ranking organisation method: The PROMETHEE method for MCDM*. Management Science, 31(6), 647–656. [S04_Brans_Vincke_1985_Preference_Ranking_Organisation_Method_PROMETHEE.pdf](file:///Users/leonardohernandez/Academica/Clase_MULTICRITERIO_DOCTORADO/literatura/articulos/S04_Brans_Vincke_1985_Preference_Ranking_Organisation_Method_PROMETHEE.pdf)
2. **Artículo:** Wang, Z., \& Rangaiah, G. P. (2025). *Multi-Criteria Decision-Making: Outranking-Type Methods*. [S04_Wang_Rangaiah_2025_Outranking_Type_Methods_ELECTRE_PROMETHEE.pdf](file:///Users/leonardohernandez/Academica/Clase_MULTICRITERIO_DOCTORADO/literatura/articulos/S04_Wang_Rangaiah_2025_Outranking_Type_Methods_ELECTRE_PROMETHEE.pdf)
3. **Guía de Lectura Asignada:** 
   * ¿Cuál es el significado del veto en ELECTRE y cómo puede aplicarse a una restricción de capacidad o de emisiones en logística?
   * Describe las 6 funciones de preferencia estándar propuestas para PROMETHEE.

---

## 📖 Contenido Temático y Desarrollo de la Sesión

### BLOQUE 1: Exposición Teórica (90 min)
* **La Ayuda a la Decisión No Compensatoria:**
  * Justificación constructivista de Bernard Roy. ¿Por qué rechazar la conmensurabilidad total?
* **Los Métodos ELECTRE (I, II, III):**
  * Conceptos de concordancia (fuerza de la hipótesis de superación) y discordancia (fuerza de la oposición).
  * Construcción de la matriz de concordancia y de discordancia.
  * Definición de niveles de concordancia crítica y veto.
* **El Método PROMETHEE (I y II):**
  * Elicitación de funciones de preferencia de criterios $P_j(a,b)$.
  * Índice de preferencia multicriterio global $\pi(a,b)$.
  * Flujo de salida positivo: $\Phi^+(a) = \frac{1}{m-1} \sum \pi(a,x)$ (mide la fuerza de $a$).
  * Flujo de entrada negativo: $\Phi^-(a) = \frac{1}{m-1} \sum \pi(x,a)$ (mide la debilidad de $a$).
  * Ordenamiento parcial (PROMETHEE I) vs. ordenamiento completo por flujo neto (PROMETHEE II).

---

### BLOQUE 2: Discusión de Literatura - Debate Socrático (45 min)
* **Pregunta Detonante 1:** *PROMETHEE I permite declarar que dos alternativas de proveedores son "incomparables" si una es muy buena en costo pero mala en entregas y la otra es lo opuesto. En una cadena de suministro automotriz (Just-in-Time), ¿cómo debe manejar el analista de decisiones la incomparabilidad? ¿Obliga al decisor a forzar un flujo neto o respeta la incomparabilidad?*
* **Pregunta Detonante 2:** *En el texto de Wang \& Rangaiah (2025), ¿qué ventajas operativas atribuyen los autores a los métodos de outranking frente a los basados en programación lineal multiobjetivo en la era de la logística digital?*

---

### BLOQUE 3: Taller Práctico - Ejercicios (45 min)

#### 3.1. Ejercicio Guiado (Profesor): Parametrización y Flujos en PROMETHEE
El profesor demostrará en vivo cómo programar con `pyDecision` o `scikit-criteria` la comparación de 3 opciones de rutas de transporte ferroviario de contenedores marítimos parametrizando funciones de preferencia lineales y tipo Gaussiano para el costo y las emisiones de $CO_2$.

#### 3.2. Caso Práctico Alumno (Trabajo Autónomo)
El alumno resolverá la selección de un proveedor de fletes intermodales bajo 5 criterios aplicando PROMETHEE I y II, mapeando manualmente las relaciones de dominancia.
* **Entregable:** Matriz de flujo neto $\Phi$, digrafo de PROMETHEE I y ordenamiento final de PROMETHEE II.

---

## 🎓 Plan de Evidencias (Evaluación)
* **Paso de Control:** Los alumnos están trabajando activamente en la resolución del **E2 (Caso Práctico 2: Jerarquización por Distancia)** a entregarse la próxima clase (Sesión 6).
* **Asignación:** Se abre la convocatoria para el **E3 (Caso Práctico 3: Relaciones de Superación ELECTRE vs. PROMETHEE)**, a entregarse en la **Sesión 8** (Ponderación **20%**).
