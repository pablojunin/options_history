import pandas as pd
from open_byma.open_byma import openBYMAdata
from datetime import datetime
    
# Crear una instancia de la clase
byma_data = openBYMAdata()

# Verificar si es día hábil
if byma_data.isworkingDay():
    print("Obteniendo datos del cierre del día para las opciones...")

    # Obtener datos de todas las opciones
    options_df = byma_data.get_options()

    # Mostrar las primeras filas del DataFrame
    print("Datos de Opciones del Cierre del Día:")
    print(options_df.head())

    # Obtener la fecha actual en formato YYYY-MM-DD
    fecha_hoy = datetime.now().strftime("%Y-%m-%d")

    # Crear el nombre del archivo con la fecha
    nombre_archivo = f"opciones_cierre_{fecha_hoy}.csv"

    # Guardar el DataFrame en el archivo CSV
    options_df.to_csv(nombre_archivo, index=False)

else:
    print("Hoy no es día hábil de mercado.")
