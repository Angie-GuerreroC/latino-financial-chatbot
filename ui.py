import streamlit as st
from chatbot import get_financial_advice

# Chatbot title
st.title("💸 Chatbot Financiero para Latinos en EE.UU.")
st.write("¡Hola! Soy tu compa financiero. Estoy aquí para ayudarte a manejar tus finanzas con consejos prácticos y referencias culturales que entenderás. 💪")

# Step 1: Language Preference
language = st.radio("¿Prefieres platicar en español o inglés?", ("Español", "Inglés"))
language_code = "es" if language == "Español" else "en"

# Step 2: Collect Demographic Data
st.header("Cuéntame un poquito de ti (sin pena).")
age = st.number_input("¿Cuántos años tienes?", min_value=18, max_value=100, step=1)
income = st.number_input("¿Cuánto ganas al mes antes de impuestos? (en USD)", min_value=0, step=100)
sex = st.selectbox("¿Eres mamá, papá, o algo más?", ["Mamá", "Papá", "Otro"])
dependents = st.number_input("¿Cuántos dependientes tienes (hijos u otros familiares)?", min_value=0, max_value=20, step=1)
marital_status = st.selectbox("¿Cuál es tu estado civil?", ["Soltero/a", "Casado/a o en pareja", "Divorciado/a", "Viudo/a"])

# Step 3: Ask about Latino Ethnic Background
ethnic_background = st.selectbox(
    "¿De dónde eres o de dónde es tu familia?",
    ["México", "Puerto Rico", "Cuba", "Colombia", "Venezuela", "El Salvador", "Guatemala", "Otro"]
)

# Adjust examples based on background
background_references = {
    "México": "como cuando ahorrabas para las piñatas de los cumpleaños",
    "Puerto Rico": "como un buen arroz con habichuelas, necesitas planear bien",
    "Cuba": "como cuando juntas para una fiesta en el malecón",
    "Colombia": "como un buen café, lleva tiempo pero vale la pena",
    "Venezuela": "como ahorrar para las hallacas de diciembre",
    "El Salvador": "como cuando juntas para las pupusas del domingo",
    "Guatemala": "como cuando ahorras para las ferias patronales",
    "Otro": "como cuando ahorras para las tradiciones de tu país"
}

cultural_reference = background_references.get(ethnic_background, "como cuando ahorras para algo importante")

# Step 4: Financial Goals
st.header("¿En qué te puedo ayudar?")
goal = st.selectbox(
    "¿Qué quieres lograr?",
    ["Ahorrar para la familia", "Comprar una casa", "Saber cuánto carro puedo pagar", "Invertir para el futuro", "Otro"]
)

# Step 5: Goal-Specific Tools
if goal == "Ahorrar para la familia":
    st.write(f"💡 Consejo: 'Ahorrar es {cultural_reference}. Empieza poquito a poquito.'")
elif goal == "Comprar una casa":
    st.write("🏡 Vamos a calcular cuánto puedes gastar en una casa.")
    house_budget = st.number_input("¿Cuánto tienes ahorrado para el enganche?", min
::contentReference[oaicite:0]{index=0}
