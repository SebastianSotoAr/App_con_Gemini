import streamlit as st
import re

def validar_nombre(nombre):
    """Valida si un nombre solo contiene caracteres alfabéticos y comienza con mayúscula."""
    patron = r"^[A-Z][a-zA-Z]+$"
    return bool(re.match(patron, nombre))

def validar_email(email):
    """Valida una dirección de correo electrónico."""
    patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(patron, email))

def validar_telefono(telefono):
    """Valida un número de teléfono (ejemplo: +573112345678)."""
    patron = r"^\+\d{10,13}$"  # Ajusta el patrón según los formatos de teléfono requeridos
    return bool(re.match(patron, telefono))

def validar_fecha(fecha):
    """Valida una fecha en formato DD/MM/AAAA."""
    patron = r"^\d{2}/\d{2}/\d{4}$"
    return bool(re.match(patron, fecha))

# Título de la app
st.title("Validador de Formularios")

# Autores
st.write("Creado por: Sebastián Soto Arcila y Gemini")

# Descripción
st.write("Esta aplicación valida la información ingresada en un formulario.")

# Campos de entrada
nombre = st.text_input("Nombre")
email = st.text_input("Correo electrónico")
telefono = st.text_input("Teléfono")
fecha = st.text_input("Fecha (DD/MM/AAAA)")

# Botón para validar
if st.button("Validar"):
    if validar_nombre(nombre):
        st.success("El nombre es válido.")
    else:
        st.error("El nombre debe comenzar con mayúscula y solo contener letras.")

    if validar_email(email):
        st.success("El correo electrónico es válido.")
    else:
        st.error("El correo electrónico no es válido.")

    if validar_telefono(telefono):
        st.success("El número de teléfono es válido.")
    else:
        st.error("El número de teléfono no es válido.")

    if validar_fecha(fecha):
        st.success("La fecha es válida.")
    else:
        st.error("La fecha no es válida.")
