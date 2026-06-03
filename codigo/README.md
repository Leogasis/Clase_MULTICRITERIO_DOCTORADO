# Directorio de Códigos y Scripts del Proyecto

Este directorio contiene los scripts desarrollados en Python para la automatización, inspección, actualización y procesamiento de los archivos del programa analítico de la clase **Herramientas Multicriterio para Toma de Decisiones**.

## Contenido del Directorio

A continuación se detalla la función de cada script dentro del flujo de trabajo del curso:

---

### 1. [read_docx.py](file:///Users/leonardohernandez/Academica/Clase_MULTICRITERIO_DOCTORADO/codigo/read_docx.py)
* **Propósito:** Extracción rápida de texto desde el documento de Word `.docx`.
* **Cómo funciona:** Descomprime el archivo `.docx` (que estructuralmente es un archivo `.zip`), accede al XML principal (`word/document.xml`), parsea los elementos de párrafo (`<w:p>`) y texto (`<w:t>`), y los escribe en un archivo de texto plano llamado `Programa_text.txt`.

### 2. [update_docx.py](file:///Users/leonardohernandez/Academica/Clase_MULTICRITERIO_DOCTORADO/codigo/update_docx.py)
* **Propósito:** Actualización programática del archivo de Word principal `Programa_Doctorado_MCDM_Logistica_FIME_UANL_2_actualizado.docx`.
* **Cómo funciona:**
  - Lee el árbol XML del documento.
  - Modifica las celdas de las tablas correspondientes a las sesiones y a la estructura de evaluación para reflejar los nuevos entregables (**E1 a E5**).
  - Actualiza la tabla general de evaluación (Ponderación 15%, 20%, 20%, 15%, 30%).
  - Modifica la tabla de cronograma general del curso.
  - Vuelve a empaquetar el XML modificado dentro del archivo `.docx` original de forma segura.

### 3. [edit_docx_file.py](file:///Users/leonardohernandez/Academica/Clase_MULTICRITERIO_DOCTORADO/codigo/edit_docx_file.py)
* **Propósito:** Es una versión de desarrollo/pruebas del script de edición de `.docx`.
* **Cómo funciona:** Realiza modificaciones similares a `update_docx.py` pero imprime el contenido XML final resultante a la salida estándar (`stdout`) para su depuración y verificación visual antes de aplicarlo.

### 4. [inspect_docx_tables.py](file:///Users/leonardohernandez/Academica/Clase_MULTICRITERIO_DOCTORADO/codigo/inspect_docx_tables.py)
* **Propósito:** Herramienta de diagnóstico para inspeccionar la estructura interna de todas las tablas en el documento de Word.
* **Cómo funciona:** Imprime el índice de cada tabla encontrada en el XML junto con el contenido textual de cada una de sus filas y celdas. Es útil para identificar qué número de tabla corresponde a cada sección (por ejemplo, localizar la tabla de cronograma o de ponderaciones).

### 5. [inspect_session_tables.py](file:///Users/leonardohernandez/Academica/Clase_MULTICRITERIO_DOCTORADO/codigo/inspect_session_tables.py)
* **Propósito:** Filtra e inspecciona específicamente aquellas tablas que contienen información de las sesiones.
* **Cómo funciona:** Analiza el primer elemento de cada tabla. Si contiene la palabra clave `"Sesión"`, procede a listar todo el contenido de la tabla por filas. Sirvió para validar que los entregables y temas de cada sesión estuvieran correctamente estructurados antes de los scripts de edición.

### 6. [inspect_docx_xml.py](file:///Users/leonardohernandez/Academica/Clase_MULTICRITERIO_DOCTORADO/codigo/inspect_docx_xml.py)
* **Propósito:** Herramienta de inspección general para buscar palabras clave dentro del XML de Word.
* **Cómo funciona:** Recorre los párrafos del documento e imprime aquellos que contienen palabras clave relacionadas con la evaluación (como `"Evidencia"`, `"E1"`, `"E2"`, etc.) para verificar su formato exacto y ubicación.

### 7. [copy_image.py](file:///Users/leonardohernandez/Academica/Clase_MULTICRITERIO_DOCTORADO/codigo/copy_image.py)
* **Propósito:** Copiar la imagen de portada generada al directorio correspondiente de las diapositivas.
* **Cómo funciona:** Toma un archivo de imagen temporal de la ruta de caché del asistente y lo copia al destino local `Diapositivas/img/mcdm_logistics_cover.png`, asegurando que exista el directorio destino.

### 8. [test_list.py](file:///Users/leonardohernandez/Academica/Clase_MULTICRITERIO_DOCTORADO/codigo/test_list.py)
* **Propósito:** Script de prueba unitario y rápido.
* **Cómo funciona:** Verifica que el script de Python tenga los permisos y capacidad adecuados para crear carpetas en el sistema de archivos (`Diapositivas/img`).
