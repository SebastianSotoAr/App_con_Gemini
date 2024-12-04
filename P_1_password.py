import streamlit as st
import re

def evaluar_contrasena(contrasena):
    """Evalúa la fortaleza de una contraseña.

    Args:
        contrasena (str): La contraseña a evaluar.

    Returns:
        str: Un mensaje indicando la fortaleza de la contraseña y sugerencias.
    """

    # Definimos las expresiones regulares para cada criterio
    mayuscula = re.compile(r'[A-Z]')
    minuscula = re.compile(r'[a-z]')
    numero = re.compile(r'\d')
    especial = re.compile(r'[^a-zA-Z0-9]')

    # Evaluamos cada criterio
    tiene_mayuscula = bool(mayuscula.search(contrasena))
    tiene_minuscula = bool(minuscula.search(contrasena))
    tiene_numero = bool(numero.search(contrasena))
    tiene_especial = bool(especial.search(contrasena))
    es_suficientemente_larga = len(contrasena) >= 8

    # Mensaje a mostrar según los resultados
    if all([tiene_mayuscula, tiene_minuscula, tiene_numero, tiene_especial, es_suficientemente_larga]):
        return "Excelente! Tu contraseña es muy segura."
    else:
        sugerencias = []
        if not es_suficientemente_larga:
            sugerencias.append("La contraseña debe tener al menos 8 caracteres.")
        if not tiene_mayuscula:
            sugerencias.append("Incluye al menos una letra mayúscula.")
        if not tiene_minuscula:
            sugerencias.append("Incluye al menos una letra minúscula.")
        if not tiene_numero:
            sugerencias.append("Incluye al menos un número.")
        if not tiene_especial:
            sugerencias.append("Incluye al menos un carácter especial.")
        return "Tu contraseña podría ser más fuerte. Sugerencias: " + ", ".join(sugerencias)

# Título de la app
st.title("Evaluador de Contraseñas")

# Autores
st.write("Creado por: Sebastián Soto Arcila y Gemini")

# Descripción
st.write("Esta aplicación te ayudará a evaluar la fortaleza de tu contraseña y te dará sugerencias para mejorarla.")

# Campo de texto para la contraseña
contrasena = st.text_input("Ingrese su contraseña")

# Botón para evaluar la contraseña
if st.button("Evaluar"):
    resultado = evaluar_contrasena(contrasena)
    st.write(resultado)
