---
type: method
tags: [metodo, teoria, mcdm]
method_name: "Best Worst Method (BWM)"
creator: "Rezaei"
---
# 🔧 Best Worst Method (BWM)

**[[Mapa del curso (MOC)|<< Volver al Mapa del Curso]]**

## 📝 Descripción General
Método de ponderación estructurado que selecciona el mejor (Best) y el peor (Worst) criterio, comparando el resto frente a ellos. Reduce el número de comparaciones de $n(n-1)/2$ (en AHP) a $2n-3$.

## 📐 Estructura Matemática Básica
Modelo de optimización lineal:
$$\min \xi^{L}$$
$$\text{s.t. } |w_B - a_{Bj} w_j| \le \xi^{L}, \quad |w_j - a_{jW} w_W| \le \xi^{L}$$

## ⚠️ Límites y Consideraciones
- Altamente consistente.
- Menor esfuerzo cognitivo para el decisor.

## 💻 Herramientas y Software
- **Python:** `pyDecision.bwm`
- **Web:** Solver oficial de Jafar Rezaei

## 📄 Papers de Referencia Relacionados
*Enlaza artículos que usen este método. Ejemplo: [[Rezaei_2015_BWM]]*

-
