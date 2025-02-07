import streamlit as st
import random

# Base de datos de marcas y nombres similares
SIMILAR_NAMES = {
    "Nike": ["Adidas", "Puma", "Reebok", "Under Armour"],
     "Adidas": ["Nike", "Puma", "Reebok", "Under Armour"],
     "Puma": ["Adidas", "Nike", "Reebok", "Under Armour"],
     "Reebok": ["Adidas", "Puma", "Nike", "Under Armour"],
     "Under Armour": ["Adidas", "Puma", "Reebok", "Nike"],
    "Coca-Cola": ["Pepsi", "Dr Pepper", "Fanta", "Sprite"],
    "Pepsi": ["Coca-Cola", "Dr Pepper", "Fanta", "Sprite"],
    "Dr Pepper": ["Pepsi", "Coca-Cola", "Fanta", "Sprite"],
    "Fanta": ["Pepsi", "Dr Pepper", "Coca-Cola", "Sprite"],
    "Sprite": ["Pepsi", "Dr Pepper", "Fanta", "Sprite"],
    "Apple": ["Samsung", "Google", "Huawei", "Microsoft"],
    "Samsung": ["Apple", "Google", "Huawei", "Microsoft"],
    "Google": ["Samsung", "Apple", "Huawei", "Microsoft"],
    "Huawei": ["Samsung", "Google", "Apple", "Microsoft"],
    "Microsoft": ["Samsung", "Google", "Huawei", "Apple"],
    "Burger King": ["McDonalds", "Wendy's", "KFC", "Popeyes"],
    "Wendys": ["Burger King", "McDonalds", "KFC", "Popeyes"],
    "KFC": ["Burger King", "Wendy's", "McDonalds", "Popeyes"],
    "Popeyes": ["Burger King", "Wendy's", "KFC", "McDonalds"],
    "McDonald's": ["Burger King", "Wendy's", "KFC", "Popeyes"],
    "Ford": ["Subaru", "Toyota", "Honda", "Nissan"]
    "Subaru": ["Ford", "Toyota", "Honda", "Nissan"]
    "Toyota": ["Subaru", "Ford", "Honda", "Nissan"]
    "Honda": ["Subaru", "Toyota", "Ford", "Nissan"]
    "Nissan": ["Subaru", "Toyota", "Honda", "Ford"]
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
