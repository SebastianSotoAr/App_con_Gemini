import streamlit as st
import re

# Configuración de la página
st.set_page_config(
    page_title="Evaluador de Contraseñas",
    page_icon="",
    layout="wide"
)

# Estilos CSS (inspirados en Pornhub, ajustar según sea necesario)
st.markdown("""
<style>
.stApp {
    font-family: Arial, sans-serif;
    background-color: #191919;
    color: #fff;
}
.stTitle {
    font-size: 36px;
    text-align: center;
    color: #f44336;
}
.stText {
    font-size: 18px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# Título y autores
st.title("Evaluador de Contraseñas ")
st.text("Creado por: Gemini y Sebastián Soto Arcila")

# Descripción
st.write("""
Esta aplicación te ayudará a evaluar la fortaleza de tu contraseña. 
Una contraseña segura debe tener al menos 8 caracteres, incluyendo mayúsculas, minúsculas, números y caracteres especiales.
""")

# Campo de entrada y botón
password = st.text_input("Ingrese su contraseña:")
if st.button("Evaluar"):
    # Expresiones regulares para verificar los criterios
    has_upper = re.search(r"[A-Z]", password)
    has_lower = re.search(r"[a-z]", password)
    has_number = re.search(r"\d", password)
    has_special = re.search(r"[^\w\s]", password)

    # Evaluación de la contraseña
    if len(password) >= 8 and has_upper and has_lower and has_number and has_special:
        st.success("¡Excelente! Tu contraseña es muy segura.")
    else:
        st.error("Tu contraseña es débil. Considera incluir:")
        if len(password) < 8:
            st.write("- Al menos 8 caracteres")
        if not has_upper:
            st.write("- Al menos una letra mayúscula")
        if not has_lower:
            st.write("- Al menos una letra minúscula")
        if not has_number:
            st.write("- Al menos un número")
        if not has_special:
            st.write("- Al menos un carácter especial")
