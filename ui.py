import streamlit as st
from src.chatbot import get_financial_advice

# Step 1: Language Preference
language = st.radio("Choose your preferred language / Elige tu idioma", ("English", "Español"))
language_code = "en" if language == "English" else "es"

# Define Translations
translations = {
    "title": {
        "en": "💸 Latino Financial Chatbot!",
        "es": "💸 Chatbot Financiero para Latinos!"
    },
    "intro": {
        "en": "Hello! I'm your financial buddy. I'm here to help you manage your finances with practical advice and cultural references you’ll understand. 💪",
        "es": "¡Hola! Soy tu compa financiero. Estoy aquí para ayudarte a manejar tus finanzas con consejos prácticos y referencias culturales que entenderás. 💪"
    },
    "age": {"en": "How old are you?", "es": "¿Cuántos años tienes?"},
    "income": {"en": "What is your monthly income before taxes (USD)?", "es": "¿Cuánto ganas al mes antes de impuestos? (en USD)"},
    "sex": {"en": "Are you a mom, dad, or something else?", "es": "¿Eres mamá, papá, o algo más?"},
    "dependents": {"en": "How many dependents do you have?", "es": "¿Cuántos dependientes tienes?"},
    "marital_status": {"en": "What is your marital status?", "es": "¿Cuál es tu estado civil?"},
    "ethnic_background": {"en": "Where are you or your family from?", "es": "¿De dónde eres o de dónde es tu familia?"},
    "goal": {"en": "What is your financial goal?", "es": "¿Qué quieres lograr?"},
    "chatbox": {"en": "Ask me anything about finance!", "es": "¡Pregúntame cualquier cosa sobre finanzas!"},
}

# Display Chatbot Title
st.title(translations["title"][language_code])
st.write(translations["intro"][language_code])

# Step 2: Collect Demographic Data
st.header(translations["goal"][language_code])
age = st.number_input(translations["age"][language_code], min_value=18, max_value=100, step=1)
income = st.number_input(translations["income"][language_code], min_value=0, step=100)
sex = st.selectbox(translations["sex"][language_code], ["Mom", "Dad", "Other"] if language == "English" else ["Mamá", "Papá", "Otro"])
dependents = st.number_input(translations["dependents"][language_code], min_value=0, max_value=20, step=1)
marital_status = st.selectbox(translations["marital_status"][language_code], ["Single", "Married", "Divorced", "Widowed"] if language == "English" else ["Soltero/a", "Casado/a o en pareja", "Divorciado/a", "Viudo/a"])

# Step 3: Ask about Latino Ethnic Background
ethnic_background = st.selectbox(
    translations["ethnic_background"][language_code],
    ["Mexico", "Puerto Rico", "Cuba", "Colombia", "Venezuela", "El Salvador", "Guatemala", "Other"] if language == "English"
    else ["México", "Puerto Rico", "Cuba", "Colombia", "Venezuela", "El Salvador", "Guatemala", "Otro"]
)

# Adjust examples based on background
background_references = {
    "Mexico": "like when you saved for birthday piñatas",
    "Puerto Rico": "like planning for a good arroz con habichuelas",
    "Cuba": "like saving up for a party on the Malecón",
    "Colombia": "like brewing a good coffee, it takes time but is worth it",
    "Venezuela": "like saving for hallacas in December",
    "El Salvador": "like setting money aside for Sunday pupusas",
    "Guatemala": "like when you save for local fairs",
    "Other": "like saving for your country’s traditions"
}

cultural_reference = background_references.get(ethnic_background, background_references["Other"])

# Step 4: Financial Goals
st.header(translations["goal"][language_code])
goal = st.selectbox(
    "",
    ["Save for my family", "Buy a house", "Determine how much car I can afford", "Invest for the future", "Other"] if language == "English"
    else ["Ahorrar para la familia", "Comprar una casa", "Saber cuánto carro puedo pagar", "Invertir para el futuro", "Otro"]
)

# Step 5: Goal-Specific Tools & Adjusted Chat
if goal == "Save for my family" or goal == "Ahorrar para la familia":
    st.write(f"💡 {'Saving is ' if language == 'English' else 'Ahorrar es '}{cultural_reference}. {'Start little by little!' if language == 'English' else 'Empieza poquito a poquito.'}")
elif goal == "Buy a house" or goal == "Comprar una casa":
    st.write("🏡 Let's calculate how much house you can afford!" if language == "English" else "🏡 Vamos a calcular cuánto puedes gastar en una casa.")
    
    house_budget = st.number_input("How much have you saved for a down payment?" if language == "English" else "¿Cuánto tienes ahorrado para el enganche?", min_value=0, step=100)
    monthly_payment = st.number_input("How much can you afford for your monthly mortgage?" if language == "English" else "¿Cuánto puedes pagar al mes en tu hipoteca?", min_value=0, step=100)
    interest_rate = st.slider("What is the average interest rate (%)?" if language == "English" else "¿Cuál es la tasa de interés promedio (%)?", 2.0, 8.0, 4.5)
    loan_term = st.slider("How many years will your mortgage be?" if language == "English" else "¿Cuántos años será tu hipoteca?", 10, 30, 30)

    home_price = house_budget + (monthly_payment * (12 * loan_term) * (1 - interest_rate / 100))
    st.write(f"🏠 {'Based on these numbers, you could afford a house up to ' if language == 'English' else 'Basado en estos números, podrías comprar una casa de hasta '}${home_price:,.2f}.")

# Step 6: Open Chatbox for More Questions
st.header(translations["chatbox"][language_code])
user_query = st.text_input("Ask a question here..." if language == "English" else "Escribe tu pregunta aquí...")

if st.button("Send" if language == "English" else "Enviar"):
    if user_query.strip():
        response = get_financial_advice(user_query, language_code)
        st.write(f"🤖 {response}")
    else:
        st.warning("Please enter a question!" if language == "English" else "¡Por favor ingresa una pregunta!")
