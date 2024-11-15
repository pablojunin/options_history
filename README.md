# Proyecto Argentum Data Bot 🐍

## Descripción
Este es un proyecto **beta** implementado en Python, cuyo objetivo es automatizar la recopilación y almacenamiento del historial diario de las opciones del MERVAL, obteniendo los datos de **BYMA Data**.

### Características
- Implementado en Python.
- Recopila y guarda datos de las opciones del MERVAL.
- Genera archivos de respaldo (`backup`) con los datos históricos para evitar pérdida de información.
- Permite visualizar el historial recopilado.

## Aplicaciones
El proyecto cuenta con dos aplicaciones principales:

1. **argentumDataBotOptions.py**
   - Obtiene los datos de opciones del mercado de BYMA Data y los guarda en el archivo `opciones_historial.csv`.
   - Realiza automáticamente un respaldo (`backup`) del archivo `opciones_historial.csv` para evitar pérdida de datos.
   - Uso en Windows: Ejecutar a través del archivo `argentumDataBotOptions.bat`.

2. **argentumDataViewer.py**
   - Permite visualizar el archivo `opciones_historial.csv` con los datos recopilados.
   - Uso en Windows: Ejecutar a través del archivo `argentumDataViewer.bat`.

### Cómo usar
Para ejecutar las aplicaciones en un entorno Windows:

```bash
# Para recopilar datos
argentumDataBotOptions.bat

# Para visualizar el historial
argentumDataViewer.bat
