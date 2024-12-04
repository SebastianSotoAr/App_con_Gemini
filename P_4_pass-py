import streamlit as st
import re

def analizar_contrasena(contrasena):
    """Analiza una contraseña para determinar si parece generada por Google o Apple.

    Args:
        contrasena (str): La contraseña a analizar.

    Returns:
        str: Un mensaje indicando el resultado del análisis.
    """

    # Patrones simplificados para demostración (a ajustar)
    patron_google = r"^[a-z]{6}\d{2}$"  # Ejemplo: abcdef12
    patron_apple = r"^[A-Z]\d{5}[a-z]$"  # Ejemplo: A12345a

    if re.match(patron_google, contrasena):
        return "La contraseña parece generada por Google."
    elif re.match(patron_apple, contrasena):
        return "La contraseña parece generada por Apple."
    else:
        return "No se pudo determinar el origen de la contraseña."

# Título de la app
st.title("Detector de Contraseñas Automáticas")

# Autores
st.write("Creado por: Sebastián Soto Arcila y Gemini")

# Descripción
st.write("Esta aplicación intenta determinar si una contraseña fue generada automáticamente por Google o Apple.")

# Campo de texto para la contraseña
contrasena = st.text_input("Ingrese la contraseña")

# Botón para analizar
if st.button("Analizar"):
    resultado = analizar_contrasena(contrasena)
    st.write(resultado)
