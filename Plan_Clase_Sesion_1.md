# Plan de Clase Detallado: Sesión 1
**Materia:** Herramientas Multicriterio para Toma de Decisiones  
**Programa:** Doctorado en Logística y Cadena de Suministro, FIME – UANL  
**Duración:** 3 horas (180 minutos)  
**Profesor:** Dr. Leonardo Gabriel Hernández Landa  
**Tema General:** Fundamentos Epistemológicos de la Toma de Decisiones Multicriterio  

---

## 🎯 Objetivos de la Sesión
Al finalizar esta primera sesión, el estudiante de doctorado será capaz de:
1. **Contrastar críticamente** el paradigma de la optimización clásica (mono-objetivo, realista) frente al de la ayuda a la decisión multicriterio (MCDM, constructivista).
2. **Clasificar y mapear** los problemas de decisión bajo la taxonomía de MCDM, MADM y MODM.
3. **Analizar la literatura científica** para identificar tendencias metodológicas y aplicaciones de MCDM en logística y cadena de suministro.
4. **Construir y analizar** un mapa bibliométrico preliminar en VOSviewer para detectar brechas de investigación (research gaps) en logística.

---

## ⏱️ Estructura del Tiempo (180 minutos en total)

| Bloque | Actividad | Tiempo | Porcentaje |
| :--- | :--- | :---: | :---: |
| **Bloque 1** | Encuadre del Curso y Exposición Teórica (Fundamentos y Taxonomía) | 90 min | 50% |
| **Bloque 2** | Discusión de Literatura (Debate Socrático de Lecturas Obligatorias) | 45 min | 25% |
| **Bloque 3** | Taller Práctico Aplicado (Mapeo Bibliométrico con VOSviewer) | 45 min | 25% |

---

## 📚 Preparación Previa Requerida (Flipped Classroom)
*Los estudiantes debieron leer con antelación los siguientes recursos:*
1. **Capítulo:** Figueira, J., Greco, S., & Ehrgott, M. (2016). *An overview of MCDM concepts and approaches*. En Multiple Criteria Decision Analysis (2nd ed., Cap. 1, pp. 1–33). Springer.
2. **Artículo:** Mardani, A., et al. (2015). *Multiple criteria decision-making techniques and their applications – a survey*. Economic Research, 28(1), 516–571.
3. **Guía de Lectura Asignada:** 
   - ¿Cómo se diferencia la ontología del MCDM respecto a la optimización clásica?
   - Identifica al menos 3 debates epistemológicos en la literatura revisada.
   - ¿Qué papel juega la racionalidad acotada de Herbert Simon en el desarrollo del MCDM?

---

## 📖 Contenido Temático y Desarrollo de la Sesión

### BLOQUE 1: Encuadre Académico y Exposición Teórica (90 min)

#### 1.1. Encuadre Pedagógico e Introducción al Doctorado (15 min)
*   **Presentación del Curso:** Filosofía del programa analítico. Enfoque orientado a la aplicación de métodos matemáticos multicriterio.
*   **Explicación del Sistema de Evaluación (Casos Prácticos + PIA):** 
    - Explicar cómo las actividades se estructuran en 4 **Casos Prácticos** para dominar algoritmos y un **Producto Integrador de Aprendizaje (PIA)** de investigación:
      - **CP1 (Sesión 5 - 15%):** Ponderación e Importancia de Criterios (AHP vs. BWM).
      - **CP2 (Sesión 8 - 20%):** Jerarquización por Distancias (TOPSIS vs. VIKOR vs. EDAS).
      - **CP3 (Sesión 10 - 20%):** Relaciones de Superación No Compensatorias (ELECTRE vs. PROMETHEE).
      - **CP4 (Sesión 13 - 15%):** Modelado con Incertidumbre y Lógica Difusa (Fuzzy TOPSIS o GRA).
      - **PIA (Sesión 15 - 30%):** Producto Integrador de Aprendizaje (Artículo de Investigación y Defensa). Se inicia formalmente en la Sesión 8.
*   **Expectativas de Nivel Doctoral:** Cuestionamiento crítico de los métodos, rigurosidad matemática y relevancia en la toma de decisiones.

#### 1.2. Paradigmas en la Investigación de Operaciones (30 min)
*   **Racionalidad Sustantiva (Optimización Clásica) vs. Racionalidad Procedimental / Acotada (Herbert Simon):**
    - El mito de la "solución óptima global" única.
    - La búsqueda de la solución "satisfactoria" y robusta bajo criterios en conflicto.
*   **Enfoques Ontológicos en Toma de Decisiones:**
    - **Normativo:** ¿Cómo *debería* decidir un decisor ideal racional? (Axiomático).
    - **Descriptivo:** ¿Cómo deciden *realmente* las personas? (Sesgos cognitivos, psicología).
    - **Prescriptivo / Constructivista:** ¿Cómo podemos ayudar al decisor a estructurar y resolver su problema mediante un proceso interactivo de aprendizaje? (El analista como facilitador).
*   **Optimización Mono-objetivo vs. MCDM:**
    - Objetivos únicos (ej. minimizar costos) vs. objetivos multidimensionales en conflicto (ej. minimizar costos, minimizar emisiones de CO₂, maximizar resiliencia y minimizar tiempos de tránsito).
    - Inconmensurabilidad de criterios: ¿Cómo comparar pesos monetarios con impactos ecológicos o sociales?

#### 1.3. Glosario y Taxonomía MCDM (25 min)
*   **MCDM (Multi-Criteria Decision Making):** El término sombrilla.
*   **MADM (Multi-Attribute Decision Making):** 
    - Decisiones con alternativas discretas, finitas y explícitas (ej. seleccionar entre 5 proveedores 3PL).
    - Enfoque en la evaluación y ordenamiento.
*   **MODM (Multi-Objective Decision Making):**
    - Decisiones con alternativas infinitas / continuas en un espacio de diseño restringido (ej. optimizar las variables de producción y transporte sujeto a restricciones).
    - Enfoque en la generación de fronteras de Pareto.
*   **Elementos Esenciales de un Modelo MADM:**
    - **Decisor (Decision Maker - DM):** Su rol subjetivo y preferencias.
    - **Analista (Analyst):** Diseñador del modelo.
    - **Alternativas ($A_i$):** El conjunto de opciones a evaluar.
    - **Criterios ($C_j$):** Las dimensiones de evaluación.
    - **Pesos de Criterios ($w_j$):** Importancia relativa de cada criterio.
    - **Matriz de Decisión ($X_{ij}$):** Evaluación de cada alternativa respecto a cada criterio.

#### 1.4. Problemáticas en Logística Susceptibles de MCDM (20 min)
*   **Selección de Proveedores (Green/Sustainable Supplier Selection):** El clásico trade-off entre costo, calidad, entrega, y cumplimiento ambiental.
*   **Localización de Instalaciones Multicriterio (Centros de Distribución):** Costo de terreno, cercanía a clientes, conectividad, disponibilidad de mano de obra, riesgos climáticos y políticos.
*   **Selección de Modos de Transporte e Intermodalidad:** Costo, tiempo de tránsito, variabilidad del lead time, emisiones de carbono, y seguridad.
*   **Resiliencia de Cadena de Suministro:** Evaluación de riesgos de disrupción frente a costos de redundancia.

---

### BLOQUE 2: Discusión de Literatura - Debate Socrático (45 min)

Este bloque se desarrollará mediante preguntas detonantes basadas en las lecturas previas. El profesor actuará como moderador socrático, impulsando a los estudiantes a justificar sus argumentos.

#### 2.1. Discusión de Figueira, Greco & Ehrgott (2016) - Cap. 1 (25 min)
*   **Pregunta Detonante 1:** *Figueira et al. discuten la evolución de la disciplina de MCDM desde finales de los 60. ¿Cuáles consideran que fueron las tensiones epistemológicas que forzaron el surgimiento del MCDM como un campo independiente de la Investigación de Operaciones clásica basada en programación lineal y entera?*
    - *Respuestas esperadas:* La insatisfacción de los tomadores de decisiones ante soluciones óptimas de un solo criterio que ignoraban aspectos sociales o cualitativos; el fracaso en la implementación práctica de modelos puramente cuantitativos y rígidos.
*   **Pregunta Detonante 2:** *En el capítulo se menciona la distinción de las tres grandes "familias" de métodos: (1) Métodos basados en teoría de la utilidad (MAUT), (2) Métodos de superación / outranking (ELECTRE, PROMETHEE) y (3) Métodos interactivos o de programación matemática multiobjetivo. Desde la perspectiva epistemológica, ¿cómo asume cada familia la modelación de las preferencias del decisor?*
    - *Respuestas esperadas:* MAUT asume racionalidad fuerte e inconmensurabilidad débil (se puede compensar un mal desempeño en un criterio con un excelente desempeño en otro). El Outranking acepta la incomparabilidad y el veto, asumiendo un enfoque más constructivista y no-compensatorio.
*   **Pregunta Detonante 3:** *¿Qué es el concepto de "inconmensurabilidad"? ¿Cómo lo resuelven los teóricos de la decisión?*

#### 2.2. Discusión de Mardani et al. (2015) - Survey de Aplicaciones (20 min)
*   **Pregunta Detonante 1:** *Mardani et al. presentan una radiografía masiva del uso de MCDM entre 1980 y 2015. El estudio revela que los métodos híbridos y el AHP clásico dominan las publicaciones. ¿Por qué creen que AHP sigue siendo tan popular a pesar de las críticas epistemológicas y de consistencia que ha recibido (como la inversión de rangos / rank reversal)?*
    - *Respuestas esperadas:* Facilidad de comprensión para los decisores en la industria, estructura jerárquica natural de los problemas organizacionales, y marketing académico histórico del método.
*   **Pregunta Detonante 2:** *Basado en los resultados de Mardani et al., ¿cuáles son los vacíos metodológicos que persisten en la aplicación de MCDM en logística? Si la mayoría de las publicaciones son aplicaciones directas de métodos conocidos, ¿dónde radica la contribución científica de un doctorando hoy en día?*
    - *Respuestas esperadas:* La contribución ya no puede ser simplemente aplicar un método conocido (ej. "Aplicación de TOPSIS a X empresa"). La contribución doctoral debe estar en la modelación híbrida, el tratamiento avanzado de la incertidumbre, o la comparación experimental de métodos para demostrar robustez.

---

### BLOQUE 3: Taller Práctico - Mapeo Bibliométrico con VOSviewer (45 min)

*Esta actividad práctica sirve como apoyo opcional para explorar la literatura de aplicaciones del MCDM.*

#### 3.1. Introducción al Análisis Bibliométrico (10 min)
*   Explicar la diferencia entre una revisión de literatura narrativa tradicional y un estudio bibliométrico cuantitativo (co-ocurrencia, co-citación, acoplamiento).
*   Introducción a VOSviewer como software de mapeo y visualización de redes bibliográficas.

#### 3.2. Extracción de Datos en Vivo (Profesor demuestra, Alumnos replican) (15 min)
1.  **Acceso a Base de Datos:** Los alumnos ingresan a Scopus o Web of Science a través de la biblioteca digital UANL.
2.  **Cadena de Búsqueda de Prueba:**
    `TITLE-ABS-KEY ( "multicriteria" OR "MCDM" OR "MCDA" ) AND TITLE-ABS-KEY ( "logistics" OR "supply chain" )`
3.  **Filtros de Búsqueda:** Limitar a los últimos 5-10 años, tipo de documento "Article" o "Review", e idioma "English".
4.  **Exportación:** Exportar la información bibliográfica y de citación en formato **RIS** o **CSV (Excel/Scopus)**, asegurándose de incluir:
    - Autores, Título, Año.
    - Metadatos de Citación.
    - Resumen (Abstract) y Palabras Clave (Keywords).

#### 3.3. Configuración y Visualización en VOSviewer (15 min)
1.  Abrir VOSviewer.
2.  Seleccionar: `Create` -> `Create a map based on bibliographic data` -> `Read data from bibliographic database files`.
3.  Cargar el archivo exportado de Scopus/WoS.
4.  **Tipo de Análisis:** `Co-occurrence` (Co-ocurrencia) de `Author keywords` o `All keywords`.
5.  **Método de Conteo:** `Full counting`.
6.  **Umbral:** Definir un número mínimo de ocurrencias de una palabra clave (ej. 5 o 10) para filtrar palabras irrelevantes.
7.  **Visualización del Mapa:**
    - Explicar el significado de los nodos (frecuencia de palabras), las líneas (fuerza de enlace/co-ocurrencia), y los clusters (comunidades de investigación).
    - Identificar las palabras clave emergentes (ej. "circular economy", "industry 4.0", "resilience").

#### 3.4. Cierre y Tarea (5 min)
*   **Conexión con Entregables:** Este análisis bibliométrico les permite explorar aplicaciones reales y seleccionar criterios validados para formular el problema logístico de sus Casos Prácticos.
*   **Recordatorio Próxima Sesión:** Lectura de Dyer (2005) sobre MAUT (Theory of Multiattribute Utility) y Keeney & Raiffa (capítulos indicados).

---

## 🛠️ Recursos y Software Necesarios
*   **Para el Profesor:** Proyector/Pantalla, acceso a Internet, pizarrón para debatir diagramas de racionalidad.
*   **Para los Alumnos:** Computadora portátil personal.
*   **Software Instalado:** **VOSviewer** (descarga libre de [vosviewer.com](https://www.vosviewer.com)).
*   **Accesos:** Credenciales de la Biblioteca Digital de la UANL (para acceso a Scopus/Web of Science y descarga de artículos en bases de datos).

---

## 📝 Lista de Cotejo de Contribución Doctoral (Para el Profesor)
Durante la clase, asegúrese de validar si los estudiantes comprendieron que:
* [ ] MCDM no busca una "verdad matemática única", sino estructurar un proceso de decisión para un decisor con preferencias específicas.
* [ ] No se permite usar métodos MCDM sin justificar por qué ese método y no otro (evitar el "síndrome del martillo de Maslow", donde a todo problema se le ve cara de clavo para darle con AHP).
* [ ] Los casos prácticos se centran en evaluar y comparar el comportamiento matemático de diferentes métodos sobre un mismo problema.
