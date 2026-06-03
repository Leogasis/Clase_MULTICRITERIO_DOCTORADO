# Revision de literatura y recomendaciones

Fecha de revision: 2026-05-22

## 1. Organizacion aplicada

Reorganicé la carpeta `literatura` en:

- `articulos/`: PDFs de articulos.
- `libros/`: libros completos o handbooks.
- `guias/`: enlaces oficiales de guias de autores.
- `reportes/`: este reporte y notas de curaduria.

Archivos nuevos identificados y renombrados:

- `libros/S01_Figueira_Greco_Ehrgott_2016_Multiple_Criteria_Decision_Analysis_2nd_ed.pdf`
  - Libro Springer 2016, segunda edicion. Cubre la Sesion 1, capitulo "An overview of MCDM concepts and approaches".
- `libros/S02_Dyer_2005_in_Figueira_Greco_Ehrgott_2005_Multiple_Criteria_Decision_Analysis_1st_ed.pdf`
  - Libro Springer 2005, primera edicion. Cubre la lectura de Dyer (2005) sobre MAUT.
- `articulos/S04_Brans_Vincke_1985_Preference_Ranking_Organisation_Method_PROMETHEE.pdf`
  - Articulo clasico de Brans & Vincke (1985), Management Science.

Estado actualizado: 15 de 31 lecturas cubiertas. El inventario principal queda en `literatura/INVENTARIO.md` y `literatura/inventario.csv`.

## 2. Lecturas no encontradas y posibles reemplazos

El criterio usado fue conservar la intencion pedagogica de cada sesion: si la lectura cerrada es fundacional, recomiendo conseguirla por biblioteca; si existe una alternativa abierta que cubre bien la misma funcion didactica, propongo intercambio.

| Sesion | Lectura no disponible | Recomendacion | Reemplazo abierto sugerido | Justificacion |
|---:|---|---|---|---|
| 2 | Keeney & Raiffa (1993), capitulos 3 y 5 | No sustituir si se puede conseguir por biblioteca | Belton & Stewart (2002), *Multiple Criteria Decision Analysis: An Integrated Approach*, caps. de modelacion de preferencias. Springer: https://link.springer.com/book/10.1007/978-1-4615-1495-4 | Keeney & Raiffa es la base axiomatica de MAUT. Belton & Stewart sirve como apoyo didactico, pero no lo reemplaza totalmente. |
| 3 | Dyer (1990) y respuesta de Saaty (1990) | Sustituir solo si no hay acceso institucional | Saaty (2007), "Criticisms of the Analytic Hierarchy Process: Why they often make no sense", open archive: https://www.sciencedirect.com/science/article/pii/S0895717707001033 + Munier & Hontoria / rank reversal moderno, por ejemplo: https://www.sciencedirect.com/science/article/pii/S2214716021000087 | Mantiene el debate critico sobre AHP, especialmente rank reversal, consistencia y supuestos de modelacion. |
| 4 | Govindan & Jepsen (2016), revision ELECTRE | Intercambiable | Wang & Rangaiah (2025), "Multi-Criteria Decision-Making: Outranking-Type Methods", SSRN PDF: https://papers.ssrn.com/sol3/Delivery.cfm/5614710.pdf?abstractid=5614710&mirid=1 | Cubre ELECTRE y PROMETHEE en conjunto, util para una sesion de metodos de superacion. |
| 5 | Opricovic & Tzeng (2004), VIKOR vs TOPSIS | Intercambiable | "A comparative case study of the VIKOR and TOPSIS rankings similarity", Procedia Computer Science 2020: https://www.sciencedirect.com/science/article/pii/S1877050920319050 | Preserva la comparacion conceptual entre VIKOR y TOPSIS con acceso abierto. |
| 5 | Behzadian et al. (2012), survey TOPSIS | Intercambiable como lectura secundaria | "Comparative analyses of multi-criteria methods in supplier selection problem", Procedia Computer Science 2022: https://www.sciencedirect.com/science/article/pii/S187705092201420X | Aterriza TOPSIS/VIKOR/MARCOS en seleccion de proveedores, mas cercano a logistica. |
| 6 | Govindan et al. (2015), green supplier evaluation review | Intercambiable | Tronnebati, El Yadari & Jawab (2022), "A Review of Green Supplier Evaluation and Selection Issues Using MCDM, MP and AI Models", Sustainability: https://www.mdpi.com/2071-1050/14/24/16714 | Es una revision abierta y actualizada sobre evaluacion/seleccion de proveedores verdes con MCDM. |
| 7 | Wei (2011), GRA intuitionistic fuzzy MCDM | Intercambiable por version abierta del mismo autor/tema | Wei et al. (2011), "Grey Relational Analysis Method for Intuitionistic Fuzzy Multiple Attribute Decision Making with Preference Information on Alternatives", open access: https://link.springer.com/article/10.2991/ijcis.2011.4.2.5 | Muy cercano en autor, anio, metodo y enfoque; funciona bien para la sesion de GRA. |
| 8 | Diakoulaki et al. (1995), CRITIC | No sustituir como lectura historica; si falta acceso, usar complemento | Taherdoost & Madanchian (2023), "Multi-Criteria Decision Making (MCDM) Methods and Concepts": https://www.mdpi.com/2673-8392/3/1/6 + articulos recientes con CRITIC/MEREC segun caso | CRITIC original es fundacional; conviene conseguirlo. Para clase, se puede apoyar con MEREC ya disponible. |
| 9 | Stevic et al. (2020), MARCOS | Intercambiable | "A Hybrid OPA and Fuzzy MARCOS Methodology for Sustainable Supplier Selection with Technology 4.0 Evaluation", Processes 2022: https://www.mdpi.com/2227-9717/10/11/2351 | Mantiene MARCOS, sostenibilidad y seleccion de proveedores; ademas incorpora Industria 4.0. |
| 10 | Dong et al. (2018), liderazgo y opinion dynamics | Intercambiable parcialmente | "Soft consensus cost models for group decision making and economic interpretations", EJOR open access: https://www.sciencedirect.com/science/article/pii/S0377221719302310 | Cubre consenso con interpretacion economica; menos centrado en liderazgo, pero util para comites de decision. |
| 10 | Palomares et al. (2014), comportamientos no cooperativos | Intercambiable si no hay IEEE | "An Adaptive Consensus Model to Manage Non-Cooperative Behaviors in Large Group Decision-Making with Probabilistic Linguistic Information", Mathematics 2026: https://www.mdpi.com/2227-7390/14/6/1049 | Mantiene exactamente la idea de no cooperacion y consenso en grupos grandes. |
| 11 | Tavana & Hatami-Marbini (2011), AHP-TOPSIS NASA | Intercambiable por caso logistico | "A hybrid approach integrating Affinity Diagram, AHP and fuzzy TOPSIS for sustainable city logistics planning": https://www.sciencedirect.com/science/article/pii/S0307904X11004136 | Cambia el caso NASA por logistica urbana, mas alineado con el doctorado. |
| 12 | Doumpos & Figueira (2019), learning criteria weights | Intercambiable | "Reimagining multi-criterion decision making by data-driven methods based on machine learning: A literature review", Information Fusion 2023: https://www.sciencedirect.com/science/article/pii/S1566253523002865 | Actualiza el tema hacia MCDM data-driven/ML, muy alineado con la sesion MCDM + IA. |
| 13 | Govindan, Khodaverdi & Jafarian (2013), TBL fuzzy supplier | Intercambiable | "Green Supplier Evaluation and Selection in Apparel Manufacturing Using a Fuzzy MCDM Approach", Sustainability 2017: https://www.mdpi.com/2071-1050/9/4/650 | Conserva triple bottom line, fuzzy MCDM y evaluacion de proveedores. |
| 13 | Luthra et al. (2017), sustainable supplier framework | Intercambiable | Zhou & Xu (2018), "An Integrated Sustainable Supplier Selection Approach Based on Hybrid Information Aggregation", Sustainability: https://www.mdpi.com/2071-1050/10/7/2543 | Marco integrado de seleccion sustentable con TBL y acceso abierto. |

## 3. Ajustes recomendados al programa

1. Mantener los dos libros Springer de Figueira, Greco & Ehrgott como bibliografia base del curso. Ya estan disponibles y cubren varias sesiones: fundamentos, MAUT, outranking, PROMETHEE/ELECTRE y discusiones de estado del arte.
2. En Sesion 3, si no se consigue el par Dyer/Saaty original, convertir la sesion en "debate AHP: rank reversal, consistencia y validez axiomatica" con dos lecturas abiertas contrapuestas.
3. En Sesion 5, cambiar el enfasis de "solo TOPSIS/VIKOR clasicos" a "comparacion y estabilidad de rankings". Esto conecta mejor con validacion y sensibilidad de Sesion 14.
4. En Sesion 10, usar al menos una lectura de consenso abierta y mas reciente; los articulos cerrados pueden quedar como recomendados.
5. Corregir en el programa la referencia de Cinelli: aparece como Decision Support Systems 57, 14-23, pero el PDF verificado corresponde a Decision Support Systems 163 (2022), articulo 113848, DOI 10.1016/j.dss.2022.113848.
6. En Sesion 15, el Word pide Sharma et al. (2021) y la guia EJOR; la lista inicial tambien pedia guia de Computers & Industrial Engineering. Conviene dejar ambas guias de autores y agregar Sharma como lectura metodologica si se consigue.

## 4. Libros que conviene conseguir

Prioridad alta:

1. Keeney, R. L., & Raiffa, H. (1993). *Decisions with Multiple Objectives: Preferences and Value Tradeoffs*. Cambridge University Press. DOI/book page: https://www.cambridge.org/core/books/decisions-with-multiple-objectives/DEF338459C327778C3F8C4C4A682032F
   - Es el soporte teorico mas fuerte para MAUT, independencia preferencial y tradeoffs.
2. Belton, V., & Stewart, T. J. (2002). *Multiple Criteria Decision Analysis: An Integrated Approach*. Springer. https://link.springer.com/book/10.1007/978-1-4615-1495-4
   - Excelente puente entre escuelas MCDA, problem structuring y aplicacion practica.
3. Hwang, C. L., & Yoon, K. (1981). *Multiple Attribute Decision Making: Methods and Applications*. Springer.
   - Fuente clasica para TOPSIS y metodos MADM de referencia.

Prioridad media:

4. Triantaphyllou, E. (2000). *Multi-Criteria Decision Making Methods: A Comparative Study*. Springer.
   - Muy util para comparar metodos, sensibilidad y rank reversal.
5. Roy, B. (1996). *Multicriteria Methodology for Decision Aiding*. Springer/Kluwer.
   - Base teorica fuerte para ELECTRE, outranking y decision aiding europeo.
6. Greco, S., Ehrgott, M., & Figueira, J. R. (eds.). (2016). *Multiple Criteria Decision Analysis: State of the Art Surveys*. Springer.
   - Ya lo tienes; debe quedar como handbook central del curso.
7. Figueira, J., Greco, S., & Ehrgott, M. (eds.). (2005). *Multiple Criteria Decision Analysis: State of the Art Surveys*. Springer.
   - Ya lo tienes; conservar porque contiene capitulos de la primera edicion usados por el programa.

Prioridad complementaria:

8. Ehrgott, M. (2005). *Multicriteria Optimization*. Springer.
   - Importante para conectar MCDM con optimizacion multiobjetivo y Pareto.
9. Zopounidis, C., & Doumpos, M. (2002/varias eds.). Libros de MCDA en finanzas y preference disaggregation.
   - Relevante para la Sesion 12 si se quiere profundizar en aprendizaje de preferencias y pesos.
10. Saaty, T. L. (1994/2008 eds.). *Fundamentals of Decision Making and Priority Theory with the Analytic Hierarchy Process*.
   - Util como fuente primaria para defender la postura AHP en la Sesion 3.

## 5. Siguiente paso sugerido

Si vas a actualizar formalmente el programa, recomiendo crear una version `Programa_Doctorado_MCDM_Logistica_FIME_UANL_2.docx` con:

- referencias cerradas marcadas como "biblioteca UANL";
- reemplazos abiertos marcados como "lectura alternativa OA";
- correccion de Cinelli 2022;
- Sesion 15 con ambas guias de autores y Sharma et al. si se consigue.
