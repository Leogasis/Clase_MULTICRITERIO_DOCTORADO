import os
try:
    os.makedirs("Diapositivas/img", exist_ok=True)
    print("Directory Diapositivas/img created successfully:", os.path.exists("Diapositivas/img"))
except Exception as e:
    print("Error creating directory:", e)

