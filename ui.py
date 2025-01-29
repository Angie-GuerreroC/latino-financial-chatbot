import streamlit as st
from src.chatbot import get_financial_advice, get_cultural_reference
from src.ui_layout import apply_custom_styles, chatbot_title, start_chat_container, end_chat_container

# Apply UI Styles
apply_custom_styles()

# Step 1: Language Preference
language = st.radio("🌎 Choose your preferred language / Elige tu idioma", ("English", "Español"))
language_code = "en" if language == "English" else "es"

# Display Chatbot Title
chatbot_title(language_code)

# **Start Chatbox UI Container**
start_chat_container()

# Define Translations
translations = {
    "intro": {
        "en": "👋 **Welcome!** Let's talk about money, goals, and dreams. Whether you're saving up for a house or just want to manage your finances better, I'm here to help!",
        "es": "👋 **¡Bienvenido!** Hablemos de dinero, metas y sueños. Ya sea que estés ahorrando para una casa o solo quieras manejar mejor tus finanzas, ¡aquí estoy para ayudarte!"
    },
    "goal_acknowledgment": {
        "en": "✨ Cool! You want to talk about **{goal}**. What questions do you have?",
        "es": "✨ ¡Genial! Quieres hablar sobre **{goal}**. ¿Qué preguntas tienes?"
    },
    "chatbox": {
        "en": "💬 Ask me anything about finance!",
        "es": "💬 ¡Pregúntame cualquier cosa sobre finanzas!"
    },
}

st.write(translations["intro"][language_code])

# Step 2: Ask User for Country of Origin
country_of_origin = st.text_input(
    "🌍 Where are you or your family from?" if language == "English" else "🌍 ¿De qué país eres o es tu familia?"
)

# Step 3: Financial Goals
goal = st.selectbox(
    "🎯 What is your financial goal?" if language == "English" else "🎯 ¿Qué quieres lograr?",
    ["Save for my family", "Buy a house", "Determine how much car I can afford", "Invest for the future", "Other topic"] if language == "English"
    else ["Ahorrar para la familia", "Comprar una casa", "Saber cuánto carro puedo pagar", "Invertir para el futuro", "Otro tema"]
)

# Fetch a dynamic cultural reference if country and goal are provided
cultural_reference = None
if country_of_origin.strip():
    with st.spinner("🔍 Finding a culturally relevant analogy..."):
        cultural_reference = get_cultural_reference(country_of_origin, goal, language_code)

# **Dynamic Goal Acknowledgment**
st.markdown(
    f'<div class="chat-bubble">{translations["goal_acknowledgment"][language_code].format(goal=goal)}</div>',
    unsafe_allow_html=True,
)

# Add cultural savings analogy for better engagement
if cultural_reference and goal in ["Save for my family", "Ahorrar para la familia"]:
    st.markdown(
        f'<div class="chat-bubble">💡 {"Saving is" if language == "English" else "Ahorrar es"} {cultural_reference}. '
        f'{"Start little by little!" if language == "English" else "Empieza poquito a poquito."}</div>',
        unsafe_allow_html=True,
    )

# Step 4: Open Chatbox for More Questions
st.header(translations["chatbox"][language_code])
user_query = st.text_input("💭 Ask a question here..." if language == "English" else "💭 Escribe tu pregunta aquí...")

if st.button("🚀 Send" if language == "English" else "🚀 Enviar"):
    if user_query.strip():
        response = get_financial_advice(user_query, language_code)
        st.markdown(f'<div class="user-bubble">🧑‍💻 {user_query}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="chat-bubble">🤖 {response}</div>', unsafe_allow_html=True)
    else:
        st.warning("⚠️ Please enter a question!" if language == "English" else "⚠️ ¡Por favor ingresa una pregunta!")

# **End Chatbox UI Container**
end_chat_container()
