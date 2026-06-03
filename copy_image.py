import os

src = "/Users/leonardohernandez/.gemini/antigravity-ide/brain/de709e7a-e678-4ebe-ba71-44570bcbf700/mcdm_logistics_cover_1779483820819.png"
dst = "/Users/leonardohernandez/MULTICRITERIO_DOCTORADO/Diapositivas/img/mcdm_logistics_cover.png"

try:
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    with open(src, 'rb') as f_src:
        data = f_src.read()
    with open(dst, 'wb') as f_dst:
        f_dst.write(data)
    print("¡Éxito! La imagen de portada se copió a Diapositivas/img/mcdm_logistics_cover.png")
except Exception as e:
    print(f"Error al copiar la imagen: {e}")
