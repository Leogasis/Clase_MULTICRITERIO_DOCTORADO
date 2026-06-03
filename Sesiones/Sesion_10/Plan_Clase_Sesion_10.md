# Plan de Clase Detallado: Sesión 10
**Materia:** Herramientas Multicriterio para Toma de Decisiones  
**Programa:** Doctorado en Logística y Cadena de Suministro, FIME – UANL  
**Duración:** 3 horas (180 minutos)  
**Profesor:** Dr. Leonardo Gabriel Hernández Landa  
**Tema General:** Decisión Multicriterio Grupal (GDMCDM) y Modelos de Consenso  

---

## 🎯 Objetivos de la Sesión
Al finalizar esta décima sesión, el estudiante de doctorado será capaz de:
1. **Comprender los retos matemáticos y sociales** de agregar preferencias individuales en un juicio colectivo coherente.
2. **Implementar operadores de agregación** avanzados como el Operador de Media Ponderada Ordenada (OWA) y medias geométricas.
3. **Calcular la distancia de consenso** y cuantificar el grado de acuerdo entre tomadores de decisiones.
4. **Diseñar mecanismos de retroalimentación** de consenso para resolver conflictos y alinear preferencias directivas.
5. **Aplicar estos modelos** a un comité corporativo real para la licitación y adquisición de flotas de transporte terrestre.

---

## ⏱️ Estructura del Tiempo (180 minutos en total)

| Bloque | Actividad | Tiempo | Porcentaje |
| :--- | :--- | :---: | :---: |
| **Bloque 1** | Exposición Teórica (Teoría de agregación, teorema de imposibilidad de Arrow, operadores OWA, índices de disenso) | 90 min | 50% |
| **Bloque 2** | Debate Socrático de Literatura (Modelos de consenso de costo suave y comportamiento cooperativo) | 45 min | 25% |
| **Bloque 3** | Taller Aplicado y Ejercicios (Simulación de juego de roles de comité de compras en Excel/Python) | 45 min | 25% |

---

## 📚 Preparación Previa Requerida (Flipped Classroom)
*Los estudiantes debieron leer con antelación los siguientes recursos:*
1. **Artículo:** *Soft consensus cost models for group decision making and economic interpretations*. European Journal of Operational Research, 277(3), 964–980. [S10_Soft_Consensus_Cost_Models_Group_Decision_Making_2019.pdf](file:///Users/leonardohernandez/Academica/Clase_MULTICRITERIO_DOCTORADO/literatura/articulos/S10_Soft_Consensus_Cost_Models_Group_Decision_Making_2019.pdf)
2. **Artículo:** Palomares, I., Martinez, L., \& Herrera, F. (2014). *A consensus model to detect and manage noncooperative behaviors in large-scale group decision making*. IEEE Transactions on Fuzzy Systems, 22(3), 516–530. `[IEEE Xplore / Biblioteca UANL]`
3. **Guía de Lectura Asignada:** 
   * ¿Qué establece el Teorema de Imposibilidad de Arrow respecto a los sistemas de votación y agregación social?
   * ¿Cómo se definen los comportamientos no cooperativos en comités de decisión a gran escala según Palomares et al.?

---

## 📖 Contenido Temático y Desarrollo de la Sesión

### BLOQUE 1: Exposición Teórica (90 min)
* **Introducción a GDMCDM:**
  * Estructura de preferencias individuales: matrices de relaciones de preferencia difusas.
* **Operadores de Agregación:**
  * Operador OWA (Ordered Weighted Averaging) de Yager (1988).
  * Operador de Media Geométrica Ponderada (WG).
* **Medición de Consenso:**
  * Matriz de similitud y distancia al consenso global.
  * Niveles de aceptación de consenso y rondas de negociación iterativas.
  * Costo de consenso: modelos de compensación económica o negociación política.

---

### BLOQUE 2: Discusión de Literatura - Debate Socrático (45 min)
* **Pregunta Detonante 1:** *En un comité de licitación logística real para renovar la flota, Finanzas exige bajo costo, Operaciones exige confiabilidad técnica y Sustentabilidad exige motores eléctricos. Si agregamos por promedio simple, ¿quién queda insatisfecho? ¿Cómo ayuda un "modelo de costo de consenso suave" a negociar el cambio de preferencias de los directores?*
* **Pregunta Detonante 2:** *¿Cómo pueden identificarse comportamientos estratégicos o bloqueos deliberados (boicots) en decisiones logísticas compartidas utilizando distancias matemáticas?*

---

### BLOQUE 3: Taller Práctico - Ejercicios (45 min)

#### 3.1. Ejercicio Guiado (Profesor): Simulación de Consenso
El profesor guiará un ejercicio interactivo donde 3 perfiles directivos (Ventas, Finanzas, Logística) evalúan 3 proveedores de última milla. El profesor calculará en Excel el nivel de consenso inicial, identificará al directivo disidente y aplicará un lazo de retroalimentación matemática para proponer cambios de juicios mínimos.

#### 3.2. Caso Práctico Alumno (Trabajo Autónomo)
El alumno programará en Python una agregación OWA para ponderaciones de criterios dadas por 5 gerentes regionales de distribución.
* **Entregable:** Pesos agregados por OWA bajo perfil optimista, moderado y pesimista, y discusión del impacto de la ordenación de datos.

---

## 🎓 Plan de Evidencias (Evaluación)
* **Paso de Control:** Los estudiantes ultiman detalles prácticos del **E4 (CP4: Lógica Difusa o Sistemas Grises)** que se entrega la siguiente semana.
* **Avance del PIA:** Definir la sección de "Caso de Estudio y Datos" del manuscrito del artículo.
