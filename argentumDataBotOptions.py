from datetime import datetime, timedelta
import pandas as pd
from open_byma.open_byma import openBYMAdata
import shutil
import sys

byma_data = openBYMAdata()

# Verificar si es día hábil
if byma_data.isworkingDay():
    print("Obteniendo datos del cierre del día para las opciones...")

    options_df = byma_data.get_options()

    # Agregar la fecha actual como columna en el DataFrame
    # fecha_hoy = datetime.now().strftime("%Y-%m-%d")
    # options_df['date'] = fecha_hoy
    
    # Obtener la fecha de ayer
    fecha_ayer = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
    options_df['date'] = fecha_ayer
    fecha_hoy = fecha_ayer
    
    # Nombre del archivo CSV con los datos acumulados
    nombre_archivo = "opciones_historial.csv"

    # Realizar backup del archivo antes de modificarlo
    backup_nombre = f"opciones_historial_backup_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.csv"
    
    try:
        # Hacer una copia de seguridad del archivo
        shutil.copy(nombre_archivo, backup_nombre)
        print(f"Backup realizado: '{backup_nombre}'")
    except FileNotFoundError:
        print(f"No se encontró el archivo '{nombre_archivo}', no se realizó backup.")
        
    # Verificar si el archivo ya existe
    try:
        # Cargar los datos previos
        datos_acumulados = pd.read_csv(nombre_archivo)

        # Filtrar para ver si ya existen datos para la fecha actual
        if fecha_hoy in datos_acumulados['date'].values:
            print(f"Los datos para la fecha {fecha_hoy} ya están registrados. No se agregarán duplicados.")
            sys.exit()
        else:
            # Concatenar los datos nuevos con los existentes
            datos_acumulados = pd.concat([datos_acumulados, options_df], ignore_index=True)
            # Guardar el DataFrame actualizado
            datos_acumulados.to_csv(nombre_archivo, index=False)
            print(f"Datos nuevos agregados y guardados en '{nombre_archivo}'.")
            
    except FileNotFoundError:
        # Si el archivo no existe, guardar el DataFrame actual
        options_df.to_csv(nombre_archivo, index=False)
        print(f"Archivo '{nombre_archivo}' creado con los datos del día.")

    # Mostrar una vista previa del DataFrame actualizado
    print(options_df.head())

else:
    print("Hoy no es día hábil de mercado.")
