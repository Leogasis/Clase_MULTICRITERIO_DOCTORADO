# Plan de Clase Detallado: Sesión 8
**Materia:** Herramientas Multicriterio para Toma de Decisiones  
**Programa:** Doctorado en Logística y Cadena de Suministro, FIME – UANL  
**Duración:** 3 horas (180 minutos)  
**Profesor:** Dr. Leonardo Gabriel Hernández Landa  
**Tema General:** MCDM bajo Incertidumbre: Teoría de Sistemas Grises (GRA) y Conjuntos Aproximados (Rough Sets)  

---

## 🎯 Objetivos de la Sesión
Al finalizar esta octava sesión, el estudiante de doctorado será capaz de:
1. **Comprender los principios ontológicos** de la Teoría de Sistemas Grises y su distinción frente a la teoría de probabilidad clásica y la lógica difusa.
2. **Implementar el algoritmo de Grey Relational Analysis (GRA)** paso a paso para medir el grado de correlación entre secuencias de datos.
3. **Analizar los conceptos fundamentales de Rough Set Theory** (conjuntos aproximados): aproximaciones inferiores/superiores y reducción de atributos redundantes.
4. **Modelar y resolver** un problema de clasificación multicriterio de inventarios (ABC) bajo condiciones de escasez de datos operativos históricos.

---

## ⏱️ Estructura del Tiempo (180 minutos en total)

| Bloque | Actividad | Tiempo | Porcentaje |
| :--- | :--- | :---: | :---: |
| **Bloque 1** | Exposición Teórica (Filosofía gris de Deng, coeficientes de relación gris, Rough Sets de Pawlak) | 90 min | 50% |
| **Bloque 2** | Debate Socrático de Literatura (Pawlak 1982, Wei et al. 2011) | 45 min | 25% |
| **Bloque 3** | Taller Aplicado y Ejercicios (Cálculo del Grey Relational Grade a mano/Excel y reducción de atributos) | 45 min | 25% |

---

## 📚 Preparación Previa Requerida (Flipped Classroom)
*Los estudiantes debieron leer con antelación los siguientes recursos:*
1. **Artículo Clásico:** Pawlak, Z. (1982). *Rough sets*. International Journal of Computer \& Information Sciences, 11(5), 341–356. [S07_Pawlak_1982_Rough_sets.pdf](file:///Users/leonardohernandez/Academica/Clase_MULTICRITERIO_DOCTORADO/literatura/articulos/S07_Pawlak_1982_Rough_sets.pdf)
2. **Artículo:** Wei, G. W., Wang, H. J., Lin, R., \& Zhao, X. F. (2011). *Grey relational analysis method for intuitionistic fuzzy multiple attribute decision making with preference information on alternatives*. International Journal of Computational Intelligence Systems, 4(2), 164–173. [S07_Wei_Wang_Lin_Zhao_2011_GRA_Intuitionistic_Fuzzy_MADM_Preference_Info.pdf](file:///Users/leonardohernandez/Academica/Clase_MULTICRITERIO_DOCTORADO/literatura/articulos/S07_Wei_Wang_Lin_Zhao_2011_GRA_Intuitionistic_Fuzzy_MADM_Preference_Info.pdf)
3. **Guía de Lectura Asignada:** 
   * ¿En qué se diferencia conceptualmente la "información gris" (Deng) de la "información difusa" (Zadeh)?
   * ¿Cómo define Pawlak los límites inferior y superior de una aproximación en una tabla de decisión?

---

## 📖 Contenido Temático y Desarrollo de la Sesión

### BLOQUE 1: Exposición Teórica (90 min)
* **La Teoría de Sistemas Grises:**
  * Concepto de información negra (desconocida), blanca (conocida) y gris (parcialmente conocida).
  * Algoritmo de Grey Relational Analysis (GRA):
    * Generación de secuencias de referencia y secuencias comparadas.
    * Normalización gris (Max, Min o valor meta).
    * Cálculo de la matriz de diferencias $\Delta_{0i}$.
    * Coeficiente de relación gris $\gamma(x_0(k), x_i(k)) = \frac{\Delta_{\min} + \zeta \Delta_{\max}}{\Delta_{0i}(k) + \zeta \Delta_{\max}}$ (donde $\zeta \in (0, 1]$, típicamente 0.5).
    * Grado de relación gris (GRG): $\Gamma(x_0, x_i) = \sum w_k \gamma_i(k)$.
* **La Teoría de Conjuntos Aproximados (Pawlak):**
  * La relación de indiscernibilidad.
  * Espacios de aproximación.
  * Clasificación multicriterio y tablas de decisión. Reducción de criterios sin pérdida de información de clasificación.

---

### BLOQUE 2: Discusión de Literatura - Debate Socrático (45 min)
* **Pregunta Detonante 1:** *En logística de inventarios, la clasificación ABC tradicional solo considera el valor del consumo anual (criterio único). Si incorporamos lead time y criticidad, ¿cómo ayuda la Rough Set Theory a identificar si la variable "criticidad" es matemáticamente redundante o si aporta un valor único a la clasificación?*
* **Pregunta Detonante 2:** *En el trabajo de Wei et al. (2011), ¿cómo se integran los números difusos intuicionistas con la lógica del análisis relacional gris?*

---

### BLOQUE 3: Taller Práctico - Ejercicios (45 min)

#### 3.1. Ejercicio Guiado (Profesor): Implementación de GRA
El profesor guiará paso a paso la resolución de un problema de clasificación de 4 proveedores logísticos de transporte terrestre utilizando GRA con 3 criterios en Excel, deduciendo el orden de prioridad y graficando el grado de relación gris.

#### 3.2. Caso Práctico Alumno (Trabajo Autónomo)
El alumno resolverá la clasificación multicriterio de 8 SKUs de inventario (costo unitario, demanda anual, variabilidad de entrega) utilizando GRA.
* **Entregable:** Matriz de diferencias, coeficientes de relación gris calculados y el ranking final de productos.

---

## 🎓 Plan de Evidencias (Evaluación)
* **Entrega:** Se recolecta el **E3 (Caso Práctico 3: Relaciones de Superación ELECTRE vs. PROMETHEE)** (20%).
* **Hito Doctoral:** A partir de esta sesión se da inicio formal al **Producto Integrador de Aprendizaje (PIA)**, donde el alumno debe aplicar las metodologías vistas sobre su conjunto de datos reales del sector industrial para escribir el artículo científico.
