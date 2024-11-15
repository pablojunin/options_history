import pandas as pd
from datetime import datetime

# https://open.bymadata.com.ar/#/options
nombre_archivo = "opciones_historial.csv"

# Verificar si el archivo existe y cargar los datos
try:
    # Cargar el archivo CSV en un DataFrame
    opciones_df = pd.read_csv(nombre_archivo)

    # Convertir las columnas de fecha y vencimiento a formato datetime
    opciones_df['date'] = pd.to_datetime(opciones_df['date'])
    opciones_df['expiration'] = pd.to_datetime(opciones_df['expiration'])

    # Mostrar información general del DataFrame
    print("Datos cargados exitosamente.")
    print(f"Total de registros: {len(opciones_df)}")
    print(opciones_df.info())

    # Configurar Pandas para mostrar todas las filas y columnas
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)

    # Mostrar el DataFrame completo
    print(opciones_df)


except FileNotFoundError:
    print(f"Error: No se encontró el archivo '{nombre_archivo}'. Asegúrate de que el archivo exista en la carpeta actual.")

except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
