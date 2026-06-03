# Plan de Clase Detallado: Sesión 2
**Materia:** Herramientas Multicriterio para Toma de Decisiones  
**Programa:** Doctorado en Logística y Cadena de Suministro, FIME – UANL  
**Duración:** 3 horas (180 minutos)  
**Profesor:** Dr. Leonardo Gabriel Hernández Landa  
**Tema General:** Teoría de la Utilidad Multiatributo (MAUT) y Decisiones bajo Incertidumbre  

---

## 🎯 Objetivos de la Sesión
Al finalizar esta segunda sesión, el estudiante de doctorado será capaz de:
1. **Analizar los axiomas fundamentales** de la teoría de la utilidad esperada de Von Neumann-Morgenstern y su validez en contextos logísticos reales.
2. **Estructurar y construir** funciones de valor y utilidad multiatributo (aditivas y multiplicativas), evaluando rigurosamente los supuestos de independencia preferencial.
3. **Diseñar e implementar** procesos de elicitación de preferencias y curvas de indiferencia para tomadores de decisiones reales.
4. **Modelar matemáticamente** el comportamiento frente al riesgo (aversión, neutralidad, propensión) en problemas de selección de proveedores y diseño de cadenas de suministro bajo condiciones de incertidumbre.

---

## ⏱️ Estructura del Tiempo (180 minutos en total)

| Bloque | Actividad | Tiempo | Porcentaje |
| :--- | :--- | :---: | :---: |
| **Bloque 1** | Exposición Teórica Avanzada (Axiomas de Utilidad, MAUT y Riesgo) | 90 min | 50% |
| **Bloque 2** | Discusión de Literatura (Debate Socrático de Lecturas Obligatorias) | 45 min | 25% |
| **Bloque 3** | Taller Práctico Aplicado (Modelado de Función de Utilidad en Python/Excel) | 45 min | 25% |

---

## 📚 Preparación Previa Requerida (Flipped Classroom)
*Los estudiantes debieron leer con antelación los siguientes recursos:*
1. **Capítulo:** Keeney, R. L., & Raiffa, H. (1993). *Decisions with Multiple Objectives: Preferences and Value Trade-offs* (cap. 3: "Multiattribute Value Functions" y cap. 5: "Multiattribute Utility Functions under Risk"). Cambridge University Press.
2. **Capítulo:** Dyer, J. S. (2005). *MAUT – Multiattribute utility theory*. En Multiple Criteria Decision Analysis: State of the Art Surveys (pp. 265–292). Springer. [S02_Dyer_2005_in_Figueira_Greco_Ehrgott_2005_Multiple_Criteria_Decision_Analysis_1st_ed.pdf](file:///Users/leonardohernandez/Academica/Clase_MULTICRITERIO_DOCTORADO/literatura/libros/S02_Dyer_2005_in_Figueira_Greco_Ehrgott_2005_Multiple_Criteria_Decision_Analysis_1st_ed.pdf)
3. **Guía de Lectura Asignada:** 
   * Analiza a fondo los supuestos de independencia preferencial e independencia de utilidad. ¿En qué situaciones logísticas reales (ej. balanceo de inventario vs. tiempos de entrega, o costos de flete vs. huella de carbono) podrían violarse estos supuestos debido a efectos de complementariedad o redundancia?
   * Explica la diferencia teórica fundamental entre una función de valor (bajo certidumbre) y una función de utilidad (bajo riesgo/incertidumbre).

---

## 📖 Contenido Temático y Desarrollo de la Sesión

### BLOQUE 1: Exposición Teórica Avanzada (90 min)

#### 1.1. Fundamentos de la Teoría de la Utilidad Esperada (25 min)
* **Axiomas de Von Neumann-Morgenstern (VNM):**
  * **Completitud:** El decisor siempre puede comparar y ordenar loterías ($A \succ B$, $B \succ A$, o $A \sim B$).
  * **Transitividad:** Si $A \succ B$ y $B \succ C$, entonces $A \succ C$.
  * **Continuidad:** Si $A \succ B \succ C$, entonces existe una probabilidad $p$ tal que $[pA, (1-p)C] \sim B$.
  * **Independencia (Sustitución):** Si $A \succ B$, entonces para cualquier lotería $C$ y $p \in (0, 1]$, $[pA, (1-p)C] \succ [pB, (1-p)C]$.
* **La paradoja de Allais:** Discusión sobre cómo los seres humanos reales violan sistemáticamente el axioma de independencia en la toma de decisiones prácticas (relevancia de las teorías descriptivas frente a las normativas).
* **Función de valor frente a función de utilidad:** 
  * Las funciones de valor representan preferencias bajo certidumbre absoluta y miden diferencias relativas de atracción.
  * Las funciones de utilidad incorporan de manera explícita la actitud del decisor ante el riesgo y la incertidumbre.

#### 1.2. Estructura de Funciones de Valor y Utilidad Multiatributo (MAUT) (30 min)
* **El supuesto de Independencia Preferencial:**
  * Un par de atributos $\{Y, Z\}$ es preferencialmente independiente del resto de atributos si el orden de preferencia de combinaciones de $\{Y, Z\}$ no depende de los valores fijos en los que se encuentren los otros atributos.
* **Forma Funcional Aditiva:**
  $$v(x) = \sum_{i=1}^n w_i v_i(x_i)$$
  * Requiere independencia preferencial mutua.
  * Supone que los atributos son complementarios o sustitutos perfectos sin interacciones cruzadas (sin sinergia ni redundancia).
* **Forma Funcional Multiplicativa (Modelo de Keeney-Raiffa):**
  $$1 + k u(x) = \prod_{i=1}^n [1 + k k_i u_i(x_i)]$$
  * Requiere independencia de utilidad mutua.
  * Permite modelar interacciones entre criterios a través del parámetro de escala global $k$. Si $k > 0$, existe sustituibilidad; si $k < 0$, existe complementariedad.
* **Elicitación del parámetro $k$:** Modelado matemático y consistencia del escalamiento.

#### 1.3. Elicitación de Preferencias y Actitud ante el Riesgo (20 min)
* **Modelado de funciones de utilidad univariadas $u_i(x_i)$:**
  * Uso de funciones exponenciales: $u(x) = a - b e^{-c x}$ (donde $c$ es el coeficiente de aversión absoluta al riesgo de Pratt-Arrow).
  * Métodos de elicitación en vivo:
    * **Método del equivalente de certeza (Certainty Equivalent Method):** Encontrar el valor seguro que es equivalente a jugar una lotería 50/50.
    * **Método del equivalente de probabilidad (Probability Equivalent Method):** Encontrar la probabilidad que hace al decisor indiferente entre una alternativa segura y una lotería extrema.
* **Clasificación de actitudes ante el riesgo:**
  * **Aversión al riesgo:** Función de utilidad cóncava ($u''(x) < 0$).
  * **Neutralidad al riesgo:** Función de utilidad lineal ($u''(x) = 0$).
  * **Propensión al riesgo:** Función de utilidad convexa ($u''(x) > 0$).

#### 1.4. Aplicación en Logística y Supply Chain (15 min)
* **Selección de proveedores bajo incertidumbre de entregas o precios:** 
  * Trade-off entre costo esperado y variabilidad en el tiempo de entrega (lead time delay).
* **Evaluación de resiliencia en redes de distribución:**
  * Modelado de la utilidad del decisor frente al riesgo catastrófico (baja probabilidad, alto impacto) frente al costo seguro de redundancia de stock o diversificación de proveedores.

---

### BLOQUE 2: Discusión de Literatura - Debate Socrático (45 min)

#### 2.1. Debate sobre supuestos de MAUT (Dyer 2005) (25 min)
* **Pregunta Detonante 1:** *En la práctica de la cadena de suministro, las decisiones corporativas suelen tomarse bajo el supuesto implícito de que los criterios son aditivos e independientes. Dyer (2005) profundiza en los estrictos fundamentos axiomáticos para que la forma aditiva sea matemáticamente válida. ¿Qué implicaciones éticas y financieras tiene para una empresa tomar una decisión estratégica de localización basándose en un modelo aditivo simple, si en la realidad existe una fuerte dependencia preferencial entre el costo de transporte y la proximidad a puertos?*
  * *Respuestas esperadas:* El decisor puede estar sobreponderando o subestimando opciones viables; el modelo matemático distorsiona la realidad al asumir compensación lineal cuando hay vetos prácticos o interacciones complejas.
* **Pregunta Detonante 2:** *En el contexto de la teoría de la utilidad bajo riesgo (Keeney-Raiffa), ¿cómo se interpreta conceptualmente una constante de escala global $k = 0$ frente a $k \neq 0$? Si se encuentra que $k < 0$, ¿qué nos dice esto sobre la psicología de la organización logística respecto a sus metas de resiliencia frente a costos?*
  * *Respuestas esperadas:* $k=0$ reduce el modelo a una simple forma aditiva (los criterios actúan de forma aislada). Un $k < 0$ indica complementariedad extrema: la organización busca un balance estricto y penaliza severamente el desempeño desigual entre criterios críticos (ej. no sirve de nada tener costo cero si la seguridad es pésima).

#### 2.2. Violación de supuestos de utilidad y Paradojas en Logística (20 min)
* **Pregunta Detonante 1:** *Pensemos en la contratación de un seguro para una flota logística o la decisión de resguardar inventario de seguridad. Si los decisores corporativos se comportaran según la teoría de VNM, comprarían seguros basándose exclusivamente en el cálculo del valor esperado. Sin embargo, en el mundo real vemos que las empresas prefieren pagar primas de seguro que exceden con creces la pérdida esperada. ¿La teoría MAUT tradicional captura de forma adecuada este fenómeno, o requerimos enfoques alternos como Prospect Theory de Kahneman y Tversky?*
  * *Respuestas esperadas:* La teoría tradicional puede capturarlo asumiendo una aversión al riesgo muy pronunciada (curvas extremadamente cóncavas), pero falla al modelar la distorsión subjetiva de probabilidades bajas, donde la Prospect Theory ofrece mejor ajuste descriptivo.

---

### BLOQUE 3: Taller Práctico - Modelado de Utilidad para Selección de Proveedor (45 min)

En este taller, el profesor guiará la formulación paso a paso de una función de utilidad multiatributo de dos criterios (Costo de Adquisición e Incumplimiento de Entregas) para evaluar proveedores bajo riesgo.

#### 3.1. Formulación del Problema (10 min)
* **Criterio 1 (Costo, $X_1$):** Rango de \$10,000 (mejor) a \$20,000 USD (peor).
* **Criterio 2 (Retraso, $X_2$):** Rango de 0% (mejor) a 15% de entregas tardías (peor).
* El estudiante determinará las funciones univariadas de utilidad exponenciales para ambos criterios:
  * Para $X_1$ (costo), asumiendo **neutralidad al riesgo** (lineal).
  * Para $X_2$ (retraso), asumiendo **aversión al riesgo** (cóncava, aversión $c = 0.15$).

#### 3.2. Elicitación de Pesos y Parámetro de Interacción $k$ (20 min)
1. Elicitar los pesos escalares individuales ($k_1, k_2$) mediante comparaciones de indiferencia:
   * Ejemplo: Determinar a qué probabilidad $p$ el decisor es indiferente entre un proveedor con retraso del 0% pero costo de \$20,000 (peor costo), y una lotería que da el mejor escenario (\$10,000, 0% retraso) con probabilidad $p$ o el peor scenario (\$20,000, 15% retraso) con probabilidad $(1-p)$.
2. Resolver la ecuación polinomial de Keeney-Raiffa para encontrar la constante de interacción global $k$:
   $$1 + k = (1 + k k_1)(1 + k k_2)$$
3. Analizar si la relación resultante es aditiva ($k_1 + k_2 = 1 \implies k=0$), multiplicativa sustituta ($k_1 + k_2 < 1 \implies k > 0$) o multiplicativa complementaria ($k_1 + k_2 > 1 \implies k < 0$).

#### 3.3. Evaluación de Alternativas e Interpretación (15 min)
* Comparar tres proveedores candidatos:
  * **Proveedor A:** Costo \$12,000 USD, Retraso 8% (estable).
  * **Proveedor B:** Costo \$10,500 USD, Retraso 12% (económico pero riesgoso).
  * **Proveedor C:** Costo \$15,000 USD, Retraso 2% (costoso pero muy confiable).
* Calcular la utilidad multiatributo global $u(A), u(B), u(C)$ y determinar el ranking óptimo del decisor bajo su perfil de riesgo.

---

## 🛠️ Recursos y Software Necesarios
* **Para el Profesor:** Proyector/Pantalla, pizarrón para deducciones algebraicas de la constante $k$.
* **Para los Alumnos:** Computadora portátil personal con Jupyter Notebook o Excel instalado.
* **Librerías de Python sugeridas:** `numpy`, `scipy` (para resolver ecuaciones polinomiales no lineales) y `matplotlib` (para graficar las curvas de utilidad).

---

## 📝 Lista de Cotejo de Contribución Doctoral (Para el Profesor)
Durante la clase, asegúrese de validar si los estudiantes comprendieron que:
* [ ] La independencia preferencial es un supuesto matemático extremadamente fuerte que rara vez se cumple de manera perfecta y que debe justificarse rigurosamente en un artículo académico.
* [ ] La curvatura de la función de utilidad (concavidad/convexidad) no es arbitraria; representa empíricamente la tolerancia al riesgo que tiene la organización y debe elicitarse mediante experimentos estructurados.
* [ ] Un estudio doctoral riguroso que aplique MAUT debe detallar explícitamente el procedimiento matemático y los cuestionarios utilizados para la elicitación de pesos y curvas de utilidad.
