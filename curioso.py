import streamlit as st

st.set_page_config(page_title="Aprende Python - Bucles y Condicionales", layout="centered")

st.title("🐍 Aprende Python: `while`, `for` e `if`")
st.markdown("""
Bienvenido a esta mini lección interactiva. A continuación se explica el uso de los principales constructores de control en Python:
""")

with st.expander("🔄 Bucle `while`"):
    st.code("""
i = 0
while i < 5:
    print(i)
    i += 1
""", language='python')
    st.markdown("El bucle `while` repite un bloque mientras una condición sea verdadera.")

with st.expander("🔁 Bucle `for`"):
    st.code("""
for i in range(5):
    print(i)
""", language='python')
    st.markdown("El bucle `for` itera sobre una secuencia como `range`, listas, etc.")

with st.expander("✅ Condicional `if`"):
    st.code("""
x = 10
if x > 5:
    print("Mayor que 5")
elif x == 5:
    print("Es igual a 5")
else:
    print("Menor que 5")
""", language='python')
    st.markdown("`if`, `elif` y `else` permiten tomar decisiones basadas en condiciones.")

---

### 📝 Quiz Interactivo

st.header("🧠 Quiz: ¿Cuánto sabes de Python?")
st.markdown("Selecciona la respuesta correcta en cada pregunta:")

# Preguntas y respuestas
questions = [
    {
        "question": "¿Cuál es la salida de: `i=0; while i<3: print(i); i+=1`?",
        "options": ["0 1 2", "1 2 3", "0 1 2 3"],
        "answer": "0 1 2"
    },
    {
        "question": "¿Qué función se usa comúnmente con `for` para iterar un número fijo de veces?",
        "options": ["range()", "enumerate()", "repeat()"],
        "answer": "range()"
    },
    {
        "question": "¿Cuál es la sintaxis correcta de un `if`?",
        "options": ["if x > 5 then:", "if (x > 5):", "if x > 5:"],
        "answer": "if x > 5:"
    },
    {
        "question": "¿Qué imprime: `for i in range(2): print(i)`?",
        "options": ["0 1", "1 2", "0 1 2"],
        "answer": "0 1"
    },
    {
        "question": "¿Qué operador se usa para 'igual a' en condiciones?",
        "options": ["=", "==", "==="],
        "answer": "=="
    },
    {
        "question": "¿Qué hace `i += 1`?",
        "options": ["Incrementa i en 1", "Asigna 1 a i", "Decrementa i en 1"],
        "answer": "Incrementa i en 1"
    },
    {
        "question": "¿Cuándo se usa `else`?",
        "options": ["Cuando la condición es falsa", "Cuando es verdadera", "Cuando empieza un bucle"],
        "answer": "Cuando la condición es falsa"
    },
    {
        "question": "¿Qué palabra se usa para romper un bucle antes de que termine?",
        "options": ["exit", "stop", "break"],
        "answer": "break"
    },
    {
        "question": "¿Cuál de estos es un bucle infinito?",
        "options": ["while True:", "for i in range(10):", "if True:"],
        "answer": "while True:"
    },
    {
        "question": "¿Cuál es la salida de `if 3 > 2: print('Sí')`?",
        "options": ["Sí", "No", "Error"],
        "answer": "Sí"
    }
]

# Estado de respuestas
user_answers = []
score = 0

for i, q in enumerate(questions):
    st.subheader(f"Pregunta {i + 1}")
    user_answer = st.radio(q["question"], q["options"], key=f"q{i}")
    user_answers.append(user_answer)

# Verificación de puntaje
if st.button("✅ Verificar puntaje"):
    score = sum(user_answers[i] == questions[i]["answer"] for i in range(len(questions)))
    st.success(f"Puntaje: {score} / {len(questions)}")

    if score == len(questions):
        st.balloons()
        st.markdown("🎉 ¡Excelente! Has respondido todo correctamente.")
    elif score >= 7:
        st.markdown("👍 ¡Muy bien! Aún puedes mejorar un poco.")
    else:
        st.markdown("📘 Sigue practicando para mejorar tu comprensión.")
