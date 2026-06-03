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
    
    # 1. Modify Table 2 (Session 3)
    # TABLE 2 is Session 3.
    tables = list(root.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}tbl'))
    print(f"Total tables found: {len(tables)}")
    
    # Let's find tables by Session title
    session_tables = {}
    for table_idx, tbl in enumerate(tables):
        first_cell = ""
        for tc in tbl.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}tc'):
            first_cell = "".join([t.text for t in tc.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t') if t.text])
            break
        if "Sesión" in first_cell:
            session_tables[first_cell] = tbl
            print(f"Session Table: {first_cell} is Table {table_idx}")

    # Let's helper-get session table by prefix
    def get_sess_tbl(prefix):
        for name, tbl in session_tables.items():
            if name.startswith(prefix):
                return tbl
        return None

    # Helper to set cell text in row
    def set_row_cell_text(tr, cell_idx, text):
        tcs = list(tr.findall('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}tc'))
        if cell_idx < len(tcs):
            set_cell_text(tcs[cell_idx], text)

    # Helper to get row by first cell text
    def get_row_by_label(tbl, label):
        for tr in tbl.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}tr'):
            tcs = list(tr.findall('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}tc'))
            if tcs:
                cell_text = "".join([t.text for t in tcs[0].iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t') if t.text])
                if cell_text.strip() == label:
                    return tr
        return None

    # Table edits for sessions:
    # Sesión 3: change Entregable row value to '—'
    tbl_s3 = get_sess_tbl("Sesión 3:")
    if tbl_s3 is not None:
        tr = get_row_by_label(tbl_s3, "Entregable")
        if tr is not None:
            set_row_cell_text(tr, 1, "—")
            print("Modified Session 3 Entregable")

    # Sesión 5: append Entregable row
    tbl_s5 = get_sess_tbl("Sesión 5:")
    if tbl_s5 is not None:
        # copy last row
        rows = list(tbl_s5.findall('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}tr'))
        new_tr = copy.deepcopy(rows[-1])
        set_row_cell_text(new_tr, 0, "Entregable")
        set_row_cell_text(new_tr, 1, "E1 — Caso Práctico 1: Ponderación de Criterios (AHP vs. BWM)")
        tbl_s5.append(new_tr)
        print("Appended Session 5 Entregable")

    # Sesión 6: change to '—' or remove the Entregable row. Actually change to '—' is cleaner
    tbl_s6 = get_sess_tbl("Sesión 6:")
    if tbl_s6 is not None:
        tr = get_row_by_label(tbl_s6, "Entregable")
        if tr is not None:
            set_row_cell_text(tr, 1, "—")
            print("Modified Session 6 Entregable")

    # Sesión 8: append Entregable row
    tbl_s8 = get_sess_tbl("Sesión 8:")
    if tbl_s8 is not None:
        # copy last row
        rows = list(tbl_s8.findall('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}tr'))
        new_tr = copy.deepcopy(rows[-1])
        set_row_cell_text(new_tr, 0, "Entregable")
        set_row_cell_text(new_tr, 1, "E2 — Caso Práctico 2: Jerarquización por Distancia (TOPSIS vs. VIKOR vs. EDAS) (Inicio formal del PIA)")
        tbl_s8.append(new_tr)
        print("Appended Session 8 Entregable")

    # Sesión 9: change to '—'
    tbl_s9 = get_sess_tbl("Sesión 9:")
    if tbl_s9 is not None:
        tr = get_row_by_label(tbl_s9, "Entregable")
        if tr is not None:
            set_row_cell_text(tr, 1, "—")
            print("Modified Session 9 Entregable")

    # Sesión 10: append Entregable row
    tbl_s10 = get_sess_tbl("Sesión 10:")
    if tbl_s10 is not None:
        rows = list(tbl_s10.findall('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}tr'))
        new_tr = copy.deepcopy(rows[-1])
        set_row_cell_text(new_tr, 0, "Entregable")
        set_row_cell_text(new_tr, 1, "E3 — Caso Práctico 3: Relaciones de Superación (ELECTRE vs. PROMETHEE)")
        tbl_s10.append(new_tr)
        print("Appended Session 10 Entregable")

    # Sesión 12: change to '—'
    tbl_s12 = get_sess_tbl("Sesión 12:")
    if tbl_s12 is not None:
        tr = get_row_by_label(tbl_s12, "Entregable")
        if tr is not None:
            set_row_cell_text(tr, 1, "—")
            print("Modified Session 12 Entregable")

    # Sesión 13: append Entregable row
    tbl_s13 = get_sess_tbl("Sesión 13:")
    if tbl_s13 is not None:
        rows = list(tbl_s13.findall('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}tr'))
        new_tr = copy.deepcopy(rows[-1])
        set_row_cell_text(new_tr, 0, "Entregable")
        set_row_cell_text(new_tr, 1, "E4 — Caso Práctico 4: Lógica Difusa e Incertidumbre (Fuzzy/GRA)")
        tbl_s13.append(new_tr)
        print("Appended Session 13 Entregable")

    # Sesión 15: modify Entregable row to E5 - PIA
    tbl_s15 = get_sess_tbl("Sesión 15:")
    if tbl_s15 is not None:
        tr = get_row_by_label(tbl_s15, "Entregable")
        if tr is not None:
            set_row_cell_text(tr, 1, "E5 — Producto Integrador de Aprendizaje (PIA): Artículo de Investigación y Defensa")
            print("Modified Session 15 Entregable")

    # 2. Modify Table 16 (Main Evaluation Table)
    # Let's find it by row header
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
        print("Modified Main Evaluation Table (Table 16)")

    # 3. Modify Descriptions Tables (Tables 17-21)
    # Let's find them by their first row contents
    for tbl in tables:
        rows = list(tbl.findall('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}tr'))
        if rows:
            first_cell = "".join([t.text for t in rows[0].iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t') if t.text])
            if first_cell.startswith("E1  |"):
                set_row_cell_text(rows[0], 0, "E1  |  Caso Práctico 1: Ponderación de Criterios (AHP vs. BWM)")
                set_row_cell_text(rows[1], 1, "Aplicación y contraste de forma práctica de las metodologías de ponderación multicriterio AHP y BWM para determinar la importancia relativa de los criterios de tu problema logístico real.")
                set_row_cell_text(rows[2], 1, "Reporte técnico con las comparaciones pareadas, cálculo de vectores de pesos y análisis de consistencia.")
                set_row_cell_text(rows[3], 1, "Metodología de ponderación de criterios para el artículo final.")
                print("Modified E1 Table")
            elif first_cell.startswith("E2  |"):
                set_row_cell_text(rows[0], 0, "E2  |  Caso Práctico 2: Jerarquización por Distancia (TOPSIS vs. VIKOR vs. EDAS)")
                set_row_cell_text(rows[1], 1, "Jerarquización de las alternativas candidatas del caso de estudio logístico aplicando y comparando tres métodos basados en distancias geométricas (TOPSIS, VIKOR y EDAS).")
                set_row_cell_text(rows[2], 1, "Matriz de decisión resuelta, rankings obtenidos por cada método y análisis comparativo de las lógicas de distancia.")
                set_row_cell_text(rows[3], 1, "Resultados de jerarquización geométrica para el artículo final.")
                print("Modified E2 Table")
            elif first_cell.startswith("E3  |"):
                set_row_cell_text(rows[0], 0, "E3  |  Caso Práctico 3: Relaciones de Superación (ELECTRE vs. PROMETHEE)")
                set_row_cell_text(rows[1], 1, "Aplicación de metodologías no compensatorias de outranking (ELECTRE I y PROMETHEE II) para analizar situaciones de veto, incomparabilidad y flujos netos en tu problema de decisión.")
                set_row_cell_text(rows[2], 1, "Umbrales definidos, matrices de concordancia/discordancia, flujos netos y grafo de superación.")
                set_row_cell_text(rows[3], 1, "Resultados del análisis no compensatorio para el artículo final.")
                print("Modified E3 Table")
            elif first_cell.startswith("E4  |"):
                set_row_cell_text(rows[0], 0, "E4  |  Caso Práctico 4: Lógica Difusa e Incertidumbre (Fuzzy/GRA)")
                set_row_cell_text(rows[1], 1, "Incorporación de incertidumbre y vaguedad en los juicios cualitativos mediante lógica difusa (Fuzzy TOPSIS) o teoría de sistemas grises (GRA).")
                set_row_cell_text(rows[2], 1, "Definición de variables lingüísticas, TFNs, matriz agregada defuzzificada y ranking resultante.")
                set_row_cell_text(rows[3], 1, "Tratamiento matemático de incertidumbre para el artículo final.")
                print("Modified E4 Table")
            elif first_cell.startswith("E5  |"):
                set_row_cell_text(rows[0], 0, "E5  |  Producto Integrador de Aprendizaje (PIA): Artículo de Investigación y Defensa")
                set_row_cell_text(rows[1], 1, "Integración de los avances metodológicos y de análisis de sensibilidad en un manuscrito científico completo estructurado bajo formato de revista indexada y su defensa oral ante panel evaluador.")
                set_row_cell_text(rows[2], 1, "Manuscrito final estructurado (8,000–10,000 palabras) + Presentación ejecutiva + Plan de sometimiento y hoja de ruta de publicación (1 p.).")
                set_row_cell_text(rows[3], 1, "Borrador final de artículo listo para sometimiento + estrategia de publicación.")
                print("Modified E5 Table")

    # 4. Modify Table 23 (Cronograma Table)
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
        # Session 3 (Row 3): E1 -> '—'
        set_row_cell_text(rows[3], 3, "—")
        # Session 5 (Row 5): '—' -> 'E1 — Caso Práctico 1: Ponderación de Criterios'
        set_row_cell_text(rows[5], 3, "E1 — Caso Práctico 1: Ponderación de Criterios")
        # Session 6 (Row 6): E2 -> '—'
        set_row_cell_text(rows[6], 3, "—")
        # Session 8 (Row 8): '—' -> 'E2 — Caso Práctico 2: Jerarquización por Distancia (Inicio del PIA)'
        set_row_cell_text(rows[8], 3, "E2 — Caso Práctico 2: Jerarquización por Distancia\n(Inicio formal del PIA)")
        # Session 9 (Row 9): E3 -> '—'
        set_row_cell_text(rows[9], 3, "—")
        # Session 10 (Row 10): '—' -> 'E3 — Caso Práctico 3: Relaciones de Superación'
        set_row_cell_text(rows[10], 3, "E3 — Caso Práctico 3: Relaciones de Superación")
        # Session 12 (Row 12): E4 -> '—'
        set_row_cell_text(rows[12], 3, "—")
        # Session 13 (Row 13): '—' -> 'E4 — Caso Práctico 4: Lógica Difusa e Incertidumbre'
        set_row_cell_text(rows[13], 3, "E4 — Caso Práctico 4: Lógica Difusa e Incertidumbre")
        # Session 15 (Row 15): E5 -> 'E5 — Producto Integrador de Aprendizaje (PIA)'
        set_row_cell_text(rows[15], 3, "E5 — Producto Integrador de Aprendizaje (PIA)")
        print("Modified Cronograma Table (Table 23)")

    # 5. Modify Paragraph in text (Pipeline description)
    for p in root.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'):
        text = "".join([t.text for t in p.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t') if t.text])
        if "Las cinco evidencias del curso no son ejercicios académicos" in text:
            # Replace paragraph text preserving first run properties
            new_text = "Los cuatro casos prácticos y el producto integrador de aprendizaje (PIA) no son ejercicios académicos aislados — son los componentes para construir y estructurar una investigación científica aplicada. Cada entregable metodológico prepara al alumno en el dominio de algoritmos multicriterio, sirviendo de base para que a partir de la Sesión 8 se inicie formalmente el Producto Integrador de Aprendizaje (PIA), el cual culmina con un manuscrito completo en formato de artículo científico listo para someter a una revista indexada (Q1/Q2)."
            set_cell_text(p, new_text)
            print("Modified Pipeline text paragraph")

    # Print modified XML to stdout
    print("=== XML START ===")
    print(ET.tostring(root, encoding='utf-8').decode('utf-8'))
    print("=== XML END ===")
    import time
    time.sleep(2)

if __name__ == '__main__':
    main()
