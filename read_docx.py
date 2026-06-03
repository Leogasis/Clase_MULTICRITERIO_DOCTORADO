import zipfile
import xml.etree.ElementTree as ET
import os

def get_docx_text(path):
    """
    Extract text from a docx file using xml parser.
    """
    try:
        namespaces = {
            'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
        }
        with zipfile.ZipFile(path) as docx:
            tree = ET.parse(docx.open('word/document.xml'))
            root = tree.getroot()
            text_list = []
            for paragraph in root.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'):
                p_text = []
                for run in paragraph.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t'):
                    if run.text:
                        p_text.append(run.text)
                if p_text:
                    text_list.append(''.join(p_text))
            return '\n'.join(text_list)
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    doc_path = '/Users/leonardohernandez/Academica/MULTICRITERIO_DOCTORADO/Programa_Doctorado_MCDM_Logistica_FIME_UANL_2_actualizado.docx'
    txt = get_docx_text(doc_path)
    with open('/Users/leonardohernandez/Academica/MULTICRITERIO_DOCTORADO/Programa_text.txt', 'w') as f:
        f.write(txt)
    print("Done")
