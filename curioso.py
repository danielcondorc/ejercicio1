import streamlit as st
from PIL import Image, ImageDraw, ImageFont

# Título
st.title("Explorador de Anatomía Humana")

# Carga de imagen
image_path = "images/anatomia.png"
image = Image.open(image_path)

# Mostrar imagen
st.image(image, caption="Imagen de la Anatomía Humana", use_column_width=True)

# Lista de partes del cuerpo (puedes expandir esto)
partes = {
    "Cabeza": (150, 50),
    "Corazón": (160, 220),
    "Hígado": (170, 270),
    "Estómago": (180, 320),
    "Pierna derecha": (200, 450),
    "Pierna izquierda": (140, 450)
}

# Selección de parte a señalar
parte = st.selectbox("Selecciona una parte del cuerpo:", list(partes.keys()))

# Procesar imagen con etiqueta
if parte:
    coords = partes[parte]
    imagen_etiquetada = image.copy()
    draw = ImageDraw.Draw(imagen_etiquetada)

    # Caja de texto con fondo negro y letra amarilla
    texto = parte
    font = ImageFont.load_default()
    text_size = draw.textsize(texto, font=font)
    box_position = (coords[0], coords[1], coords[0] + text_size[0] + 10, coords[1] + text_size[1] + 10)

    draw.rectangle(box_position, fill="black")
    draw.text((coords[0] + 5, coords[1] + 5), texto, fill="yellow", font=font)

    st.image(imagen_etiquetada, caption=f"Parte señalada: {parte}", use_column_width=True)
