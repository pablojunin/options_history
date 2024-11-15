import pandas as pd
from open_byma.open_byma import openBYMAdata


# Crear una instancia de la clase
byma_data = openBYMAdata()

# Verificar si es día hábil
if byma_data.isworkingDay():
    print("Hoy es día hábil de mercado.")

    # Obtener datos de índices
    indices_df = byma_data.indices()
    print("Datos de Índices:")
    print(indices_df)

    # Obtener datos de Blue Chips
    bluechips_df = byma_data.get_bluechips()
    print("Datos de Blue Chips:")
    print(bluechips_df)

    # Obtener datos de CEDEARs
    cedears_df = byma_data.get_cedears()
    print("Datos de CEDEARs:")
    print(cedears_df)

    # Obtener datos de futuros
    futures_df = byma_data.get_futures()
    print("Datos de Futuros:")
    print(futures_df)
    
    # Mostrar los DataFrames
    print("Mostrando datos de Índices:")
    print(indices_df.head())

    print("Mostrando datos de Blue Chips:")
    print(bluechips_df.head())

    print("Mostrando datos de CEDEARs:")
    print(cedears_df.head())

    print("Mostrando datos de Futuros:")
    print(futures_df.head())
else:
    print("Hoy no es día hábil de mercado.")
