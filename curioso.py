import streamlit as st
import random

# Base de datos simplificada de partes y subpartes
anatomia = {
    "corazón": [
        "Aurícula derecha",
        "Aurícula izquierda",
        "Ventrículo derecho",
        "Ventrículo izquierdo",
        "Válvula tricúspide",
        "Válvula mitral",
        "Aorta",
        "Arteria pulmonar"
    ],
    "cerebro": [
        "Lóbulo frontal",
        "Lóbulo parietal",
        "Lóbulo temporal",
        "Lóbulo occipital",
        "Cerebelo",
        "Tronco encefálico",
        "Hipotálamo"
    ],
    "ojo": [
        "Córnea",
        "Cristalino",
        "Iris",
        "Pupila",
        "Retina",
        "Nervio óptico",
        "Esclerótica"
    ]
}

# Función para generar acrónimo mnemotécnico
def generar_acronimo(subpartes):
    letras_iniciales = [parte[0].upper() for parte in subpartes]
    acronimo = "".join(letras_iniciales)
    return acronimo

def generar_frase_mnemonica(subpartes):
    letras = [parte[0].upper() for parte in subpartes]
    palabras_ejemplo = {
        "A": "Amigos", "B": "Bailan", "C": "Con", "D": "Diversión", "E": "En",
        "F": "Fiestas", "G": "Grandes", "H": "Hoy", "I": "Intensamente",
        "J": "Juegan", "K": "Koalas", "L": "Locamente", "M": "Mientras",
        "N": "Nadan", "O": "Observan", "P": "Peces", "Q": "Quemando",
        "R": "Ríos", "S": "Soleados", "T": "Trepan", "U": "Unas",
        "V": "Velas", "W": "Wafles", "X": "Xilófonos", "Y": "Yogures", "Z": "Zambullen"
    }
    frase = " ".join([palabras_ejemplo.get(letra, letra) for letra in letras])
    return frase

# Interfaz Streamlit
st.set_page_config(page_title="Anatomía + Memotecnia", layout="centered")
st.title("🧠 Aplicativo de Anatomía con Técnicas Mnemotécnicas")

parte = st.text_input("Ingresa una parte del cuerpo humano (ej. corazón, cerebro, ojo):").strip().lower()

if parte:
    if parte in anatomia:
        subpartes = anatomia[parte]
        st.subheader(f"🫀 Subpartes de {parte.capitalize()}:")
        for i, sub in enumerate(subpartes, 1):
            st.write(f"{i}. {sub}")

        st.subheader("🧩 Acrónimo mnemotécnico:")
        acronimo = generar_acronimo(subpartes)
        st.code(acronimo)

        st.subheader("💡 Frase mnemotécnica sugerida:")
        frase = generar_frase_mnemonica(subpartes)
        st.success(frase)
    else:
        st.warning("Esa parte del cuerpo no está en la base de datos. Prueba con: corazón, cerebro u ojo.")
