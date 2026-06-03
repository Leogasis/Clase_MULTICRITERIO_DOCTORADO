import zipfile
import xml.etree.ElementTree as ET

def inspect_session_tables():
    doc_path = 'Programa_Doctorado_MCDM_Logistica_FIME_UANL_2_actualizado.docx'
    with zipfile.ZipFile(doc_path) as docx:
        xml_content = docx.read('word/document.xml')
        root = ET.fromstring(xml_content)
        
        for table_idx, tbl in enumerate(root.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}tbl')):
            first_cell = ""
            for tc in tbl.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}tc'):
                first_cell = "".join([t.text for t in tc.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t') if t.text])
                break
            if "Sesión" in first_cell:
                print(f"Table {table_idx}: {first_cell}")
                for row_idx, tr in enumerate(tbl.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}tr')):
                    cells = []
                    for tc in tr.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}tc'):
                        cell_text = "".join([t.text for t in tc.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t') if t.text])
                        cells.append(cell_text)
                    print(f"  Row {row_idx}: {cells}")

if __name__ == '__main__':
    inspect_session_tables()
