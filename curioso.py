import streamlit as st
import cv2
import numpy as np
import mediapipe as mp
from PIL import Image, ImageDraw, ImageFont

# Configurar página
st.set_page_config(page_title="Anatomía Humana", layout="centered")
st.title("Explorador de Anatomía Humana")

# Subida de imagen
uploaded_file = st.file_uploader("Sube una imagen de cuerpo humano:", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    st.image(image_rgb, caption="Imagen original", use_column_width=True)

    # MediaPipe Pose
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose(static_image_mode=True)
    results = pose.process(image_rgb)

    if results.pose_landmarks:
        annotated_image = image_rgb.copy()
        draw = ImageDraw.Draw(Image.fromarray(annotated_image))

        # Diccionario de puntos claves (ejemplo limitado)
        partes = {
            "Cabeza": mp_pose.PoseLandmark.NOSE,
            "Hombro derecho": mp_pose.PoseLandmark.RIGHT_SHOULDER,
            "Hombro izquierdo": mp_pose.PoseLandmark.LEFT_SHOULDER,
            "Cadera": mp_pose.PoseLandmark.LEFT_HIP,
            "Rodilla izquierda": mp_pose.PoseLandmark.LEFT_KNEE,
            "Rodilla derecha": mp_pose.PoseLandmark.RIGHT_KNEE,
        }

        pil_image = Image.fromarray(annotated_image)
        draw = ImageDraw.Draw(pil_image)
        font = ImageFont.load_default()

        for nombre, landmark_enum in partes.items():
            landmark = results.pose_landmarks.landmark[landmark_enum]
            x = int(landmark.x * image.shape[1])
            y = int(landmark.y * image.shape[0])
            
            # Dibujar caja negra con texto amarillo
            text_size = draw.textsize(nombre, font=font)
            box = (x, y, x + text_size[0] + 10, y + text_size[1] + 10)
            draw.rectangle(box, fill="black")
            draw.text((x + 5, y + 5), nombre, fill="yellow", font=font)

        st.image(pil_image, caption="Partes del cuerpo detectadas", use_column_width=True)
    else:
        st.warning("No se detectaron puntos de referencia en la imagen. Asegúrate de que sea una imagen clara de una persona de cuerpo entero.")
