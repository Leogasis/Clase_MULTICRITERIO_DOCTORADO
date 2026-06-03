# Plan de Clase Detallado: Sesión 2
**Materia:** Herramientas Multicriterio para Toma de Decisiones  
**Programa:** Doctorado en Logística y Cadena de Suministro, FIME – UANL  
**Duración:** 3 horas (180 minutos)  
**Profesor:** Dr. Leonardo Gabriel Hernández Landa  
**Tema General:** Ponderación Subjetiva de Criterios: AHP (Saaty) y Best-Worst Method (BWM)  

---

## 🎯 Objetivos de la Sesión
Al finalizar esta segunda sesión, el estudiante de doctorado será capaz de:
1. **Diferenciar y contrastar** los fundamentos matemáticos y axiomáticos del Proceso de Jerarquía Analítica (AHP) frente al Método del Mejor-Peor (BWM).
2. **Construir matrices de comparación pareada** consistentes y resolver vectores de prioridad utilizando métodos de autovalores o aproximaciones geométricas.
3. **Calcular e interpretar** el Índice de Consistencia ($CI$) y la Razón de Consistencia ($CR$) en AHP.
4. **Formular y resolver el modelo de optimización lineal** del BWM para calcular pesos óptimos con menor número de comparaciones pareadas.
5. **Aplicar estas técnicas** en un problema real de selección estratégica de socios logísticos 3PL.

---

## ⏱️ Estructura del Tiempo (180 minutos en total)

| Bloque | Actividad | Tiempo | Porcentaje |
| :--- | :--- | :---: | :---: |
| **Bloque 1** | Exposición Teórica (Axiomas de Saaty, AHP, debate de Rank Reversal y teoría de BWM) | 90 min | 50% |
| **Bloque 2** | Debate Socrático de Literatura (Rezaei 2015, Dyer 1990) | 45 min | 25% |
| **Bloque 3** | Taller Aplicado y Ejercicios (Cálculo de AHP a mano/Excel y BWM en Python) | 45 min | 25% |

---

## 📚 Preparación Previa Requerida (Flipped Classroom)
*Los estudiantes debieron leer con antelación los siguientes recursos:*
1. **Artículo:** Rezaei, J. (2015). *Best-worst multi-criteria decision-making method*. Omega, 53, 49–57. [S03_Rezaei_2015_Best_worst_multi_criteria_decision_making_method.pdf](file:///Users/leonardohernandez/Academica/Clase_MULTICRITERIO_DOCTORADO/literatura/articulos/S03_Rezaei_2015_Best_worst_multi_criteria_decision_making_method.pdf)
2. **Capítulo de Libro:** Saaty, T. L. (1980). *The Analytic Hierarchy Process* (capítulos seleccionados sobre axiomas y escalas). McGraw-Hill.
3. **Guía de Lectura Asignada:** 
   * ¿Cuál es la mayor crítica matemática que Dyer (1990) le hace al AHP clásico?
   * ¿Por qué el Best-Worst Method (BWM) requiere un menor número de comparaciones en comparación con el AHP clásico ($2n - 3$ frente a $n(n-1)/2$)?

---

## 📖 Contenido Temático y Desarrollo de la Sesión

### BLOQUE 1: Exposición Teórica (90 min)
* **Axiomas del AHP de Saaty:**
  * Reciprocidad ($a_{ji} = 1/a_{ij}$), Homogeneidad (los elementos comparados deben pertenecer a la misma escala), Dependencia (jerarquía estructural) y Expectativas.
* **El Debate sobre Rank Reversal (Inversión de Rangos):**
  * Análisis de la polémica de Dyer vs. Saaty. ¿Es admisible que la adición de una alternativa irrelevante cambie el orden de preferencia de las alternativas originales?
* **El Método del Mejor-Peor (BWM):**
  * Pasos del algoritmo: Selección de los criterios Best ($C_B$) y Worst ($C_W$).
  * Comparaciones Best-to-Others ($A_{B}$) y Others-to-Worst ($A_{W}$).
  * Formulación del modelo matemático minimax para resolver los pesos óptimos $w^*$:
    $$\min \xi$$
    $$\text{s.t. } |w_B - a_{Bj} w_j| \le \xi, \quad |w_j - a_{jW} w_W| \le \xi, \quad \sum_j w_j = 1, \quad w_j \ge 0$$

---

### BLOQUE 2: Discusión de Literatura - Debate Socrático (45 min)
* **Pregunta Detonante 1:** *Dyer (1990) argumenta que la escala 1-9 de Saaty es arbitraria y carece de base axiomática operativa. ¿Consideras que esto invalida el AHP en el diseño de redes logísticas complejas, o su usabilidad práctica justifica la falta de rigor?*
* **Pregunta Detonante 2:** *En la selección de un proveedor 3PL, la consistencia de los juicios del comité directivo suele ser baja debido a visiones contrapuestas (Ventas vs. Finanzas). ¿Cómo ayuda BWM a mitigar esta inconsistencia en comparación con AHP?*

---

### BLOQUE 3: Taller Práctico - Ejercicios (45 min)

#### 3.1. Ejercicio Guiado (Profesor): Cálculo de Consistencia en AHP
El profesor guiará en el pizarrón el cálculo de la consistencia de una matriz de comparaciones de $3 \times 3$ de criterios logísticos (Costo, Tiempo de entrega, Flexibilidad):
1. Normalización por columnas y obtención del vector de prioridades (pesos aproximados).
2. Cálculo de $\lambda_{\max}$ y del Índice de Consistencia ($CI = \frac{\lambda_{\max} - n}{n-1}$).
3. Comparación con el Índice Aleatorio ($RI$) para obtener la Razón de Consistencia ($CR = CI/RI$). Validar si $CR < 0.10$.

#### 3.2. Caso Práctico Alumno (Trabajo Autónomo)
El estudiante deberá resolver la selección de ponderaciones subjetivas para un problema de selección de transportista de carga terrestre consolidada (LTL) con 4 criterios: Costo ($C_1$), Confiabilidad ($C_2$), Capacidad de Rastreo ($C_3$), y Sustentabilidad ($C_4$).
* **Entregable:** Construir las matrices AHP de comparaciones, verificar su nivel de consistencia y proponer los pesos finales.

---

## 🎓 Plan de Evidencias (Evaluación)
Esta sesión aporta directamente al **E1 (Caso Práctico 1: Ponderación de Criterios)**, el cual será entregado en la **Sesión 4** y pondera un **15%** de la calificación final del curso.
