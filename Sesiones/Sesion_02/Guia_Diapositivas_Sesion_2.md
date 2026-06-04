# Guía de Apoyo al Docente: Diapositivas de la Sesión 2
**Materia:** Herramientas Multicriterio para Toma de Decisiones  
**Tema:** Ponderación Subjetiva: AHP (Saaty) y Best-Worst Method (BWM)  
**Programa:** Doctorado en Logística y Cadena de Suministro, FIME – UANL  

Este documento proporciona una guía diapositiva por diapositiva para el profesor, detallando los puntos clave a explicar, las notas pedagógicas y cómo conectar la matemática compleja con conceptos comprensibles para estudiantes de posgrado con perfiles multidisciplinarios.

---

## 📋 Índice de Diapositivas

### Diapositiva 1: Portada
* **Contenido:** Título del curso, tema de la sesión, datos del profesor e institución.
* **Propósito:** Encuadrar la sesión y establecer el ambiente académico formal del Doctorado.

---

### Diapositiva 2: Objetivos de la Sesión
* **Contenido:** Logros de aprendizaje esperados (analizar críticamente axiomas de AHP, evaluar Rank Reversal, dominar algoritmo minimax de BWM y resolver problemas logísticos).
* **Guía de Explicación:**
  * Enfatizar el verbo **"Analizar críticamente"**: A nivel doctorado, no basta con usar el software de AHP (ej. SuperDecisions); es necesario comprender y cuestionar las limitaciones teóricas del método.
  * Introducir la diferencia entre la toma de decisiones heurística y los modelos de optimización rigurosos.

---

### Diapositiva 3: Agenda de la Sesión (3 Horas)
* **Contenido:** División del tiempo (90 min de teoría y axiomas, 45 min de debate de literatura y 45 min de taller práctico en Python/Excel).
* **Guía de Explicación:** Explicar las expectativas del tiempo de trabajo y fomentar la participación activa en el Bloque 2 (Debate Socrático).

---

### Diapositiva 4: Introducción a la Ponderación Subjetiva
* **Contenido:** Explicación del rol de los pesos ($w_j$) de los criterios ($C_j$). Diferencia entre ponderación subjetiva (basada en opiniones de expertos) y objetiva (deducida analíticamente de la dispersión de datos).
* **Guía de Explicación:**
  * Plantear el dilema: *¿Cómo sabemos si un peso asignado del 50% a la confiabilidad es matemáticamente representativo y no solo un sesgo momentáneo del decisor?*
  * Introducir el concepto de **fatiga cognitiva** cuando el número de criterios es elevado.

---

### Diapositiva 4b: Posicionamiento de Métodos: Compensatorios vs. No Compensatorios
* **Contenido:** Estructuración y clasificación de los métodos MCDM según su nivel de compensación (Compensatorios: AHP, BWM, TOPSIS, VIKOR, MAUT vs. No Compensatorios: ELECTRE, PROMETHEE).
* **Guía de Explicación:**
  * Explicar el concepto de **Compensación**: la posibilidad de balancear o comerciar un desempeño pobre en un criterio mediante un desempeño excelente en otro (trade-offs).
  * Explicar los métodos **No Compensatorios**: donde existen vetos o dominancias estrictas que previenen la compensación (comunes en decisiones con restricciones regulatorias, de seguridad o ambientales en cadena de suministro).
  * Enmarcar que AHP y BWM se posicionan en la familia de métodos para modelos **compensatorios**, pero son los encargados de elicitar los pesos subjetivos iniciales.

---

### Diapositiva 5: Fundamentos del Proceso de Jerarquía Analítica (AHP)
* **Contenido:** Origen de AHP (Thomas Saaty, 1970s), descomposición jerárquica y el paso fundamental de reemplazar estimaciones directas por comparaciones pareadas.
* **Guía de Explicación:**
  * Describir la estructura jerárquica de arriba hacia abajo (Meta $\rightarrow$ Criterios $\rightarrow$ Alternativas).
  * Explicar por qué los seres humanos son malos estimando pesos absolutos directamente (ej. "el costo pesa 0.35"), pero consistentes comparando de dos en dos (ej. "el costo es moderadamente más importante que el tiempo").

---

### Diapositiva 6: Ciento Axiomático del AHP
* **Contenido:** Los 4 axiomas de Saaty: Reciprocidad, Homogeneidad, Dependencia y Expectativas.
* **Guía de Explicación:**
  * **Glosario Didáctico:** 
    > **Axioma:** Una regla o principio tan básico y claro que se acepta como verdadero sin necesidad de demostración matemática, sirviendo de cimiento para el resto de la teoría.
  * Explicar detenidamente el axioma de **Reciprocidad**: si $A$ es 3 veces más importante que $B$, entonces $B$ es $1/3$ de importante que $A$.
  * Explicar **Homogeneidad**: no comparar el costo de un flete terrestre ($1,000 MXN) con el costo de construir un puerto marítimo ($100 millones USD) en el mismo nivel jerárquico.

---

### Diapositiva 7: La Escala Fundamental de Comparación (1 a 9)
* **Contenido:** Escala discreta de Saaty, definiciones verbales y lógica cognitiva (Ley de Miller de la capacidad humana: $7 \pm 2$).
* **Guía de Explicación:**
  * Explicar la fundamentación psicológica: el cerebro humano solo puede procesar y categorizar simultáneamente entre 5 y 9 objetos distintos de información sin confundirse.
  * Cuestionar a los estudiantes: *¿Por qué usar una escala de 1 a 9 y no una escala de 1 a 100?* (La escala 1-100 induce un falso sentido de precisión e incrementa el error).

---

### Diapositiva 8: Construcción de la Matriz AHP
* **Contenido:** Definición formal de la matriz $\mathbf{A} \in \mathbb{R}^{n \times n}$. Cálculo del número total de comparaciones requeridas $N = \frac{n(n-1)}{2}$.
* **Guía de Explicación:**
  * Mostrar cómo la diagonal de la matriz siempre se llena con 1s ($a_{ii}=1$), y la parte inferior es la recíproca de la superior.
  * Hacer el cálculo numérico: si tenemos $n=8$ criterios logísticos, requerimos hacer 28 comparaciones en una encuesta, lo cual puede generar fatiga y respuestas aleatorias en los decisores.

---

### Diapositiva 9: Elicitación del Vector de Prioridades
* **Contenido:** Concepto de consistencia teórica perfecta ($a_{ij} = w_i / w_j$), el autovector principal y el Teorema de Perron-Frobenius.
* **Guía de Explicación:**
  * **Glosario Didáctico:**
    > **Elicitación:** El arte o proceso sistemático de "extraer" el conocimiento subjetivo de la mente del experto y plasmarlo en números estructurados.
    > **Autovector (Eigenvector):** Dirección matemática estable asociada a una matriz. En AHP, representa el peso óptimo de los criterios derivado de la influencia mutua de todas las comparaciones de la matriz.
  * Explicar la ecuación fundamental: $\mathbf{A}\mathbf{w} = \lambda_{\max}\mathbf{w}$. Si no hay ruido, $\lambda_{\max} = n$. Si hay ruido conceptual del decisor, $\lambda_{\max} > n$.

---

### Diapositiva 10: Medición de la Consistencia en AHP
* **Contenido:** Fórmulas para el Índice de Consistencia ($CI = \frac{\lambda_{\max}-n}{n-1}$) y la Razón de Consistencia ($CR = CI/RI$). Tabla del Índice Aleatorio ($RI$).
* **Guía de Explicación:**
  * Explicar que el Índice Aleatorio ($RI$) es la consistencia promedio de matrices de tamaño $n$ llenadas con números aleatorios.
  * Enfatizar la regla de oro: **$CR < 10\%$**. Si el error es mayor al 10%, los juicios del experto son demasiado incoherentes (aleatorios) y se debe repetir la encuesta.

---

### Diapositiva 11: El Gran Debate: Rank Reversal (Inversión de Rangos)
* **Contenido:** La polémica de Dyer vs. Saaty (1990) en *Management Science*. Qué pasa al agregar alternativas duplicadas o irrelevantes.
* **Guía de Explicación:**
  * Explicar conceptualmente el problema: Si un modelo dice que el transportista A es mejor que el B, y al introducir al modelo un transportista C (que es idéntico a B) el modelo cambia de opinión y pone a B sobre A, esto se llama **Rank Reversal**.
  * Explicar las dos posturas: Dyer lo considera un error matemático imperdonable; Saaty argumenta que la mente humana cambia prioridades de forma natural cuando cambia el contexto de decisión.

---

### Diapositiva 12: Limitaciones de AHP
* **Contenido:** Alta carga cognitiva, susceptibilidad a la inconsistencia estructural y escala asimétrica.
* **Guía de Explicación:**
  * Resumir por qué AHP se vuelve impráctico cuando hay muchos criterios.
  * Plantear la pregunta que da paso al siguiente tema: *¿Cómo podemos ponderar subjetivamente de manera más eficiente?*

---

### Diapositiva 13: Introducción al Best-Worst Method (BWM)
* **Contenido:** Metodología de Jafar Rezaei (2015), comparación estructurada Best-to-Others y Others-to-Worst, y la fórmula del número de comparaciones $N_{BWM} = 2n-3$.
* **Guía de Explicación:**
  * **Glosario Didáctico:**
    > **Convexidad:** Propiedad matemática que garantiza que la superficie de búsqueda del problema de optimización no tiene "valles falsos" (óptimos locales). Si el solucionador encuentra un mínimo, es el mejor absoluto de todo el espacio de búsqueda (óptimo global).
  * Explicar el ahorro en el esfuerzo: para $n=8$, pasamos de 28 comparaciones en AHP a solo 13 en BWM.

---

### Diapositiva 14: Los Pasos del Algoritmo BWM
* **Contenido:** Pasos del algoritmo: definir criterios, identificar Best/Worst, construir el vector Best-to-Others ($A_B$) y el vector Others-to-Worst ($A_W$).
* **Guía de Explicación:**
  * Mostrar paso a paso el flujo de trabajo conceptual de una encuesta BWM.
  * Resaltar que en BWM el decisor nunca compara criterios de mediana importancia entre sí, eliminando comparaciones redundantes e innecesarias.

---

### Diapositiva 15: Formulación Matemática Minimax de BWM
* **Contenido:** Modelo matemático minimax no lineal y no convexo.
* **Guía de Explicación:**
  * **Glosario Didáctico:**
    > **Minimax:** Un enfoque matemático de optimización que busca "minimizar el peor de los casos" o la desviación máxima entre lo que dice el experto y los pesos reales asignados.
  * Detallar las restricciones de valor absoluto: $\left| \frac{w_B}{w_j} - a_{Bj} \right| \le \xi$.
  * Explicar el problema de este modelo: debido a la división de variables, el problema no es lineal y puede tener múltiples óptimos locales, lo que genera inestabilidad en los resultados.

---

### Diapositiva 16: Modelo BWM Lineal de Rezaei (2016)
* **Contenido:** Formulación de programación lineal libre de divisiones y convexidad del problema.
* **Guía de Explicación:**
  * Mostrar cómo la simple multiplicación por el denominador transforma el modelo no lineal en uno lineal: $\left| w_B - a_{Bj} w_j \right| \le \xi^L$.
  * Explicar que los problemas lineales son sumamente fáciles y rápidos de resolver en computadoras comunes utilizando solvers libres (como `scipy.optimize.linprog`).

---

### Diapositiva 17: Consistencia en el Método BWM
* **Contenido:** Razón de consistencia en BWM $CR = \frac{\xi^*}{CI}$ y la tabla de Índices de Consistencia ($CI$).
* **Guía de Explicación:** Explica que a diferencia de AHP, la consistencia mínima en BWM depende del valor del juicio extremo asignado al comparar el mejor criterio frente al peor ($a_{BW}$).

---

### Diapositiva 18: Comparación Directa: AHP vs. BWM
* **Contenido:** Tabla comparativa (complejidad, consistencia, optimización, carga cognitiva).
* **Guía de Explicación:**
  * **Glosario Didáctico:**
    > **Transitividad:** Consistencia de lógica transitiva: si prefieres la manzana a la pera, y la pera al plátano, lógicamente prefieres la manzana al plátano. Romper esta cadena es una violación a la transitividad.
  * Resumir la tabla. Ayudar al estudiante doctoral a elegir cuál método conviene según el problema de investigación que estén planteando en su tesis.

---

### Diapositiva 19: Caso de Estudio: Selección de Transportista LTL
* **Contenido:** Datos del caso práctico: Costo ($C_1$), Confiabilidad ($C_2$), Visibilidad ($C_3$), y Sustentabilidad ($C_4$). Parámetros BWM de entrada (Best: $C_2$, Worst: $C_4$).
* **Guía de Explicación:** Explicar el escenario de cadena de suministro (transporte consolidado LTL en Monterrey) y cómo se derivan los vectores de comparación a partir de las prioridades del comité del CEDIS.

---

### Diapositiva 20: Taller Práctico y Trabajo Autónomo (E1)
* **Contenido:** Pautas del entregable E1. Tareas: cálculo de consistencia en AHP, implementación de BWM lineal en Python y correlación de rankings.
* **Guía de Explicación:**
  * Explicar la importancia del taller aplicado para la calificación.
  * Instruir sobre el uso de bibliotecas de optimización en Python.

---

### Diapositiva 21: Conclusiones
* **Contenido:** Puntos de recapitulación (impacto de la ponderación subjetiva, el estándar de AHP frente a la eficiencia de BWM y su relación con el PIA).
* **Guía de Explicación:** Cerrar la sesión vinculando los métodos con el Producto Integrador de Aprendizaje (PIA).

---

### Diapositiva 22: Referencias Bibliográficas Clave
* **Contenido:** Bibliografía obligatoria para investigación (Saaty 1980, Rezaei 2015, Rezaei 2016, Dyer 1990).
* **Guía de Explicación:** Motivar a los estudiantes a buscar y leer las fuentes directas y seminales en la carpeta `literatura/articulos` para sus respectivas tesis.
