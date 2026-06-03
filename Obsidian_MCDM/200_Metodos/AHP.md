---
type: method
tags: [metodo, teoria, mcdm]
method_name: "Analytic Hierarchy Process (AHP)"
creator: "Saaty"
---
# 🔧 Analytic Hierarchy Process (AHP)

**[[Mapa del curso (MOC)|<< Volver al Mapa del Curso]]**

## 📝 Descripción General
Consiste en estructurar el problema jerárquicamente. Se realizan comparaciones pareadas de alternativas y criterios usando una escala del 1 al 9. Se calcula el vector propio principal para determinar pesos y prioridades.

## 📐 Estructura Matemática Básica
$$A \cdot w = \lambda_{\max} \cdot w$$  
Donde $A$ es la matriz de comparaciones, $w$ es el vector de pesos y $\lambda_{\max}$ es el valor propio principal.

## ⚠️ Límites y Consideraciones
- Subjetividad en juicios.
- Consistencia lógica verificable ($CR < 0.10$).
- Fenómeno de **Rank Reversal** al añadir alternativas.

## 💻 Herramientas y Software
- **Python:** `pyDecision.ahp`
- **R:** `ahp` package
- **Software:** SuperDecisions

## 📄 Papers de Referencia Relacionados
*Enlaza artículos que usen este método. Ejemplo: [[Rezaei_2015_BWM]]*

-
