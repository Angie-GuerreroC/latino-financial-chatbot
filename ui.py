import streamlit as st
from src.chatbot import get_financial_advice

# Step 1: Language Preference
language = st.radio("Choose your preferred language / Elige tu idioma", ("English", "Español"))
language_code = "en" if language == "English" else "es"

# Define Translations
translations = {
    "title": {
        "en": "💸 Latino Financial Chatbot for the U.S.",
        "es": "💸 Chatbot Financiero para Latinos en EE.UU."
    },
    "intro": {
        "en": "Hello! I'm your financial buddy. I'm here to help you manage your finances with practical advice and cultural references you’ll understand. 💪",
        "es": "¡Hola! Soy tu compa financiero. Estoy aquí para ayudarte a manejar tus finanzas con consejos prácticos y referencias culturales que entenderás. 💪"
    },
    "goal_acknowledgment": {
        "en": "Cool! You want to talk about {goal}. What questions do you have?",
        "es": "¡Genial! Quieres hablar sobre {goal}. ¿Qué preguntas tienes?"
    },
    "chatbox": {
        "en": "Ask me anything about finance!",
        "es": "¡Pregúntame cualquier cosa sobre finanzas!"
    },
}

# Display Chatbot Title
st.title(translations["title"][language_code])
st.write(translations["intro"][language_code])

# Step 2: Financial Goals
goal = st.selectbox(
    "What is your financial goal?" if language == "English" else "¿Qué quieres lograr?",
    ["Save for my family", "Buy a house", "Determine how much car I can afford", "Invest for the future", "Other"] if language == "English"
    else ["Ahorrar para la familia", "Comprar una casa", "Saber cuánto carro puedo pagar", "Invertir para el futuro", "Otro"]
)

# **Dynamic Goal Acknowledgment**
st.write(translations["goal_acknowledgment"][language_code].format(goal=goal))

# Step 3: Open Chatbox for More Questions
st.header(translations["chatbox"][language_code])
user_query = st.text_input("Ask a question here..." if language == "English" else "Escribe tu pregunta aquí...")

if st.button("Send" if language == "English" else "Enviar"):
    if user_query.strip():
        response = get_financial_advice(user_query, language_code)
        st.write(f"🤖 {response}")
    else:
        st.warning("Please enter a question!" if language == "English" else "¡Por favor ingresa una pregunta!")
