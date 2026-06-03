# Plan de Clase Detallado: Sesión 14
**Materia:** Herramientas Multicriterio para Toma de Decisiones  
**Programa:** Doctorado en Logística y Cadena de Suministro, FIME – UANL  
**Duración:** 3 horas (180 minutos)  
**Profesor:** Dr. Leonardo Gabriel Hernández Landa  
**Tema General:** Validación, Robustez, Replicabilidad y Revisión por Pares en MCDM  

---

## 🎯 Objetivos de la Sesión
Al finalizar esta decimocuarta sesión, el estudiante de doctorado será capaz de:
1. **Evaluar de manera crítica** la calidad metodológica de los estudios de toma de decisiones multicriterio publicados en la literatura científica.
2. **Diseñar e implementar análisis de sensibilidad avanzados** utilizando Simulación Monte Carlo y el método global de Saltelli para perturbar pesos y evaluar la robustez del ranking.
3. **Calcular la concordancia de rankings** entre diferentes métodos empleando coeficientes de correlación y concordancia (Spearman, Kendall $W$).
4. **Ejercer el rol de revisor académico (referee)** realizando una revisión por pares constructiva y rigurosa del borrador de un compañero de clase.

---

## ⏱️ Estructura del Tiempo (180 minutos en total)

| Bloque | Actividad | Tiempo | Porcentaje |
| :--- | :--- | :---: | :---: |
| **Bloque 1** | Exposición Teórica (Errores comunes en análisis de sensibilidad, checklist de Saltelli, validación cruzada de rankings, buenas prácticas de open code) | 60 min | 33% |
| **Bloque 2** | Taller de Simulación Monte Carlo (Implementación del código de análisis de sensibilidad global en Python) | 60 min | 33% |
| **Bloque 3** | Taller de Revisión por Pares (Discusión en parejas y retroalimentación del borrador del artículo del PIA) | 60 min | 34% |

---

## 📚 Preparación Previa Requerida (Flipped Classroom)
*Los estudiantes debieron leer con antelación los siguientes recursos:*
1. **Artículo Metodológico:** Saltelli, A., et al. (2019). *Why so many published sensitivity analyses are false: A systematic review of sensitivity analysis practices*. Environmental Modelling \& Software, 114, 29–39. [S14_Saltelli_et_al_2019_Why_so_many_published_sensitivity_analyses_are_false.pdf](file:///Users/leonardohernandez/Academica/Clase_MULTICRITERIO_DOCTORADO/literatura/articulos/S14_Saltelli_et_al_2019_Why_so_many_published_sensitivity_analyses_are_false.pdf)
2. **Artículo:** Cinelli, M., et al. (2022). *Proper and improper uses of MCDA methods in energy systems analysis*. Decision Support Systems, 163, 113848. [S14_Cinelli_et_al_2022_Proper_and_improper_uses_of_MCDA_methods_in_energy_systems_analysis.pdf](file:///Users/leonardohernandez/Academica/Clase_MULTICRITERIO_DOCTORADO/literatura/articulos/S14_Cinelli_et_al_2022_Proper_and_improper_uses_of_MCDA_methods_in_energy_systems_analysis.pdf)
3. **Guía de Lectura Asignada:** 
   * ¿Cuáles son las tres falacias más comunes que Saltelli et al. detectan en los análisis de sensibilidad de la literatura actual (ej. variación OAT - *One At a Time*)?
   * Elabora una lista de 5 errores metodológicos críticos detallados por Cinelli et al. que invalidarían la aceptación de un artículo sobre MCDM en logística.

---

## 📖 Contenido Temático y Desarrollo de la Sesión

### BLOQUE 1: Exposición Teórica (60 min)
* **El Análisis de Sensibilidad Tradicional vs. Global:**
  * Limitaciones del análisis *One-At-a-Time* (variar un peso a la vez manteniendo los otros fijos).
  * Perturbación simultánea de los pesos de la matriz respetando la restricción de suma unitaria: $w_j' = w_j + \epsilon_j$ sujeto a $\sum w_j' = 1$.
* **Validación de Métodos:**
  * Validación cruzada: aplicar 3 métodos distintos (ej. TOPSIS, VIKOR, EDAS) a los mismos datos y medir la robustez de los rankings resultantes.
* **El Proceso de Revisión por Pares (Peer Review):**
  * Rúbricas de calidad en revistas Elsevier, Springer y Taylor \& Francis. Estructura de un reporte de arbitraje académico formal.

---

### BLOQUE 2: Taller Práctico - Simulación Monte Carlo en Python (60 min)
El profesor compartirá una plantilla de Jupyter Notebook. Los estudiantes escribirán un script en Python para:
1. Generar 1,000 vectores de pesos aleatorios perturbando un vector de pesos base mediante una distribución de Dirichlet.
2. Resolver el algoritmo TOPSIS para cada vector aleatorio.
3. Calcular el porcentaje de simulaciones en las que la alternativa líder del caso de estudio cambia (medida de robustez).
4. Calcular el coeficiente de correlación de Spearman promedio de la simulación.

---

### BLOQUE 3: Taller de Revisión por Pares en Vivo (60 min)
* **Dinámica en Vivo:** Los estudiantes intercambian sus borradores completos del manuscrito del **PIA**.
* Cada estudiante actúa como un revisor anónimo (*referee*). Utilizando una lista de cotejo basada en Cinelli et al. (2022) y las guías de autor de revistas Q1 de logística, redacta un reporte de revisión crítica formal sugiriendo al menos 3 mejoras metodológicas cruciales antes de la entrega final.

---

## 🎓 Plan de Evidencias (Evaluación)
* **Entregable Indirecto:** El reporte de revisión por pares redactado por el alumno es evaluado y ponderado como parte de su participación activa en el seminario de investigación.
* **Hito de Ajuste:** El alumno tiene una semana para integrar los cambios del revisor en su borrador final antes de la defensa del PIA en la Sesión 15.
