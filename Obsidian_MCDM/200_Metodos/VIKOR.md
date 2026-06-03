---
type: method
tags: [metodo, teoria, mcdm]
method_name: "VIKOR (ViseKriterijumska Optimizacija I Kompromisno Resenje)"
creator: "Opricovic"
---
# 🔧 VIKOR (ViseKriterijumska Optimizacija I Kompromisno Resenje)

**[[Mapa del curso (MOC)|<< Volver al Mapa del Curso]]**

## 📝 Descripción General
Método de compromiso que maximiza la utilidad de grupo (distancia de Manhattan, medida $S_i$) y minimiza el arrepentimiento individual (distancia de Chebyshev, medida $R_i$). Proporciona intervalos de estabilidad.

## 📐 Estructura Matemática Básica
Índice VIKOR:
$$Q_i = v \frac{S_i - S^*}{S^- - S^*} + (1-v) \frac{R_i - R^*}{R^- - R^*}$$

## ⚠️ Límites y Consideraciones
- Ideal para negociaciones y consensos.
- Proporciona un umbral de ventaja aceptable y estabilidad.

## 💻 Herramientas y Software
- **Python:** `pyDecision.vikor`
- **R:** `MCDA` package

## 📄 Papers de Referencia Relacionados
*Enlaza artículos que usen este método. Ejemplo: [[Rezaei_2015_BWM]]*

-
