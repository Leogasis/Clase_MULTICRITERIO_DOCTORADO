---
type: case-project
tags: [entregable, CP2, distancia]
deadline: "Sesión 8"
weight: "20%"
---
# 🔧 CP2 — Jerarquización por Distancia a la Solución Ideal (TOPSIS vs. VIKOR vs. EDAS)

**[[Flujo de casos prácticos|<< Volver al Flujo de Casos Prácticos]]**

## 🎯 Objetivo
Resolver tu caso de estudio logístico y jerarquizar tus 4 alternativas candidatas aplicando y comparando tres métodos basados en distancias geométricas (TOPSIS, VIKOR y EDAS).

## 📝 Actividad
1.  **Datos de Entrada:** Presenta la matriz de decisión $X_{4 \times 5}$ con datos cuantitativos y cualitativos reales y los pesos de criterios obtenidos en el CP1.
2.  **Aplicación de TOPSIS:**
    - Normaliza la matriz (lineal o vectorial) y aplica los pesos.
    - Identifica la solución ideal positiva ($A^+$) y negativa ($A^-$).
    - Calcula las distancias euclidianas y el coeficiente de cercanía relativo ($CC_i$).
3.  **Aplicación de VIKOR:**
    - Determina los valores óptimos ($f_j^*$) y peores ($f_j^-$).
    - Calcula las medidas de utilidad de grupo ($S_i$) y de arrepentimiento individual ($R_i$).
    - Calcula el índice VIKOR ($Q_i$) con un peso de la estrategia de decisión $v = 0.5$.
    - Evalúa las condiciones de ventaja aceptable y estabilidad aceptable.
4.  **Aplicación de EDAS:**
    - Calcula la solución promedio para cada criterio.
    - Determina las distancias positivas (PDA) y negativas (NDA) desde el promedio.
    - Obtén la puntuación de evaluación final ($AS_i$).
5.  **Análisis Comparativo:**
    - Muestra los rankings obtenidos por TOPSIS, VIKOR y EDAS.
    - Discute el impacto de las lógicas de distancia (distancia euclidiana de TOPSIS vs. compromiso/arrepentimiento de VIKOR vs. evaluación promedio de EDAS) en el resultado.
