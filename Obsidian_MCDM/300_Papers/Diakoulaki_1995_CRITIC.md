---
type: paper
tags: [paper, lectura, literatura, critic, ponderacion]
title: "Determining objective weights in multiple criteria problems: the CRITIC method"
author: "D. Diakoulaki, G. Mavrotas, L. Papayannakis"
journal: "Computers & Operations Research"
year: 1995
---
# 📄 Determining objective weights in multiple criteria problems: the CRITIC method

**[[Mapa del curso (MOC)|<< Volver al Mapa del Curso]]**

- **Autor(es):** D. Diakoulaki, G. Mavrotas, L. Papayannakis
- **Revista:** Computers & Operations Research (Vol. 22, No. 7, pp. 763–770)
- **Año:** 1995

## 📝 Resumen del Artículo
Este artículo seminal introduce por primera vez el método **CRITIC** (*Criteria Importance Through Intercriteria Correlation*). Los autores argumentan que los pesos de los criterios deben reflejar la estructura e información intrínseca de los datos empíricos de desempeño de las alternativas. Para ello, proponen combinar el análisis de la desviación estándar (contraste o variabilidad individual del criterio) y el coeficiente de correlación lineal de Pearson (conflicto entre criterios) para evitar la redundancia de la información en el modelo de decisión.

## 🔑 Contribuciones Clave
*   **Crítica a la Ponderación Subjetiva e Independencia:** Identifica que los decisores humanos suelen ignorar las dependencias reales entre criterios al asignar pesos a mano, lo que deforma la representatividad matemática del modelo.
*   **Métrica de Conflicto Intercriterio:** Formula el conflicto que un criterio genera con los demás como $\sum (1 - r_{jk})$. Si hay correlación de +1, el conflicto aportado es 0 (redundancia total).
*   **Definición de Cantidad de Información ($C_j$):** Propone multiplicar la desviación estándar por la suma de conflictos para ponderar la "señal de información útil" que contiene cada columna de la matriz de decisión.

## 🔗 Conexiones en el Vault
*   Método: [[CRITIC]]
*   Sesión relacionada: [[Sesion_03_Ponderacion_Objetiva_Entropia_CRITIC_MEREC|Sesión 03]]
*   Conexión con otros métodos: Sirve como contrapeso metodológico directo de la [[Entropia]] (que no evalúa correlaciones) y complementa el rigor en análisis multivariados de datos de tesis.

## ✏️ Notas Personales y Crítica
*Escribe tus reflexiones de lectura aquí...*
