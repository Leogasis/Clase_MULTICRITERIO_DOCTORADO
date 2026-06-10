---
type: case-project
tags: [entregable, CP1, ponderacion]
deadline: "Sesión 4"
weight: "15%"
---
# 🔧 CP1 — Ponderación de Criterios (AHP, BWM y Entropía)

**[[Mapa del curso (MOC)|<< Volver al Mapa del Curso]]**

## 🎯 Objetivo
Aplicar y contrastar de forma práctica metodologías de ponderación multicriterio subjetiva (**AHP** y **BWM**) y objetiva (**Entropía**) para determinar la importancia relativa de los criterios de tu problema logístico o de cadena de suministro doctoral real.

## 📝 Actividad

1.  **Contextualización:** Define brevemente el problema de decisión real que estás modelando para tu Product Integrador de Aprendizaje (PIA) o tesis doctoral (ej. localización de CEDIS, selección de proveedores verdes, compra de flota).
2.  **Estructura de Criterios:** Presenta una estructura de al menos 5 criterios (con al menos 2 cualitativos y 2 cuantitativos) y su justificación académica y operativa.
3.  **Aplicación de AHP (Saaty):** 
    *   Realiza las comparaciones pareadas usando la escala tradicional de Saaty (1-9).
    *   Calcula el vector propio principal para obtener los pesos subjetivos.
    *   Calcula el Índice de Consistencia ($CI$) y la Razón de Consistencia ($CR$), asegurándote de que sea $< 0.10$. Si es mayor, ajusta juicios.
4.  **Aplicación de BWM (Rezaei):**
    *   Identifica el mejor (Best) y peor (Worst) criterio.
    *   Establece las comparaciones Best-to-Others y Others-to-Worst (escala 1-9).
    *   Resuelve el modelo de optimización minimax lineal para obtener los pesos y el índice de consistencia $\xi^*$.
5.  **Aplicación de la Entropía de Shannon:**
    *   Utiliza una muestra de datos reales (mínimo 5 alternativas hipotéticas u operativas de tu caso) para los criterios cuantitativos.
    *   Normaliza los datos mediante normalización sumatoria (previo ajuste de criterios de costo).
    *   Calcula la entropía $e_j$, divergencia $d_j$ y los pesos objetivos de Shannon.
6.  **Análisis Comparativo y Propuesta Combinada:**
    *   Presenta en una tabla comparativa los pesos obtenidos con **AHP**, **BWM** y **Entropía**.
    *   Analiza las divergencias significativas: *¿Qué ocurre si un criterio considerado muy importante en AHP/BWM recibe peso bajo en Entropía debido a la homogeneidad de los datos?*
    *   Evalúa el esfuerzo cognitivo (número de comparaciones pareadas) y la robustez matemática frente a cambios en los datos.
    *   Propón una metodología de hibridación combinando pesos subjetivos y objetivos mediante una combinación lineal ponderada: $w_j^{final} = \alpha w_j^{sub} + (1-\alpha) w_j^{obj}$ (justificando tu elección del parámetro $\alpha$).

## 📄 Formato de Entrega
*   Reporte en PDF (3-5 páginas) con la contextualización, ecuaciones utilizadas, tablas de comparación pareada, tabla comparativa de pesos finales y discusión crítica.
*   Script ejecutable en Python (`.ipynb` o `.py`) o archivo de Excel con el cálculo transparente de los tres métodos.
