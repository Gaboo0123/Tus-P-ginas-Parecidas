import streamlit as st
import random

# Base de datos de marcas y nombres similares
SIMILAR_NAMES = {
    "Nike": ["Adidas", "Puma", "Reebok", "Under Armour"],
     "Pepsi": ["Adidas", "Puma", "Reebok", "Under Armour"],
    "Coca-Cola": ["Pepsi", "Dr Pepper", "Fanta", "Sprite"],
    "Apple": ["Samsung", "Google", "Huawei", "Microsoft"],
    "McDonald's": ["Burger King", "Wendy's", "KFC", "Taco Bell"],
    "Ford": ["Chevrolet", "Toyota", "Honda", "Nissan"]
}

def get_similar_names(name):
    """Obtiene nombres similares basados en la base de datos."""
    name = name.strip().title()  # Normaliza el nombre
    return SIMILAR_NAMES.get(name, ["No se encontraron sugerencias"])

# Configuración de la página
st.set_page_config(page_title="Generador de Nombres Similares", layout="centered")
st.title("🔍 Generador de Nombres Similares")

# Input del usuario
user_input = st.text_input("Escribe un nombre de marca o empresa:")

if user_input:
    suggestions = get_similar_names(user_input)
    st.subheader("Sugerencias:")
    for suggestion in suggestions:
        st.write(f"✅ {suggestion}")

# Mensaje de footer
st.markdown("---")
st.markdown("Desarrollado con ❤️ usando Streamlit")
