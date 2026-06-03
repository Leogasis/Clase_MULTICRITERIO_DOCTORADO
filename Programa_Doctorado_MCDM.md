# PROGRAMA ANALÍTICO
## Herramientas Multicriterio para Toma de Decisiones

**Nivel:** Doctorado | **Modalidad:** Presencial | **Tetramestral**
*15 sesiones × 3 horas = 45 horas totales*  
**Área:** Investigación de Operaciones y Logística  
**Institución:** UANL – Facultad de Ingeniería Mecánica y Eléctrica (FIME)  
**Programa:** Doctorado en Logística  

---

### I. Datos Generales de la Materia

| Campo | Descripción |
| :--- | :--- |
| **Nombre de la materia** | Herramientas Multicriterio para Toma de Decisiones |
| **Programa** | Doctorado en Logística |
| **Unidad académica** | FIME – Universidad Autónoma de Nuevo León (UANL) |
| **Duración** | Tetramestral \| 15 sesiones × 3 horas = 45 horas |
| **Créditos** | 6 créditos (sujeto a tabla de créditos institucional) |
| **Prerrequisitos** | Estadística avanzada, Investigación de Operaciones, Seminario de investigación I |
| **Idioma** | Español (lectura obligatoria en inglés) |

---

### II. Descripción del Curso

Este curso de nivel doctoral profundiza en los fundamentos teóricos, matemáticos y metodológicos de los métodos de toma de decisiones multicriterio (MCDM/MADM), con énfasis en su aplicación rigurosa en problemas complejos de logística y cadena de suministro. A diferencia del nivel de especialidad, el enfoque doctoral integra la dimensión investigativa: el estudiante no solo aprende a aplicar métodos, sino a cuestionarlos, extenderlos y contribuir al avance del conocimiento científico.

A lo largo del tetramestre, el estudiante desarrollará un protocolo de investigación original que culmina en un artículo o anteproyecto de tesis, con potencial de publicación en revistas internacionales indexadas.

---

### III. Competencias a Desarrollar

#### Competencias Genéricas del Doctorado
- Capacidad de generación, aplicación y divulgación del conocimiento científico.
- Pensamiento crítico, analítico y reflexivo ante problemas de investigación.
- Comunicación científica oral y escrita en contextos de alto impacto.

#### Competencias Específicas de la Materia
- Dominar los fundamentos axiomáticos y matemáticos de los principales métodos MCDM.
- Seleccionar, justificar y aplicar métodos MCDM apropiados para problemas de logística complejos.
- Extender o adaptar métodos existentes incorporando incertidumbre (lógica difusa, conjuntos grises, rough sets).
- Diseñar estudios de caso con validez científica, análisis de sensibilidad y robustez.
- Articular los resultados de investigación bajo los estándares de publicación en revistas Q1/Q2.

---

### IV. Contenido Temático por Sesión

> [!NOTE]
> Las lecturas marcadas como **"Archivo disponible"** se encuentran organizadas en la carpeta [literatura](file:///Users/leonardohernandez/Academica/Clase_MULTICRITERIO_DOCTORADO/literatura); las marcadas como **"Biblioteca UANL / pendiente"** deben conseguirse por acceso institucional o pueden mantenerse como lectura recomendada.
>
> Cada sesión combina exposición teórica (~90 min), discusión de artículos científicos (~45 min) y actividad aplicada (~45 min).

#### Sesión 1: Fundamentos epistemológicos de la toma de decisiones multicriterio
* **Lecturas previas:**
  - **[Capítulo]** Figueira, J., Greco, S., & Ehrgott, M. (2016). *An overview of MCDM concepts and approaches*. En Multiple Criteria Decision Analysis (2nd ed., cap. 1, pp. 1–33). Springer. [S01_Figueira_Greco_Ehrgott_2016_Multiple_Criteria_Decision_Analysis_2nd_ed.pdf](file:///Users/leonardohernandez/Academica/Clase_MULTICRITERIO_DOCTORADO/literatura/libros/S01_Figueira_Greco_Ehrgott_2016_Multiple_Criteria_Decision_Analysis_2nd_ed.pdf)
  - **[Artículo]** Mardani, A., et al. (2015). *Multiple criteria decision-making techniques and their applications – a survey*. Economic Research, 28(1), 516–571. [S01_Mardani_et_al_2015_Multiple_criteria_decision_making_techniques_and_their_applications_survey.pdf](file:///Users/leonardohernandez/Academica/Clase_MULTICRITERIO_DOCTORADO/literatura/articulos/S01_Mardani_et_al_2015_Multiple_criteria_decision_making_techniques_and_their_applications_survey.pdf)
* **Guía de lectura:** Identifica al menos 3 debates epistemológicos en la literatura revisada. ¿Cómo se diferencia la ontología del MCDM respecto a la optimización clásica?
* **Temas de sesión:**
  - Paradigmas en la investigación de operaciones y ciencias de la decisión.
  - Revisión crítica de la literatura: state-of-the-art y análisis bibliométrico.
  - Diferencias entre MCDM y MADM: taxonomía actualizada.
  - Problemáticas en logística susceptibles de modelación multicriterio.
* **Actividad:** Mapeo bibliométrico con VOSviewer sobre una temática de logística elegida por el estudiante.

#### Sesión 2: Ponderación subjetiva de criterios: AHP (Saaty) y Best-Worst Method (BWM)
* **Lecturas previas:**
  - **[Artículo]** Rezaei, J. (2015). *Best-worst multi-criteria decision-making method*. Omega, 53, 49–57. [S03_Rezaei_2015_Best_worst_multi_criteria_decision_making_method.pdf](file:///Users/leonardohernandez/Academica/Clase_MULTICRITERIO_DOCTORADO/literatura/articulos/S03_Rezaei_2015_Best_worst_multi_criteria_decision_making_method.pdf)
  - **[Capítulo]** Saaty, T. L. (1980). *The Analytic Hierarchy Process* (capítulos seleccionados sobre axiomas y escalas). McGraw-Hill.
* **Guía de lectura:** ¿Por qué el Best-Worst Method (BWM) requiere un menor número de comparaciones en comparación con el AHP clásico ($2n - 3$ frente a $n(n-1)/2$)? ¿Cuál es la mayor crítica matemática que Dyer (1990) le hace al AHP clásico?
* **Temas de sesión:**
  - Axiomas del AHP de Saaty: reciprocidad, homogeneidad, dependencia y expectativas.
  - El debate sobre Rank Reversal (Inversión de Rangos): polémica Dyer vs. Saaty.
  - El algoritmo de Best-Worst Method (BWM): formulación matemática minimax lineal.
  - Elicitación de pesos subjetivos y consistencia analítica.
* **Actividad:** Cálculo manual de consistencia AHP y resolución del modelo BWM en Python/Excel para selección de transportista LTL.

#### Sesión 3: Ponderación objetiva de criterios: Entropía de Shannon, CRITIC y MEREC
* **Lecturas previas:**
  - **[Artículo]** Diakoulaki, D., Mavrotas, G., & Papayannakis, L. (1995). *Determining objective weights in multiple criteria problems: the CRITIC method*. Computers & Operations Research, 22(7), 763–770. `[Biblioteca UANL / pendiente de archivo local]`
  - **[Artículo]** Keshavarz-Ghorabaee, M., et al. (2021). *Determination of Objective Weights Using a New Method Based on the Removal Effects of Criteria (MEREC)*. Symmetry, 13(4), 525. [S08_Keshavarz_Ghorabaee_et_al_2021_Determination_of_Objective_Weights_Using_MEREC.pdf](file:///Users/leonardohernandez/Academica/Clase_MULTICRITERIO_DOCTORADO/literatura/articulos/S08_Keshavarz_Ghorabaee_et_al_2021_Determination_of_Objective_Weights_Using_MEREC.pdf)
* **Guía de lectura:** ¿Qué diferencias filosóficas existen entre determinar pesos de forma subjetiva vs. objetiva? ¿Cómo resuelve CRITIC la redundancia entre criterios correlacionados?
* **Temas de sesión:**
  - La señal de la información en los datos: entropía de Shannon.
  - Método CRITIC: desviación estándar y correlación lineal (Pearson).
  - Método MEREC (Removal Effects of Criteria) y ponderación por exclusión.
  - Integración de pesos subjetivos-objetivos en logística de almacenes.
* **Actividad:** Cálculo de pesos de Entropía y CRITIC en Python para dataset de KPIs de bodegas y contraste de resultados.

#### Sesión 4: Paradigma de distancia geométrica: TOPSIS, VIKOR y variantes
* **Lecturas previas:**
  - **[Lectura alternativa OA]** *A comparative case study of the VIKOR and TOPSIS rankings similarity*. Procedia Computer Science (2020). [S05_Comparative_Case_Study_VIKOR_TOPSIS_Rankings_Similarity_2020.pdf](file:///Users/leonardohernandez/Academica/Clase_MULTICRITERIO_DOCTORADO/literatura/articulos/S05_Comparative_Case_Study_VIKOR_TOPSIS_Rankings_Similarity_2020.pdf)
  - **[Lectura complementaria OA]** *Comparative analyses of multi-criteria methods in supplier selection problem*. Procedia Computer Science, 207 (2022), 4593–4602. [S05_Comparative_Analyses_MCDM_Methods_Supplier_Selection_2022.pdf](file:///Users/leonardohernandez/Academica/Clase_MULTICRITERIO_DOCTORADO/literatura/articulos/S05_Comparative_Analyses_MCDM_Methods_Supplier_Selection_2022.pdf)
* **Guía de lectura:** ¿Cuál es la diferencia en la métrica de distancia de Minkowski ($L_p$) utilizada por TOPSIS ($p=2$) frente a VIKOR ($p=1$ y $p=\infty$)?
* **Temas de sesión:**
  - Concepto de compromiso y distancias a puntos ideales y anti-ideales.
  - Algoritmo TOPSIS: normalización vectorial y coeficiente de proximidad relativa.
  - Algoritmo VIKOR: utilidad de grupo ($S_i$), arrepentimiento individual ($R_i$) y estabilidad aceptable.
  - Validación de concordancia de rankings (coeficientes de Spearman y Kendall).
* **Actividad:** Implementación de TOPSIS y VIKOR en Python para localización de micro-hubs urbanos de última milla.
* **Entregable:** **E1 — Caso Práctico 1: Ponderación de Criterios (AHP, BWM y Entropía)**

#### Sesión 5: Paradigma de superación (Outranking): ELECTRE y PROMETHEE
* **Lecturas previas:**
  - **[Artículo clásico]** Brans, J. P., & Vincke, P. (1985). *A preference ranking organisation method*. Management Science, 31(6), 647–656. [S04_Brans_Vincke_1985_Preference_Ranking_Organisation_Method_PROMETHEE.pdf](file:///Users/leonardohernandez/Academica/Clase_MULTICRITERIO_DOCTORADO/literatura/articulos/S04_Brans_Vincke_1985_Preference_Ranking_Organisation_Method_PROMETHEE.pdf)
  - **[Lectura alternativa OA]** Wang, Z., & Rangaiah, G. P. (2025). *Multi-Criteria Decision-Making: Outranking-Type Methods*. [S04_Wang_Rangaiah_2025_Outranking_Type_Methods_ELECTRE_PROMETHEE.pdf](file:///Users/leonardohernandez/Academica/Clase_MULTICRITERIO_DOCTORADO/literatura/articulos/S04_Wang_Rangaiah_2025_Outranking_Type_Methods_ELECTRE_PROMETHEE.pdf)
* **Guía de lectura:** ¿Cuál es el significado del veto en ELECTRE y cómo puede aplicarse a una restricción de emisiones en logística? Describe las funciones de preferencia de PROMETHEE.
* **Temas de sesión:**
  - Ayuda a la decisión no compensatoria: filosofía de Bernard Roy y conmensurabilidad.
  - Métodos ELECTRE (I, II, III): matrices de concordancia, discordancia y vetos.
  - Métodos PROMETHEE (I y II): flujos positivos ($\Phi^+$), negativos ($\Phi^-$) y flujos netos ($\Phi$).
  - Visualización del plano GAIA y análisis de relaciones de dominancia.
* **Actividad:** Comparación de alternativas de flota verde en Python usando `pyDecision` con umbrales de veto.

#### Sesión 6: Teoría de la utilidad multiatributo (MAUT) y decisiones bajo riesgo
* **Lecturas previas:**
  - **[Capítulo]** Keeney, R. L., & Raiffa, H. (1993). *Decisions with Multiple Objectives* (cap. 3 y 5). Cambridge University Press. `[Biblioteca UANL / pendiente de archivo local]`
  - **[Capítulo]** Dyer, J. S. (2005). *MAUT – Multiattribute utility theory*. En Multiple Criteria Decision Analysis (pp. 265–292). Springer. [S02_Dyer_2005_in_Figueira_Greco_Ehrgott_2005_Multiple_Criteria_Decision_Analysis_1st_ed.pdf](file:///Users/leonardohernandez/Academica/Clase_MULTICRITERIO_DOCTORADO/literatura/libros/S02_Dyer_2005_in_Figueira_Greco_Ehrgott_2005_Multiple_Criteria_Decision_Analysis_1st_ed.pdf)
* **Guía de lectura:** Analiza los supuestos de independencia preferencial e independencia de utilidad. ¿En qué situaciones de logística real podrían violarse?
* **Temas de sesión:**
  - Axiomas de Von Neumann-Morgenstern y comportamiento frente al riesgo.
  - Funciones de utilidad exponenciales y el coeficiente de aversión de Pratt-Arrow.
  - Modelos aditivos vs. multiplicativos (ecuación de Keeney-Raiffa).
  - Elicitación de curvas de utilidad mediante equivalentes de certeza.
* **Actividad:** Modelado en Python de la constante $k$ y evaluación de proveedores bajo riesgo.
* **Entregable:** **E2 — Caso Práctico 2: Jerarquización por Distancia (TOPSIS vs. VIKOR)**

#### Sesión 7: Lógica difusa y conjuntos difusos en MCDM: Fuzzy AHP y Fuzzy TOPSIS
* **Lecturas previas:**
  - **[Artículo fundacional]** Zadeh, L. A. (1965). *Fuzzy sets*. Information and Control, 8(3), 338–353. [S06_Zadeh_1965_Fuzzy_sets.pdf](file:///Users/leonardohernandez/Academica/Clase_MULTICRITERIO_DOCTORADO/literatura/articulos/S06_Zadeh_1965_Fuzzy_sets.pdf)
  - **[Lectura alternativa OA]** Tronnebati, I., El Yadari, M., & Jawab, F. (2022). *A Review of Green Supplier Evaluation and Selection Issues Using MCDM, MP and AI Models*. Sustainability, 14(24), 16714. [S06_Tronnebati_El_Yadari_Jawab_2022_Green_Supplier_Evaluation_Selection_Review.pdf](file:///Users/leonardohernandez/Academica/Clase_MULTICRITERIO_DOCTORADO/literatura/articulos/S06_Tronnebati_El_Yadari_Jawab_2022_Green_Supplier_Evaluation_Selection_Review.pdf)
* **Guía de lectura:** ¿Por qué la lógica difusa es especialmente adecuada para modelar variables cualitativas lingüísticas de expertos en la cadena de suministro?
* **Temas de sesión:**
  - Conjuntos difusos: funciones de membresía y Números Difusos Triangulares (TFNs).
  - Aritmética de TFNs y variables lingüísticas de decisión.
  - Algoritmo Fuzzy TOPSIS (Chen) y Fuzzy AHP (Chang).
  - Métodos de defuzzificación (Centroide / BNP).
* **Actividad:** Implementación de Fuzzy TOPSIS en Python para evaluar riesgos en puertos internacionales.

#### Sesión 8: MCDM bajo incertidumbre: teoría de sistemas grises (GRA) y conjuntos aproximados (Rough Sets)
* **Lecturas previas:**
  - **[Lectura alternativa OA]** Wei, G. W., Wang, H. J., Lin, R., & Zhao, X. F. (2011). *Grey relational analysis method for intuitionistic fuzzy multiple attribute decision making with preference information on alternatives*. IJCNN, 4(2), 164–173. [S07_Wei_Wang_Lin_Zhao_2011_GRA_Intuitionistic_Fuzzy_MADM_Preference_Info.pdf](file:///Users/leonardohernandez/Academica/Clase_MULTICRITERIO_DOCTORADO/literatura/articulos/S07_Wei_Wang_Lin_Zhao_2011_GRA_Intuitionistic_Fuzzy_MADM_Preference_Info.pdf)
  - **[Artículo]** Pawlak, Z. (1982). *Rough sets*. International Journal of Computer & Information Sciences, 11(5), 341–356. [S07_Pawlak_1982_Rough_sets.pdf](file:///Users/leonardohernandez/Academica/Clase_MULTICRITERIO_DOCTORADO/literatura/articulos/S07_Pawlak_1982_Rough_sets.pdf)
* **Guía de lectura:** ¿En qué escenarios de logística tiene ventaja el enfoque de números grises frente a los métodos probabilísticos y difusos?
* **Temas de sesión:**
  - Concepto de información gris y el algoritmo de Grey Relational Analysis (GRA).
  - Coeficiente de relación gris (GRC) y Grado de relación gris (GRG).
  - Teoría de Conjuntos Aproximados (Rough Sets): indiscernibilidad y tablas de decisión.
  - Reducción de atributos sin pérdida de poder de clasificación.
* **Actividad:** Clasificación multicriterio de SKUs de inventario (ABC) en Excel/Python utilizando GRA.
* **Entregable:** **E3 — Caso Práctico 3: Relaciones de Superación (ELECTRE vs. PROMETHEE)** (e inicio del PIA)

#### Sesión 9: Métodos de nueva generación: MARCOS, EDAS, CODAS y CoCoSo
* **Lecturas previas:**
  - **[Lectura alternativa OA]** Wang, C.-N., Nguyen, T. T. T., Dang, T.-T., & Nguyen, N.-A.-T. (2022). *A Hybrid OPA and Fuzzy MARCOS Methodology for Sustainable Supplier Selection with Technology 4.0 Evaluation*. Processes, 10(11), 2351. [S09_Wang_Nguyen_Dang_Nguyen_2022_OPA_Fuzzy_MARCOS_Sustainable_Supplier_I40.pdf](file:///Users/leonardohernandez/Academica/Clase_MULTICRITERIO_DOCTORADO/literatura/articulos/S09_Wang_Nguyen_Dang_Nguyen_2022_OPA_Fuzzy_MARCOS_Sustainable_Supplier_I40.pdf)
  - **[Artículo]** Keshavarz Ghorabaee, M., et al. (2015). *Multi-criteria inventory classification using a new method of evaluation based on distance from average solution (EDAS)*. Informatica, 26(3), 435–451. [S09_Keshavarz_Ghorabaee_et_al_2015_EDAS_Evaluation_based_on_Distance_from_Average_Solution.pdf](file:///Users/leonardohernandez/Academica/Clase_MULTICRITERIO_DOCTORADO/literatura/articulos/S09_Keshavarz_Ghorabaee_et_al_2015_EDAS_Evaluation_based_on_Distance_from_Average_Solution.pdf)
* **Guía de lectura:** ¿Por qué EDAS usa la solución promedio en lugar de extremos? ¿Cómo reduce esto el impacto de los outliers?
* **Temas de sesión:**
  - Algoritmo EDAS: distancias PDA y NDA y normalización al promedio.
  - Algoritmo MARCOS: extensión con alternativas de referencia ideal e ideal negativa.
  - Métodos CoCoSo y CODAS: lógicas combinativas y de distancia en logística.
  - Consistencia y robustez ante rank reversal en algoritmos de nueva generación.
* **Actividad:** Comparación en Python de EDAS y TOPSIS en selección de software WMS con datos atípicos.

#### Sesión 10: Decisión multicriterio grupal (GDMCDM) y consenso
* **Lecturas previas:**
  - **[Lectura alternativa OA]** *Soft consensus cost models for group decision making and economic interpretations*. European Journal of Operational Research, 277(3), 964–980. [S10_Soft_Consensus_Cost_Models_Group_Decision_Making_2019.pdf](file:///Users/leonardohernandez/Academica/Clase_MULTICRITERIO_DOCTORADO/literatura/articulos/S10_Soft_Consensus_Cost_Models_Group_Decision_Making_2019.pdf)
  - **[Artículo]** Palomares, I., Martinez, L., & Herrera, F. (2014). *A consensus model to detect and manage noncooperative behaviors in large-scale group decision making*. IEEE Transactions on Fuzzy Systems, 22(3), 516–530. `[IEEE Xplore / pendiente de archivo local]`
* **Guía de lectura:** ¿Cómo podrían manifestarse los comportamientos no-cooperativos en un comité de licitación logística y cómo se manejan?
* **Temas de sesión:**
  - Agregación de preferencias individuales: operadores OWA y medias geométricas.
  - Medición del disenso e índices de similitud grupal.
  - Modelos matemáticos de costo de consenso suave (Soft Consensus Cost).
  - Integración Delphi-MCDM para paneles de expertos.
* **Actividad:** Simulación de licitación de flotas de camiones pesados usando operadores de agregación grupal en Python.

#### Sesión 11: Integración MCDM con optimización y modelos híbridos
* **Lecturas previas:**
  - **[Artículo]** Deb, K., et al. (2002). *A fast and elitist multiobjective genetic algorithm: NSGA-II*. IEEE TEVC, 6(2), 182–197. [S11_Deb_et_al_2002_A_fast_and_elitist_multiobjective_genetic_algorithm_NSGA_II.pdf](file:///Users/leonardohernandez/Academica/Clase_MULTICRITERIO_DOCTORADO/literatura/articulos/S11_Deb_et_al_2002_A_fast_and_elitist_multiobjective_genetic_algorithm_NSGA_II.pdf)
  - **[Lectura alternativa OA]** Awasthi, A., Chauhan, S. S., & Goyal, S. K. (2012). *A hybrid approach integrating Affinity Diagram, AHP and fuzzy TOPSIS for sustainable city logistics planning*. Applied Mathematical Modelling, 36(2), 573–584. [S11_AHP_Fuzzy_TOPSIS_Sustainable_City_Logistics_Planning_2012.pdf](file:///Users/leonardohernandez/Academica/Clase_MULTICRITERIO_DOCTORADO/literatura/articulos/S11_AHP_Fuzzy_TOPSIS_Sustainable_City_Logistics_Planning_2012.pdf)
* **Guía de lectura:** ¿Cómo garantiza la crowding distance la diversidad en la frontera de Pareto? ¿Cuándo tiene sentido metodológico hibridar optimización y MCDM?
* **Temas de sesión:**
  - Optimización multiobjetivo (MODM) frente a toma de decisiones multiatributo (MADM).
  - Algoritmo genético evolutivo NSGA-II: fast non-dominated sort y elitismo.
  - Metodologías de hibridación MODM + MADM: selección de soluciones de compromiso en la frontera de Pareto.
  - Diseño de redes de distribución bi-objetivo (costo vs. lead time).
* **Actividad:** Ejecución de NSGA-II en Python y filtrado de soluciones mediante TOPSIS.
* **Entregable:** **E4 — Caso Práctico 4: Lógica Difusa e Incertidumbre (Fuzzy / Sistemas Grises)**

#### Sesión 12: MCDM con datos masivos, machine learning e inteligencia artificial
* **Lecturas previas:**
  - **[Artículo]** Doumpos, M., & Figueira, J. R. (2019). *Learning approaches to criteria weights in MCDM: a literature review*. Omega, 84, 176–194. `[Biblioteca UANL / pendiente de archivo local]`
  - **[Artículo]** Arrieta, A. B., et al. (2020). *Explainable Artificial Intelligence (XAI): Concepts, taxonomies, opportunities and challenges toward responsible AI*. Information Fusion, 58, 82–115. [S12_Arrieta_et_al_2020_Explainable_Artificial_Intelligence_XAI.pdf](file:///Users/leonardohernandez/Academica/Clase_MULTICRITERIO_DOCTORADO/literatura/articulos/S12_Arrieta_et_al_2020_Explainable_Artificial_Intelligence_XAI.pdf)
* **Guía de lectura:** ¿Cómo cambia el rol del experto cuando los pesos de los criterios se aprenden automáticamente? ¿Qué implicaciones éticas y prácticas tiene esto en decisiones logísticas de alto impacto?
* **Temas de sesión:**
  - Data-driven MCDM: aprendizaje de preferencias con ML.
  - Clustering y clasificación para reducción de alternativas.
  - Explainable AI (XAI) y toma de decisiones transparente.
  - Aplicaciones: predicción de disrupciones y decisiones en tiempo real.
* **Actividad:** Revisión sistemática de literatura MCDM + AI en logística (últimos 5 años).

#### Sesión 13: Sostenibilidad, logística verde y MCDM
* **Lecturas previas:**
  - **[Lectura alternativa OA]** Banaeian, N., et al. (2017). *Green Supplier Evaluation and Selection in Apparel Manufacturing Using a Fuzzy Multi-Criteria Decision-Making Approach*. Sustainability, 9(4), 650. [S13_Green_Supplier_Evaluation_Selection_Apparel_Fuzzy_MCDM_2017.pdf](file:///Users/leonardohernandez/Academica/Clase_MULTICRITERIO_DOCTORADO/literatura/articulos/S13_Green_Supplier_Evaluation_Selection_Apparel_Fuzzy_MCDM_2017.pdf)
  - **[Lectura alternativa OA]** Zhou, X., & Xu, Z. (2018). *An Integrated Sustainable Supplier Selection Approach Based on Hybrid Information Aggregation*. Sustainability, 10(7), 2543. [S13_Zhou_Xu_2018_Integrated_Sustainable_Supplier_Selection_Hybrid_Info_Aggregation.pdf](file:///Users/leonardohernandez/Academica/Clase_MULTICRITERIO_DOCTORADO/literatura/articulos/S13_Zhou_Xu_2018_Integrated_Sustainable_Supplier_Selection_Hybrid_Info_Aggregation.pdf)
* **Guía de lectura:** ¿Cómo operacionalizan los autores el concepto de 'triple bottom line' como criterios MCDM? ¿Qué tensiones identificas entre los criterios económicos y ambientales en los casos estudiados?
* **Temas de sesión:**
  - Triple bottom line: indicadores económicos, ambientales y sociales en MCDM.
  - Green Supplier Selection: revisión de la literatura y mejores prácticas.
  - Life Cycle Assessment (LCA) integrado con MCDM.
  - Objetivos de Desarrollo Sostenible (ODS) como criterios de evaluación.
* **Actividad:** Diseño de marco MCDM para evaluación de sostenibilidad en un caso de logística inversa.

#### Sesión 14: Validación, robustez y replicabilidad en investigación MCDM
* **Lecturas previas:**
  - **[Artículo metodológico]** Saltelli, A., et al. (2019). *Why so many published sensitivity analyses are false: A systematic review of sensitivity analysis practices*. Environmental Modelling & Software, 114, 29–39. [S14_Saltelli_et_al_2019_Why_so_many_published_sensitivity_analyses_are_false.pdf](file:///Users/leonardohernandez/Academica/Clase_MULTICRITERIO_DOCTORADO/literatura/articulos/S14_Saltelli_et_al_2019_Why_so_many_published_sensitivity_analyses_are_false.pdf)
  - **[Artículo]** Cinelli, M., et al. (2022). *Proper and improper uses of MCDA methods in energy systems analysis*. Decision Support Systems, 163, 113848. [S14_Cinelli_et_al_2022_Proper_and_improper_uses_of_MCDA_methods_in_energy_systems_analysis.pdf](file:///Users/leonardohernandez/Academica/Clase_MULTICRITERIO_DOCTORADO/literatura/articulos/S14_Cinelli_et_al_2022_Proper_and_improper_uses_of_MCDA_methods_in_energy_systems_analysis.pdf)
* **Guía de lectura:** Según Saltelli et al., ¿cuáles son los errores más frecuentes en análisis de sensibilidad? Aplica este checklist crítico a uno de tus avances previos del protocolo de investigación.
* **Temas de sesión:**
  - Análisis de sensibilidad avanzado: Monte Carlo, coeficiente de variación de Delphi.
  - Validación cruzada de rankings: índices de concordancia.
  - Reproducibilidad de resultados: datos abiertos y código abierto.
  - Checklist de calidad para publicación en revistas de alto impacto (JEL, EJOR, Omega).
* **Actividad:** Revisión por pares del protocolo de investigación de un compañero con formato referee.

#### Sesión 15: Presentaciones finales y retroalimentación académica
* **Lecturas previas:**
  - **[Guía]** Sharma, D. K., et al. (2021). *How to write a good research paper: a guide for MCDM researchers*. Journal of Decision Systems, 30(2–3), 1–15. `[Taylor & Francis / pendiente de archivo local]`
  - **[Recurso]** Guía de autores de European Journal of Operational Research (EJOR). [S15_European_Journal_of_Operational_Research_guide_for_authors.url.txt](file:///Users/leonardohernandez/Academica/Clase_MULTICRITERIO_DOCTORADO/literatura/guias/S15_European_Journal_of_Operational_Research_guide_for_authors.url.txt)
  - **[Recurso]** Guía de autores de Computers & Industrial Engineering. [S15_Computers_Industrial_Engineering_guide_for_authors.url.txt](file:///Users/leonardohernandez/Academica/Clase_MULTICRITERIO_DOCTORADO/literatura/guias/S15_Computers_Industrial_Engineering_guide_for_authors.url.txt)
* **Guía de lectura:** Revisa la guía de autores de EJOR. ¿Tu protocolo actual cumple con los lineamientos de estructura, extensión y estilo? Identifica tres mejoras concretas antes de la presentación.
* **Temas de sesión:**
  - Presentación de proyectos finales (formato congreso: 15 min + 5 min preguntas).
  - Retroalimentación estructurada: rúbrica de evaluación académica.
  - Discusión: agenda de investigación futura en MCDM y logística.
  - Cierre: publicación, difusión y extensión de los proyectos.
* **Actividad:** Defensa del proyecto de investigación ante panel evaluador.
* **Entregable:** **E5 — Producto Integrador de Aprendizaje (PIA)**

---

### V. Sistema de Evaluación: Casos Prácticos y Producto Integrador (PIA)

Las evidencias del curso combinan el rigor práctico-numérico (Casos Prácticos E1 a E4) con la producción científica de nivel doctoral (E5 - PIA). Los casos prácticos permiten dominar la implementación matemática de los algoritmos en logística, sirviendo como andamiaje y validación para el Producto Integrador de Aprendizaje (PIA), el cual consiste en redactar y defender un manuscrito científico apto para publicación en una revista internacional indexada (Q1/Q2).

| Evidencia | Peso | Entrega | Componente Evaluado |
| :--- | :---: | :---: | :--- |
| **E1** — Caso Práctico 1: Ponderación de Criterios (AHP, BWM y Entropía) | 15% | Sesión 4 | Cálculo y comparación de pesos subjetivos y objetivos |
| **E2** — Caso Práctico 2: Jerarquización por Distancia (TOPSIS vs. VIKOR) | 20% | Sesión 6 | Modelado geométrico y contraste de rankings de compromiso |
| **E3** — Caso Práctico 3: Relaciones de Superación (ELECTRE vs. PROMETHEE) | 20% | Sesión 8 | Modelado no compensatorio con umbrales y incomparabilidad |
| **E4** — Caso Práctico 4: Lógica Difusa e Incertidumbre (Fuzzy / Sistemas Grises) | 15% | Sesión 11 | Tratamiento formal de vaguedad y datos incompletos |
| **E5** — Producto Integrador de Aprendizaje (PIA): Artículo y Defensa | 30% | Sesión 15 | Artículo científico completo (estructura IMRyD) + Defensa oral |
| **TOTAL** | **100%** | | **1 artículo indexado co-autorado + Dominio práctico** |

#### Descripción Detallada de Cada Evidencia

* **E1 | Caso Práctico 1: Ponderación de Criterios**
  * **¿Qué es?** Aplicación comparativa de métodos subjetivos (AHP/BWM) y objetivos (Entropía) sobre un problema real de selección de transportistas LTL.
  * **Formato:** Reporte de cálculo (3-4 pp.) + Script de Python / Excel reproducible.
  * **Enfoque Doctoral:** Discusión sobre la validez axiomática del AHP, el debate Dyer-Saaty, e inconsistencias en juicios subjetivos vs. señales de datos.
* **E2 | Caso Práctico 2: Jerarquización por Distancia**
  * **¿Qué es?** Modelado geométrico del problema de localización de micro-hubs urbanos usando TOPSIS y VIKOR.
  * **Formato:** Reporte técnico de modelado (4-5 pp.) + Código en Python + Análisis de concordancia (Spearman).
  * **Enfoque Doctoral:** Justificación matemática de la elección de la métrica $L_p$ y análisis de robustez al variar el parámetro de mayoría $v$.
* **E3 | Caso Práctico 3: Relaciones de Superación**
  * **¿Qué es?** Modelado no compensatorio de aprovisionamiento verde con veto estricto por huella de carbono mediante ELECTRE y PROMETHEE.
  * **Formato:** Reporte técnico y digrafos de outranking + Script en Python (`pyDecision`).
  * **Enfoque Doctoral:** Justificación de la incomparabilidad y de los umbrales de veto en contextos logísticos Just-in-Time.
* **E4 | Caso Práctico 4: Lógica Difusa e Incertidumbre**
  * **¿Qué es?** Evaluación de riesgo en puertos internacionales bajo vaguedad lingüística empleando Fuzzy TOPSIS o GRA.
  * **Formato:** Reporte y código de defuzzificación + Análisis comparativo.
  * **Enfoque Doctoral:** Formalización del modelado cualitativo frente a aproximaciones de variables lingüísticas estructuradas.
* **E5 | Producto Integrador de Aprendizaje (PIA)**
  * **¿Qué es?** Un artículo de investigación científica original que aplique la hibridación de métodos MCDM a un problema real de la tesis doctoral del estudiante o de logística avanzada, complementado con análisis de sensibilidad global (checklist de Saltelli) y validación cruzada.
  * **Formato:** Manuscrito estructurado en formato IMRyD según guía de autores de revista Q1/Q2 (8,000–10,000 palabras) + Defensa en formato ponencia (15 min + 5 min preguntas).
  * **Enfoque Doctoral:** Aporte científico original, validación matemática de robustez y justificación de selección metodológica.

#### Escala de Calificación
- **Excelente:** 90–100
- **Muy Bien:** 80–89
- **Suficiente:** 70–79
- **Insuficiente:** < 70

---

### VI. Metodología de Enseñanza-Aprendizaje

El curso emplea una pedagogía activa orientada a la producción científica:
- Exposición magistral con discusión socrática de fundamentos teóricos.
- *Flipped classroom*: lectura previa de artículos científicos asignados.
- Aprendizaje basado en problemas (ABP) con casos reales de logística.
- Revisión por pares: los estudiantes evalúan avances de sus compañeros con criterios académicos.
- Talleres de software: Python (`scikit-criteria`, `pyDecision`), Excel avanzado, VOSviewer.
- Seminario de investigación integrado: cada actividad alimenta el protocolo final.
- *Se espera que el estudiante dedique al menos 4 horas de trabajo autónomo por sesión (lectura, programación, redacción).*

---

### VII. Bibliografía y Recursos

#### Bibliografía Obligatoria
- Hwang, C. L., & Yoon, K. (1981). *Multiple Attribute Decision Making*. Springer.
- Saaty, T. L. (1980). *The Analytic Hierarchy Process*. McGraw-Hill.
- Figueira, J., Greco, S., & Ehrgott, M. (Eds.) (2016). *Multiple Criteria Decision Analysis: State of the Art Surveys* (2nd ed.). Springer.
- Zavadskas, E. K., et al. (2019). *Decision Making Methods and Applications*. MDPI.
- Stević, Ž., et al. (2020). *Sustainable supplier selection in healthcare industries using a new MCDM method: Measurement of Alternatives and Ranking according to COmpromise Solution (MARCOS)*. Computers & Industrial Engineering, 140.
- Rezaei, J. (2015). *Best-worst multi-criteria decision-making method*. Omega, 53, 49–57.

#### Bibliografía Complementaria
- Keshavarz Ghorabaee, M., et al. (2015). *Multi-criteria inventory classification using a new method of evaluation based on distance from average solution (EDAS)*. Informatica, 26(3), 435–451.
- Mardani, A., et al. (2020). *A systematic review and meta-analysis of SWARA and WASPAS methods*. Applied Soft Computing, 96.
- Çalı, S., & Balaman, Ş. Y. (2019). *A novel outranking based multi criteria group decision making methodology integrating ELECTRE and VIKOR under intuitionistic fuzzy environment*. Expert Systems with Applications, 119, 36–50.
- **Revistas recomendadas:** European Journal of Operational Research (EJOR), Omega, Expert Systems with Applications, Computers & Industrial Engineering.

#### Bases de Datos y Recursos Digitales
- **Web of Science / Scopus:** búsqueda bibliométrica de MCDM en logística.
- **Google Scholar + Publish or Perish:** análisis de impacto.
- **ScienceDirect y SpringerLink:** acceso a artículos del área.
- **Repositorio PyPI:** librerías `pyDecision`, `scikit-criteria` para implementación en Python.
- **Software recomendado:** DecisionLab (PROMETHEE/GAIA), Super Decisions (ANP), Python/Jupyter.

---

### VIII. Cronograma Tentativo del Tetramestre

| Sesión | Tema Principal | Actividad | Entregable |
| :---: | :--- | :--- | :---: |
| **1** | Fundamentos epistemológicos de la toma de decisiones | Mapeo bibliométrico con VOSviewer sobre temática de logística | — |
| **2** | Ponderación subjetiva de criterios: AHP y Best-Worst Method (BWM) | Cálculo manual de consistencia AHP y resolución del modelo BWM en Python/Excel | — |
| **3** | Ponderación objetiva de criterios: Entropía de Shannon, CRITIC y MEREC | Cálculo de pesos de Entropía y CRITIC en Python para dataset de KPIs | — |
| **4** | Paradigma de distancia geométrica: TOPSIS, VIKOR y variantes | Implementación de TOPSIS y VIKOR en Python para localización de micro-hubs | **E1** |
| **5** | Paradigma de superación (Outranking): ELECTRE y PROMETHEE | Comparación de alternativas de flota verde en Python usando pyDecision | — |
| **6** | Teoría de la utilidad multiatributo (MAUT) y decisiones bajo riesgo | Modelado en Python de la constante k y evaluación de proveedores bajo riesgo | **E2** |
| **7** | Lógica difusa y conjuntos difusos en MCDM: Fuzzy AHP y Fuzzy TOPSIS | Implementación de Fuzzy TOPSIS en Python para evaluar riesgos en puertos | — |
| **8** | MCDM bajo incertidumbre: teoría de sistemas grises (GRA) y conjuntos aproximados (Rough Sets) | Clasificación de SKUs de inventario (ABC) en Excel/Python utilizando GRA | **E3** |
| **9** | Métodos de nueva generación: MARCOS, EDAS, CODAS y CoCoSo | Comparación en Python de EDAS y TOPSIS en selección de software WMS | — |
| **10** | Decisión multicriterio grupal (GDMCDM) y consenso | Simulación de licitación de flotas de camiones pesados en Python | — |
| **11** | Integración MCDM con optimización y modelos híbridos | Ejecución de NSGA-II en Python y filtrado de soluciones mediante TOPSIS | **E4** |
| **12** | MCDM con datos masivos, machine learning e IA | Análisis bibliométrico del estado del arte en Big Data-MCDM | — |
| **13** | Sostenibilidad, logística verde y MCDM | Diseño de un modelo MCDM integral de economía circular | — |
| **14** | Validación, robustez y replicabilidad en investigación | Revisión por pares de la metodología del manuscrito del PIA | — |
| **15** | Presentaciones finales y retroalimentación académica | Defensa oral del artículo científico desarrollado durante el curso | **E5** |

---

### IX. Consideraciones Éticas y Académicas

- Toda la producción escrita deberá ser original; el uso de IA generativa debe declararse explícitamente.
- Los datos utilizados en los casos de estudio deben citarse adecuadamente o anonimizarse si son confidenciales.
- Las revisiones por pares se realizarán bajo principios de confidencialidad y respeto académico.
- El protocolo de investigación puede convertirse en el capítulo metodológico de la tesis doctoral.

---
*FIME – UANL | Doctorado en Logística | Herramientas Multicriterio para Toma de Decisiones*  
*Programa sujeto a ajustes según avance del grupo y líneas de investigación activas.*
