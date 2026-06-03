# Plan de Clase Detallado: Sesión 11
**Materia:** Herramientas Multicriterio para Toma de Decisiones  
**Programa:** Doctorado en Logística y Cadena de Suministro, FIME – UANL  
**Duración:** 3 horas (180 minutos)  
**Profesor:** Dr. Leonardo Gabriel Hernández Landa  
**Tema General:** Modelos Híbridos: Integración de MCDM con Optimización (NSGA-II)  

---

## 🎯 Objetivos de la Sesión
Al finalizar esta undécima sesión, el estudiante de doctorado será capaz de:
1. **Comprender la diferencia y sinergia** entre la generación de soluciones (MODM/Optimización) y la selección de alternativas (MADM/MCDM).
2. **Formular modelos matemáticos multiobjetivo** aplicados a redes de distribución logística.
3. **Analizar los conceptos fundamentales de los algoritmos evolutivos**, específicamente el algoritmo NSGA-II (ordenamiento no dominado, distancia de apiñamiento).
4. **Hibridar modelos:** Usar un algoritmo MODM para generar la frontera de Pareto y aplicar un método MADM (ej. TOPSIS) para seleccionar la mejor solución de compromiso de la frontera.

---

## ⏱️ Estructura del Tiempo (180 minutos en total)

| Bloque | Actividad | Tiempo | Porcentaje |
| :--- | :--- | :---: | :---: |
| **Bloque 1** | Exposición Teórica (MODM, conceptos de optimalidad de Pareto, algoritmo genético NSGA-II, frameworks híbridos) | 90 min | 50% |
| **Bloque 2** | Debate Socrático de Literatura (Deb et al. 2002, Awasthi et al. 2012) | 45 min | 25% |
| **Bloque 3** | Taller Aplicado y Ejercicios (Resolución de un problema de transporte bi-objetivo en Python con Pyomo o DEAP) | 45 min | 25% |

---

## 📚 Preparación Previa Requerida (Flipped Classroom)
*Los estudiantes debieron leer con antelación los siguientes recursos:*
1. **Artículo Clásico:** Deb, K., et al. (2002). *A fast and elitist multiobjective genetic algorithm: NSGA-II*. IEEE Transactions on Evolutionary Computation, 6(2), 182–197. [S11_Deb_et_al_2002_A_fast_and_elitist_multiobjective_genetic_algorithm_NSGA_II.pdf](file:///Users/leonardohernandez/Academica/Clase_MULTICRITERIO_DOCTORADO/literatura/articulos/S11_Deb_et_al_2002_A_fast_and_elitist_multiobjective_genetic_algorithm_NSGA_II.pdf)
2. **Artículo:** Awasthi, A., Chauhan, S. S., \& Goyal, S. K. (2012). *A hybrid approach integrating Affinity Diagram, AHP and fuzzy TOPSIS for sustainable city logistics planning*. Applied Mathematical Modelling, 36(2), 573–584. [S11_AHP_Fuzzy_TOPSIS_Sustainable_City_Logistics_Planning_2012.pdf](file:///Users/leonardohernandez/Academica/Clase_MULTICRITERIO_DOCTORADO/literatura/articulos/S11_AHP_Fuzzy_TOPSIS_Sustainable_City_Logistics_Planning_2012.pdf)
3. **Guía de Lectura Asignada:** 
   * ¿Cuál es el rol de la distancia de apiñamiento (crowding distance) en el algoritmo NSGA-II para garantizar la diversidad en la frontera de Pareto?
   * ¿Cómo justifican Awasthi et al. (2012) la hibridación de AHP y Fuzzy TOPSIS en lugar de usar un único método en la planeación logística sustentable?

---

## 📖 Contenido Temático y Desarrollo de la Sesión

### BLOQUE 1: Exposición Teórica (90 min)
* **Optimización Multiobjetivo (MODM):**
  * Conceptos de dominancia de Pareto. Soluciones eficientes e ineficientes.
* **El Algoritmo NSGA-II (Deb et al. 2002):**
  * Clasificación rápida no dominada (Fast Non-Dominated Sort).
  * Distancia de apiñamiento (Crowding Distance) para dispersión de soluciones.
  * Preservación de elitismo y operadores genéticos.
* **Integración MODM + MADM:**
  * El problema de seleccionar una única solución física para implementar a partir de las cientos de soluciones en la frontera de Pareto.
  * Hibridación: La frontera de Pareto se convierte en la matriz de decisión de entrada ($X$), y se aplica TOPSIS/VIKOR para encontrar la solución que mejor balancee las prioridades de la junta directiva.

---

### BLOQUE 2: Discusión de Literatura - Debate Socrático (45 min)
* **Pregunta Detonante 1:** *Kalyanmoy Deb introdujo NSGA-II en 2002, convirtiéndose en el estándar de oro de la optimización multiobjetivo. En la planeación de rutas de transporte verde, ¿por qué un algoritmo evolutivo tiene ventajas en comparación con los métodos clásicos de suma ponderada de objetivos?*
* **Pregunta Detonante 2:** *En el artículo de Awasthi et al. (2012), los autores mapean la planeación de la logística urbana sostenible. ¿Por qué las decisiones de políticas públicas urbanas requieren obligatoriamente hibridaciones de estructuración cualitativa y evaluación cuantitativa?*

---

### BLOQUE 3: Taller Práctico - Ejercicios (45 min)

#### 3.1. Ejercicio Guiado (Profesor): Hibridación MODM + MADM
El profesor mostrará un script de Python que genera 50 soluciones óptimas de Pareto para un problema de asignación de carga de transporte terrestre bi-objetivo (Costo vs. Emisiones). El profesor guiará a la clase para filtrar la frontera utilizando TOPSIS en Python para seleccionar la solución recomendada final.

#### 3.2. Caso Práctico Alumno (Trabajo Autónomo)
El alumno resolverá un problema simplificado de diseño de red de distribución con 2 objetivos (maximizar el nivel de servicio y minimizar el costo fijo) y seleccionará la solución de compromiso mediante el método SAW y TOPSIS.
* **Entregable:** Gráfica de la frontera de Pareto, pesos asignados y justificación del punto óptimo elegido.

---

## 🎓 Plan de Evidencias (Evaluación)
* **Entrega:** Se recolecta el **E4 (Caso Práctico 4: Incertidumbre y Lógica Difusa o Sistemas Grises)** (15%).
* **Avance del PIA:** Los alumnos deben mostrar el primer borrador completo de los resultados numéricos de su artículo científico.
