import streamlit as st
import pandas as pd
import re
import openpyxl

def procesar_csv(url_csv):
    """Procesa un archivo CSV, valida los datos y genera un archivo Excel.

    Args:
        url_csv (str): URL del archivo CSV.
    """

    # Leer el archivo CSV
    df = pd.read_csv(url_csv)

    # Aquí puedes agregar lógica para validar los datos usando expresiones regulares
    # Por ejemplo:
    # df['Nombre del producto'] = df['Nombre del producto'].apply(lambda x: validar_nombre(x))

    # Crear un nuevo DataFrame con la estructura deseada
    df_excel = pd.DataFrame({
        'Número de serie del producto': df['Número de serie del producto'],
        'Nombre del producto': df['Nombre del producto'],
        'Valor': df['Valor'],
        'Fecha de compra': df['Fecha de compra'],
        # ... agregar más columnas según sea necesario
    })

    # Guardar el DataFrame como un archivo Excel
    df_excel.to_excel('resultado.xlsx', index=False)

# Título de la app
st.title("Procesador de CSV a Excel")

# Autores
st.write("Creado por: Sebastián Soto Arcila y Gemini")

# Descripción
st.write("Esta aplicación procesa un archivo CSV y genera un archivo Excel con los datos formateados.")

# URL del archivo CSV
url_csv = st.text_input("Ingrese la URL del archivo CSV", value="https://raw.githubusercontent.com/gabrielawad/programacion-para-ingenieria/refs/heads/main/archivos-datos/regex/regex_productos.csv")

# Botón para procesar
if st.button("Procesar"):
    procesar_csv(url_csv)
    st.success("¡Archivo Excel generado exitosamente!")
