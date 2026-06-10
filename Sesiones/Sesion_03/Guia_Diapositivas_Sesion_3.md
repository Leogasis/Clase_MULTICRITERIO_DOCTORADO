# Guía de Apoyo al Docente: Diapositivas de la Sesión 3
**Materia:** Herramientas Multicriterio para Toma de Decisiones  
**Tema:** Ponderación Objetiva: Entropía de Shannon y Método CRITIC  
**Programa:** Doctorado en Logística y Cadena de Suministro, FIME – UANL  

Este documento proporciona una guía diapositiva por diapositiva para el profesor, detallando los puntos clave a explicar, las notas pedagógicas y cómo conectar la matemática compleja con conceptos comprensibles para estudiantes de posgrado con perfiles multidisciplinarios.

---

## 📋 Índice de Diapositivas

### Diapositiva 1: Portada
* **Contenido:** Título del curso, tema de la sesión, datos del profesor e institución.
* **Propósito:** Encuadrar la sesión y establecer el ambiente académico formal del Doctorado.

---

### Diapositiva 2: Objetivos de la Sesión
* **Contenido:** Logros de aprendizaje esperados (analizar la filosofía de la ponderación objetiva, implementar la Entropía de Shannon, calcular pesos con CRITIC y contrastar perfiles de peso).
* **Guía de Explicación:**
  * Enfatizar la diferencia fundamental con la sesión anterior: pasamos de modelar los *juicios humanos* (opinión de expertos) a analizar la *señal analítica de los datos empíricos* (la matriz de decisión).
  * Explicar que en la investigación doctoral se fomenta la **hibridación** (combinar enfoques objetivos y subjetivos) para aportar mayor rigor.

---

### Diapositiva 3: Agenda de la Sesión (3 Horas)
* **Contenido:** Distribución del tiempo (90 min de teoría, 45 min de debate de literatura y 45 min de taller práctico).
* **Guía de Explicación:** Explicar las expectativas del tiempo de trabajo y fomentar la participación activa en el debate.

---

### Diapositiva 4: Introducción a la Ponderación Objetiva
* **Contenido:** Definición y rol de la ponderación objetiva frente a la subjetiva. Concepto de discriminación por similitud de alternativas.
* **Guía de Explicación:**
  * Plantear el problema: *Imaginemos que evaluamos proveedores bajo el criterio "Tiempo de Entrega" y todos tardan exactamente 24 horas. ¿Qué tanto nos ayuda ese criterio a decidir?* (Nada, por lo tanto, matemáticamente su peso debe reducirse a cero, sin importar lo importante que sea operativamente).
  * Introducir el concepto de **información útil** o **poder de discriminación** de los criterios.

---

### Diapositiva 5: Filosofía de la Entropía de Shannon
* **Contenido:** Origen en la teoría de la información (Claude Shannon, 1948). Concepto de desorden, incertidumbre e información útil en MCDM.
* **Guía de Explicación:**
  * **Glosario Didáctico:**
    > **Entropía:** En física química representa el desorden. En teoría de la información, representa la incertidumbre o aleatoriedad de un mensaje. A mayor uniformidad en los datos, mayor entropía (más incertidumbre y menor poder de discriminación).
  * Conectar el concepto: Si los datos de las alternativas en una columna son idénticos, la incertidumbre sobre cuál elegir es máxima (entropía alta). Si los datos son muy dispersos, es fácil discriminar (entropía baja).

---

### Diapositiva 6: Algoritmo de la Entropía: Normalización
* **Contenido:** Fórmula de normalización sumatoria para probabilidades proyectadas: $p_{ij} = x_{ij}/\sum x_{kj}$.
* **Guía de Explicación:**
  * Explicar por qué es necesaria esta normalización: transforma los datos a una escala $[0, 1]$ que representa la proporción o probabilidad que cada alternativa aporta a la suma total del criterio.
  * Resaltar el requisito crítico: **los datos deben ser estrictamente positivos**. Además, si un criterio es de costo (se busca minimizar), debe transformarse previamente (ej. mediante inversión $1/x_{ij}$ o restando del valor máximo) para alinearlo con la lógica de beneficio.

---

### Diapositiva 7: Algoritmo de la Entropía: Cálculo de Entropía
* **Contenido:** Ecuación de entropía $e_j = -k \sum p_{ij} \ln(p_{ij})$ y constante de escala $k = 1/\ln(m)$.
* **Guía de Explicación:**
  * Explicar que la constante $k$ sirve para normalizar la entropía de manera que quede estrictamente entre 0 y 1, lo cual permite comparar criterios con diferente número de alternativas.
  * Advertencia de programación: Si una alternativa tiene un valor normalizado $p_{ij} = 0$, el logaritmo $\ln(0)$ no está definido. Explicar el tratamiento analítico $\lim_{p \to 0} p \ln(p) = 0$ y cómo implementarlo en Python o Excel (usando condicionales `if p > 0`).

---

### Diapositiva 8: Algoritmo de la Entropía: Pesos Finales
* **Contenido:** Cálculo del grado de divergencia $d_j = 1 - e_j$ y cálculo de los pesos finales $w_j = d_j/\sum d_k$.
* **Guía de Explicación:**
  * **Divergencia ($d_j$):** Representa qué tan "diferente" o informativo es el criterio. Si la entropía $e_j$ es baja (mucha dispersión), la divergencia $d_j$ será alta, otorgándole un peso mayor.
  * Mostrar cómo la suma de todos los pesos obtenidos es exactamente 1.0 (vector normalizado).

---

### Diapositiva 9: Método CRITIC (Diakoulaki et al., 1995)
* **Contenido:** Origen de CRITIC, deficiencias de la Entropía y propuesta híbrida (desviación estándar como contraste y correlación de Pearson como conflicto).
* **Guía de Explicación:**
  * **Glosario Didáctico:**
    > **CRITIC:** Siglas de *Criteria Importance Through Intercriteria Correlation*. Es un método que evalúa simultáneamente la variabilidad de cada criterio y la correlación cruzada con los demás para eliminar la redundancia de datos.
  * Plantear la crítica: Si medimos 3 criterios muy similares (ej. costo de flete, costo de seguro, costo de combustible), la Entropía les dará pesos altos a todos. CRITIC penalizará esta redundancia porque detectará que están fuertemente correlacionados.

---

### Diapositiva 10: Algoritmo CRITIC: Normalización y Desviación
* **Contenido:** Fórmulas de normalización Max-Min para beneficio y costo, y cálculo de la desviación estándar $\sigma_j$ de cada criterio.
* **Guía de Explicación:**
  * Explicar que la normalización Max-Min en CRITIC aísla las escalas y unifica la dirección de todos los criterios hacia la maximización (el mejor valor siempre es 1 y el peor es 0).
  * Explicar que la desviación estándar $\sigma_j$ de cada columna mide la intensidad de contraste de la información. A mayor desviación, mayor contraste y, por ende, mayor peso potencial.

---

### Diapositiva 11: Algoritmo CRITIC: Matriz de Correlación y Conflicto
* **Contenido:** Cálculo de la correlación de Pearson $r_{jk}$, el término de conflicto $(1-r_{jk})$ y la cantidad de información $C_j = \sigma_j \sum (1-r_{jk})$.
* **Guía de Explicación:**
  * **Glosario Didáctico:**
    > **Correlación de Pearson ($r_{jk}$):** Medida estadística entre -1 y 1 que indica la fuerza y dirección de una relación lineal entre dos variables. Un valor cercano a 1 indica que los criterios se comportan de forma casi idéntica (redundancia).
  * Analizar la fórmula: Si un criterio tiene alta correlación positiva con los demás, la suma de $(1 - r_{jk})$ será pequeña (poca información única). Si tiene correlación negativa o nula, aportará información valiosa no cubierta por otros criterios, incrementando $C_j$.

---

### Diapositiva 12: Algoritmo CRITIC: Pesos Finales
* **Contenido:** Obtención de pesos normalizados $w_j = C_j/\sum C_k$ e interpretación teórica.
* **Guía de Explicación:**
  * Resumir la lógica: el peso de un criterio es directamente proporcional a su desviación estándar (contraste) y a su independencia lineal respecto a los demás (conflicto).
  * Preguntar a los alumnos qué método prefieren si tuvieran datos altamente ruidosos en su tesis doctoral.

---

### Diapositiva 13: Comparación Epistemológica: Subjetivo vs. Objetivo
* **Contenido:** Tabla comparativa que evalúa fuente de información, carga cognitiva, sensibilidad a datos, redundancia y uso recomendado para tesis doctorales.
* **Guía de Explicación:**
  * Explicar que el mayor peligro de la ponderación objetiva es la dependencia absoluta de la muestra de datos actual. Si cambiamos la muestra de alternativas, los pesos de los criterios cambiarán completamente, lo cual puede ser inaceptable en decisiones estratégicas de largo plazo.
  * Discutir cómo mitigar esto con **pesos combinados** (ej. $w_j^{final} = \alpha w_j^{subjetivo} + (1-\alpha) w_j^{objetivo}$).

---

### Diapositiva 14: Discusión de Literatura (Debate Socrático)
* **Contenido:** Preguntas detonantes sobre la paradoja de la licitación y el método MEREC (Keshavarz-Ghorabaee, 2021).
* **Guía de Explicación:**
  * **Paradoja de la licitación:** Fomentar el debate socrático. Si el costo es lo más importante para la gerencia, pero todos cobran igual, ¿está bien que el modelo le asigne peso 0? (Matemáticamente sí, porque no ayuda a discriminar; estratégicamente puede ser riesgoso si el decisor olvida que el costo sigue siendo un límite duro).
  * **MEREC:** Explicar el concepto de "efecto de remoción". Sirve para comparar cómo la remoción de un criterio cambia las puntuaciones relativas. Fomentar la discusión en aplicaciones de inventario (ABC) y selección de rutas.

---

### Diapositiva 15: Taller Aplicado: Ejercicio Guiado en Excel
* **Contenido:** Datos del caso práctico guiado de 3 CEDIS con 3 criterios cuantitativos (OTIF, Costo, Ciclo de orden).
* **Guía de Explicación:**
  * Abrir Excel en vivo y realizar la normalización max-min de los datos.
  * Mostrar cómo calcular la correlación (`COEF.DE.CORR` en Excel) y la desviación estándar (`DESVEST.P`).
  * Resolver la ecuación en vivo para que los alumnos entiendan el flujo matemático antes de programarlo en Python.

---

### Diapositiva 16: Caso Práctico Autónomo en Python
* **Contenido:** Planteamiento del reto de los 10 transportistas terrestres y 4 KPIs operativos.
* **Guía de Explicación:**
  * Explicar que se evaluará el uso de código limpio en Jupyter Notebooks.
  * Indicar que no deben usar paquetes predefinidos (cajas negras) para el cálculo de entropía o CRITIC, sino codificar los algoritmos usando operaciones vectoriales nativas en NumPy y Pandas.

---

### Diapositiva 17: Conclusiones
* **Contenido:** Puntos de recapitulación clave (señal numérica de los datos, límites de la entropía, ventajas de CRITIC y pesos combinados para tesis).
* **Guía de Explicación:** Vincular el aprendizaje con los entregables del curso (Caso Práctico E1) y motivar al desarrollo de sus artículos de tesis.

---

### Diapositiva 18: Referencias Obligatorias
* **Contenido:** Bibliografía seminal (Diakoulaki 1995, Keshavarz-Ghorabaee 2021, Shannon 1948).
* **Guía de Explicación:** Recordarles que todos los PDFs de lectura obligatoria están disponibles en la carpeta `literatura/articulos` del proyecto.
