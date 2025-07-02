import pandas as pd
import tabula

# Cambia esta ruta al nombre del archivo que descargaste (debes tenerlo en la misma carpeta)
archivo_pdf = "rptcotizaCOTIZA-20250701120711-49023186592840.pdf"

# Extrae las tablas del PDF
print("Extrayendo tablas desde el PDF...")
tablas = tabula.read_pdf(archivo_pdf, pages='all', multiple_tables=True)

# Une todas las tablas en un solo DataFrame
df_total = pd.concat(tablas, ignore_index=True)

# Guarda el resultado en un archivo Excel
nombre_salida = "cotizaciones_afp.xlsx"
df_total.to_excel(nombre_salida, index=False)

print(f"¡Listo! Archivo guardado como: {nombre_salida}")
