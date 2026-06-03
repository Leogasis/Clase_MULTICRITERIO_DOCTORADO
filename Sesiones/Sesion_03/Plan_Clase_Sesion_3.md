# Plan de Clase Detallado: Sesión 3
**Materia:** Herramientas Multicriterio para Toma de Decisiones  
**Programa:** Doctorado en Logística y Cadena de Suministro, FIME – UANL  
**Duración:** 3 horas (180 minutos)  
**Profesor:** Dr. Leonardo Gabriel Hernández Landa  
**Tema General:** Ponderación Objetiva de Criterios: Entropía de Shannon y Método CRITIC  

---

## 🎯 Objetivos de la Sesión
Al finalizar esta tercera sesión, el estudiante de doctorado será capaz de:
1. **Analizar la filosofía matemática** de la ponderación objetiva basada en la variabilidad e interacción de los datos en lugar de la opinión de expertos.
2. **Formular e implementar** el cálculo de pesos a través de la Entropía de Shannon para medir el contenido de información de cada criterio.
3. **Calcular pesos óptimos** utilizando el método CRITIC, incorporando tanto la desviación estándar como la correlación lineal (Pearson) entre criterios.
4. **Contrastar críticamente** los resultados de pesos subjetivos (Sesión 2) y objetivos (Sesión 3) aplicados a un mismo conjunto de datos operativos de almacenes.

---

## ⏱️ Estructura del Tiempo (180 minutos en total)

| Bloque | Actividad | Tiempo | Porcentaje |
| :--- | :--- | :---: | :---: |
| **Bloque 1** | Exposición Teórica (Filosofía de la información de Shannon, algoritmos de Entropía y CRITIC) | 90 min | 50% |
| **Bloque 2** | Debate Socrático de Literatura (Diakoulaki et al. 1995, Keshavarz-Ghorabaee 2021) | 45 min | 25% |
| **Bloque 3** | Taller Aplicado y Ejercicios (Cálculo de Entropía en Excel/Python y discusión de contrastes) | 45 min | 25% |

---

## 📚 Preparación Previa Requerida (Flipped Classroom)
*Los estudiantes debieron leer con antelación los siguientes recursos:*
1. **Artículo:** Diakoulaki, D., Mavrotas, G., & Papayannakis, L. (1995). *Determining objective weights in multiple criteria problems: the CRITIC method*. Computers \& Operations Research, 22(7), 763–770.
2. **Artículo:** Keshavarz-Ghorabaee, M., et al. (2021). *Determination of Objective Weights Using a New Method Based on the Removal Effects of Criteria (MEREC)*. Symmetry, 13(4), 525. [S08_Keshavarz_Ghorabaee_et_al_2021_Determination_of_Objective_Weights_Using_MEREC.pdf](file:///Users/leonardohernandez/Academica/Clase_MULTICRITERIO_DOCTORADO/literatura/articulos/S08_Keshavarz_Ghorabaee_et_al_2021_Determination_of_Objective_Weights_Using_MEREC.pdf)
3. **Guía de Lectura Asignada:** 
   * ¿Cuál es el supuesto subyacente de la Entropía respecto a la varianza de un criterio? (¿Un criterio con alta varianza recibe más o menos peso?).
   * ¿Cómo resuelve CRITIC la redundancia entre criterios altamente correlacionados?

---

## 📖 Contenido Temático y Desarrollo de la Sesión

### BLOQUE 1: Exposición Teórica (90 min)
* **La Filosofía de la Ponderación Objetiva:**
  * Sesgos cognitivos del tomador de decisiones vs. la señal intrínseca de los datos empíricos.
* **El Método de la Entropía de Shannon:**
  * Normalización sumatoria de la matriz de decisión: $p_{ij} = x_{ij} / \sum x_{kj}$.
  * Cálculo de la entropía del criterio $C_j$: $e_j = -k \sum p_{ij} \ln(p_{ij})$ (donde $k = 1/\ln(m)$).
  * Grado de divergencia: $d_j = 1 - e_j$.
  * Obtención de pesos normalizados: $w_j = d_j / \sum d_k$.
* **El Método CRITIC:**
  * Normalización Max-Min para proyectar a $[0, 1]$.
  * Cálculo de la desviación estándar $\sigma_j$ de cada criterio.
  * Cálculo de la matriz de correlación de Pearson $r_{jk}$.
  * Medida de la cantidad de información $C_j$: $C_j = \sigma_j \sum_{k=1}^n (1 - r_{jk})$.
  * Obtención de pesos: $w_j = C_j / \sum C_k$.

---

### BLOQUE 2: Discusión de Literatura - Debate Socrático (45 min)
* **Pregunta Detonante 1:** *En logística, el costo casi siempre es considerado el criterio más "importante" subjetivamente por el director financiero. Sin embargo, en una licitación donde todos los transportistas cotizan tarifas casi idénticas, el método de Entropía le dará un peso cercano a cero al costo. ¿Tiene sentido metodológico esto? ¿Cómo afecta a la toma de decisiones reales?*
* **Pregunta Detonante 2:** *El método MEREC (2021) propone calcular pesos basándose en el efecto de remover un criterio. ¿En qué escenarios logísticos de cadena de suministro (ej. gestión de inventarios, selección de rutas) consideran que este enfoque es superior a la Entropía?*

---

### BLOQUE 3: Taller Práctico - Ejercicios (45 min)

#### 3.1. Ejercicio Guiado (Profesor): Cálculo de Pesos CRITIC en Excel
El profesor guiará el cálculo paso a paso de pesos CRITIC para evaluar el desempeño de 3 almacenes (CEDIS) con 3 criterios cuantitativos:
1. Exactitud de Inventario (%).
2. Costo operativo por caja procesada (USD).
3. Tiempo de ciclo de orden (horas).

#### 3.2. Caso Práctico Alumno (Trabajo Autónomo)
El alumno recibirá un dataset real de 10 transportistas terrestres evaluados bajo 4 KPIs operativos. Deberá calcular los pesos por Entropía y por CRITIC en Python utilizando librerías científicas, graficar los perfiles de pesos obtenidos y contrastar los resultados.
* **Entregable:** Script de Python ejecutable y reporte gráfico comparativo.

---

## 🎓 Plan de Evidencias (Evaluación)
Esta sesión cierra los conceptos para el **E1 (Caso Práctico 1: Ponderación de Criterios: AHP vs. BWM vs. Entropía)**, el cual vence y se entrega en la **Sesión 4** (Ponderación **15%**).
