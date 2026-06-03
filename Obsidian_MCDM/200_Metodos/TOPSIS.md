---
type: method
tags: [metodo, teoria, mcdm]
method_name: "TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)"
creator: "Hwang & Yoon"
---
# 🔧 TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)

**[[Mapa del curso (MOC)|<< Volver al Mapa del Curso]]**

## 📝 Descripción General
Selecciona la alternativa que se encuentra a menor distancia de la solución ideal positiva ($A^+$) y a mayor distancia de la solución ideal negativa o anti-ideal ($A^-$) usando distancia euclidiana.

## 📐 Estructura Matemática Básica
Coeficiente de cercanía:
$$CC_i = \frac{d_i^-}{d_i^+ + d_i^-}$$
Donde $d_i^+$ y $d_i^-$ son las distancias a las soluciones ideales.

## ⚠️ Límites y Consideraciones
- Sencillo de programar.
- No tiene límites en número de criterios.
- Compensatorio en su lógica.

## 💻 Herramientas y Software
- **Python:** `pyDecision.topsis`
- **R:** `MCDA` package

## 📄 Papers de Referencia Relacionados
*Enlaza artículos que usen este método. Ejemplo: [[Rezaei_2015_BWM]]*

-
