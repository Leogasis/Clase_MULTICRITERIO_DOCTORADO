import zipfile
import xml.etree.ElementTree as ET
import copy
import os

namespaces = {
    'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
}
ET.register_namespace('w', 'http://schemas.openxmlformats.org/wordprocessingml/2006/main')

def set_cell_text(tc, val):
    p_list = list(tc.findall('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'))
    if not p_list:
        p = ET.Element('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p')
        tc.append(p)
    else:
        p = p_list[0]
        for extra_p in p_list[1:]:
            tc.remove(extra_p)
            
    r_list = list(p.findall('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}r'))
    if not r_list:
        r = ET.Element('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}r')
        p.append(r)
    else:
        r = r_list[0]
        for extra_r in r_list[1:]:
            p.remove(extra_r)
            
    t_list = list(r.findall('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t'))
    if not t_list:
        t = ET.Element('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t')
        r.append(t)
    else:
        t = t_list[0]
        for extra_t in t_list[1:]:
            r.remove(extra_t)
            
    t.text = val

def main():
    doc_path = 'Programa_Doctorado_MCDM_Logistica_FIME_UANL_2_actualizado.docx'
    temp_path = 'temp_word.zip'
    
    with zipfile.ZipFile(doc_path) as docx:
        xml_content = docx.read('word/document.xml')
        
    root = ET.fromstring(xml_content)
    
    tables = list(root.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}tbl'))
    print(f"Total tables found: {len(tables)}")
    
    session_tables = {}
    for table_idx, tbl in enumerate(tables):
        first_cell = ""
        for tc in tbl.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}tc'):
            first_cell = "".join([t.text for t in tc.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t') if t.text])
            break
        if "Sesión" in first_cell:
            session_tables[first_cell] = tbl

    def get_sess_tbl(prefix):
        for name, tbl in session_tables.items():
            if name.startswith(prefix):
                return tbl
        return None

    def set_row_cell_text(tr, cell_idx, text):
        tcs = list(tr.findall('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}tc'))
        if cell_idx < len(tcs):
            set_cell_text(tcs[cell_idx], text)

    def get_row_by_label(tbl, label):
        for tr in tbl.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}tr'):
            tcs = list(tr.findall('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}tc'))
            if tcs:
                cell_text = "".join([t.text for t in tcs[0].iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t') if t.text])
                if cell_text.strip() == label:
                    return tr
        return None

    # Sesión 3: change Entregable to '—'
    tbl_s3 = get_sess_tbl("Sesión 3:")
    if tbl_s3 is not None:
        tr = get_row_by_label(tbl_s3, "Entregable")
        if tr is not None:
            set_row_cell_text(tr, 1, "—")

    # Sesión 5: append Entregable row
    tbl_s5 = get_sess_tbl("Sesión 5:")
    if tbl_s5 is not None:
        rows = list(tbl_s5.findall('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}tr'))
        new_tr = copy.deepcopy(rows[-1])
        set_row_cell_text(new_tr, 0, "Entregable")
        set_row_cell_text(new_tr, 1, "E1 — Caso Práctico 1: Ponderación de Criterios (AHP vs. BWM)")
        tbl_s5.append(new_tr)

    # Sesión 6: change to '—'
    tbl_s6 = get_sess_tbl("Sesión 6:")
    if tbl_s6 is not None:
        tr = get_row_by_label(tbl_s6, "Entregable")
        if tr is not None:
            set_row_cell_text(tr, 1, "—")

    # Sesión 8: append Entregable row
    tbl_s8 = get_sess_tbl("Sesión 8:")
    if tbl_s8 is not None:
        rows = list(tbl_s8.findall('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}tr'))
        new_tr = copy.deepcopy(rows[-1])
        set_row_cell_text(new_tr, 0, "Entregable")
        set_row_cell_text(new_tr, 1, "E2 — Caso Práctico 2: Jerarquización por Distancia (TOPSIS vs. VIKOR vs. EDAS) (Inicio formal del PIA)")
        tbl_s8.append(new_tr)

    # Sesión 9: change to '—'
    tbl_s9 = get_sess_tbl("Sesión 9:")
    if tbl_s9 is not None:
        tr = get_row_by_label(tbl_s9, "Entregable")
        if tr is not None:
            set_row_cell_text(tr, 1, "—")

    # Sesión 10: append Entregable row
    tbl_s10 = get_sess_tbl("Sesión 10:")
    if tbl_s10 is not None:
        rows = list(tbl_s10.findall('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}tr'))
        new_tr = copy.deepcopy(rows[-1])
        set_row_cell_text(new_tr, 0, "Entregable")
        set_row_cell_text(new_tr, 1, "E3 — Caso Práctico 3: Relaciones de Superación (ELECTRE vs. PROMETHEE)")
        tbl_s10.append(new_tr)

    # Sesión 12: change to '—'
    tbl_s12 = get_sess_tbl("Sesión 12:")
    if tbl_s12 is not None:
        tr = get_row_by_label(tbl_s12, "Entregable")
        if tr is not None:
            set_row_cell_text(tr, 1, "—")

    # Sesión 13: append Entregable row
    tbl_s13 = get_sess_tbl("Sesión 13:")
    if tbl_s13 is not None:
        rows = list(tbl_s13.findall('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}tr'))
        new_tr = copy.deepcopy(rows[-1])
        set_row_cell_text(new_tr, 0, "Entregable")
        set_row_cell_text(new_tr, 1, "E4 — Caso Práctico 4: Lógica Difusa e Incertidumbre (Fuzzy/GRA)")
        tbl_s13.append(new_tr)

    # Sesión 15: modify Entregable row to E5 - PIA
    tbl_s15 = get_sess_tbl("Sesión 15:")
    if tbl_s15 is not None:
        tr = get_row_by_label(tbl_s15, "Entregable")
        if tr is not None:
            set_row_cell_text(tr, 1, "E5 — Producto Integrador de Aprendizaje (PIA): Artículo de Investigación y Defensa")

    # Modify Table 16 (Main Evaluation Table)
    tbl_eval = None
    for tbl in tables:
        rows = list(tbl.findall('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}tr'))
        if rows:
            first_cell = "".join([t.text for t in rows[0].iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t') if t.text])
            if first_cell.strip() == "Evidencia":
                tbl_eval = tbl
                break

    if tbl_eval is not None:
        rows = list(tbl_eval.findall('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}tr'))
        # Row 1: E1
        set_row_cell_text(rows[1], 0, "E1 — Caso Práctico 1: Ponderación de Criterios (AHP vs. BWM)")
        set_row_cell_text(rows[1], 1, "15%")
        set_row_cell_text(rows[1], 2, "Sesión 5")
        set_row_cell_text(rows[1], 3, "Ponderación de Criterios")
        # Row 2: E2
        set_row_cell_text(rows[2], 0, "E2 — Caso Práctico 2: Jerarquización por Distancia (TOPSIS vs. VIKOR vs. EDAS)")
        set_row_cell_text(rows[2], 1, "20%")
        set_row_cell_text(rows[2], 2, "Sesión 8")
        set_row_cell_text(rows[2], 3, "Jerarquización por Distancia")
        # Row 3: E3
        set_row_cell_text(rows[3], 0, "E3 — Caso Práctico 3: Relaciones de Superación (ELECTRE vs. PROMETHEE)")
        set_row_cell_text(rows[3], 1, "20%")
        set_row_cell_text(rows[3], 2, "Sesión 10")
        set_row_cell_text(rows[3], 3, "Relaciones de Superación")
        # Row 4: E4
        set_row_cell_text(rows[4], 0, "E4 — Caso Práctico 4: Lógica Difusa e Incertidumbre (Fuzzy/GRA)")
        set_row_cell_text(rows[4], 1, "15%")
        set_row_cell_text(rows[4], 2, "Sesión 13")
        set_row_cell_text(rows[4], 3, "Lógica Difusa e Incertidumbre")
        # Row 5: E5
        set_row_cell_text(rows[5], 0, "E5 — Producto Integrador de Aprendizaje (PIA)")
        set_row_cell_text(rows[5], 1, "30%")
        set_row_cell_text(rows[5], 2, "Sesión 15")
        set_row_cell_text(rows[5], 3, "Artículo de Investigación y Defensa")

    # Modify Descriptions Tables (Tables 17-21)
    for tbl in tables:
        rows = list(tbl.findall('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}tr'))
        if rows:
            first_cell = "".join([t.text for t in rows[0].iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t') if t.text])
            if first_cell.startswith("E1  |") or first_cell.startswith("E1 |"):
                set_row_cell_text(rows[0], 0, "E1  |  Caso Práctico 1: Ponderación de Criterios (AHP vs. BWM)")
                set_row_cell_text(rows[1], 1, "Aplicación y contraste de forma práctica de las metodologías de ponderación multicriterio AHP y BWM para determinar la importancia relativa de los criterios de tu problema logístico real.")
                set_row_cell_text(rows[2], 1, "Reporte técnico con las comparaciones pareadas, cálculo de vectores de pesos y análisis de consistencia.")
                set_row_cell_text(rows[3], 1, "Metodología de ponderación de criterios para el artículo final.")
            elif first_cell.startswith("E2  |") or first_cell.startswith("E2 |"):
                set_row_cell_text(rows[0], 0, "E2  |  Caso Práctico 2: Jerarquización por Distancia (TOPSIS vs. VIKOR vs. EDAS)")
                set_row_cell_text(rows[1], 1, "Jerarquización de las alternativas candidatas del caso de estudio logístico aplicando y comparando tres métodos basados en distancias geométricas (TOPSIS, VIKOR y EDAS).")
                set_row_cell_text(rows[2], 1, "Matriz de decisión resuelta, rankings obtenidos por cada método y análisis comparativo de las lógicas de distancia.")
                set_row_cell_text(rows[3], 1, "Resultados de jerarquización geométrica para el artículo final.")
            elif first_cell.startswith("E3  |") or first_cell.startswith("E3 |"):
                set_row_cell_text(rows[0], 0, "E3  |  Caso Práctico 3: Relaciones de Superación (ELECTRE vs. PROMETHEE)")
                set_row_cell_text(rows[1], 1, "Aplicación de metodologías no compensatorias de outranking (ELECTRE I y PROMETHEE II) para analizar situaciones de veto, incomparabilidad y flujos netos en tu problema de decisión.")
                set_row_cell_text(rows[2], 1, "Umbrales definidos, matrices de concordancia/discordancia, flujos netos y grafo de superación.")
                set_row_cell_text(rows[3], 1, "Resultados del análisis no compensatorio para el artículo final.")
            elif first_cell.startswith("E4  |") or first_cell.startswith("E4 |"):
                set_row_cell_text(rows[0], 0, "E4  |  Caso Práctico 4: Lógica Difusa e Incertidumbre (Fuzzy/GRA)")
                set_row_cell_text(rows[1], 1, "Incorporación de incertidumbre y vaguedad en los juicios cualitativos mediante lógica difusa (Fuzzy TOPSIS) o teoría de sistemas grises (GRA).")
                set_row_cell_text(rows[2], 1, "Definición de variables lingüísticas, TFNs, matriz agregada defuzzificada y ranking resultante.")
                set_row_cell_text(rows[3], 1, "Tratamiento matemático de incertidumbre para el artículo final.")
            elif first_cell.startswith("E5  |") or first_cell.startswith("E5 |"):
                set_row_cell_text(rows[0], 0, "E5  |  Producto Integrador de Aprendizaje (PIA): Artículo de Investigación y Defensa")
                set_row_cell_text(rows[1], 1, "Integración de los avances metodológicos y de análisis de sensibilidad en un manuscrito científico completo estructurado bajo formato de revista indexada y su defensa oral ante panel evaluador.")
                set_row_cell_text(rows[2], 1, "Manuscrito final estructurado (8,000–10,000 palabras) + Presentación ejecutiva + Plan de sometimiento y hoja de ruta de publicación (1 p.).")
                set_row_cell_text(rows[3], 1, "Borrador final de artículo listo para sometimiento + estrategia de publicación.")

    # Modify Table 23 (Cronograma Table)
    tbl_crono = None
    for tbl in tables:
        rows = list(tbl.findall('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}tr'))
        if rows:
            first_cell = "".join([t.text for t in rows[0].iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t') if t.text])
            if first_cell.strip() == "Ses.":
                tbl_crono = tbl
                break

    if tbl_crono is not None:
        rows = list(tbl_crono.findall('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}tr'))
        set_row_cell_text(rows[3], 3, "—")
        set_row_cell_text(rows[5], 3, "E1 — Caso Práctico 1: Ponderación de Criterios")
        set_row_cell_text(rows[6], 3, "—")
        set_row_cell_text(rows[8], 3, "E2 — Caso Práctico 2: Jerarquización por Distancia\n(Inicio formal del PIA)")
        set_row_cell_text(rows[9], 3, "—")
        set_row_cell_text(rows[10], 3, "E3 — Caso Práctico 3: Relaciones de Superación")
        set_row_cell_text(rows[12], 3, "—")
        set_row_cell_text(rows[13], 3, "E4 — Caso Práctico 4: Lógica Difusa e Incertidumbre")
        set_row_cell_text(rows[15], 3, "E5 — Producto Integrador de Aprendizaje (PIA)")

    # Modify Paragraph in text (Pipeline description)
    for p in root.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'):
        text = "".join([t.text for t in p.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t') if t.text])
        if "Las cinco evidencias del curso no son ejercicios académicos" in text:
            new_text = "Los cuatro casos prácticos y el producto integrador de aprendizaje (PIA) no son ejercicios académicos aislados — son los componentes para construir y estructurar una investigación científica aplicada. Cada entregable metodológico prepara al alumno en el dominio de algoritmos multicriterio, sirviendo de base para que a partir de la Sesión 8 se inicie formalmente el Producto Integrador de Aprendizaje (PIA), el cual culmina con un manuscrito completo en formato de artículo científico listo para someter a una revista indexada (Q1/Q2)."
            set_cell_text(p, new_text)

    xml_str = ET.tostring(root, encoding='utf-8')
    
    with zipfile.ZipFile(doc_path, 'r') as doc_in:
        with zipfile.ZipFile(temp_path, 'w') as doc_out:
            for item in doc_in.infolist():
                if item.filename == 'word/document.xml':
                    doc_out.writestr(item, xml_str)
                else:
                    doc_out.writestr(item, doc_in.read(item.filename))
                    
    os.replace(temp_path, doc_path)
    print("Done editing docx successfully!")

if __name__ == '__main__':
    main()
