import zipfile
import xml.etree.ElementTree as ET

namespaces = {
    'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
}

def inspect_xml():
    doc_path = 'Programa_Doctorado_MCDM_Logistica_FIME_UANL_2_actualizado.docx'
    with zipfile.ZipFile(doc_path) as docx:
        xml_content = docx.read('word/document.xml')
        root = ET.fromstring(xml_content)
        
        # Let's print paragraphs containing "Evidencia" or "E1"
        count = 0
        for p in root.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'):
            text = "".join([t.text for t in p.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t') if t.text])
            if "Evidencia" in text or "E1" in text or "E2" in text or "E3" in text or "E4" in text or "E5" in text:
                print(f"P_TEXT: {text}")
                count += 1
                if count > 50:
                    break

if __name__ == '__main__':
    inspect_xml()
