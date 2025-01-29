import streamlit as st
from chatbot import get_financial_advice
from utils import (
    calculate_home_affordability,
    calculate_car_affordability,
    calculate_investment_growth
)
from src.settings import CULTURAL_REFERENCES

# Chatbot title
st.title("💸 Chatbot Financiero para Latinos en EE.UU.")
st.write("¡Hola! Soy tu compa financiero. Estoy aquí para ayudarte con consejos prácticos y referencias culturales. 💪")

# Step 1: Language Preference
language = st.radio("¿Prefieres platicar en español o inglés?", ("Español", "Inglés"))
language_code = "es" if language == "Español" else "en"

# Step 2: Collect User Data
st.header("Cuéntame un poquito de ti (sin pena).")
age = st.number_input("¿Cuántos años tienes?", min_value=18, max_value=100, step=1)
income = st.number_input("¿Cuánto ganas al mes antes de impuestos? (en USD)", min_value=0, step=100)
sex = st.selectbox("¿Eres mamá, papá, o algo más?", ["Mamá", "Papá", "Otro"])
dependents = st.number_input("¿Cuántos dependientes tienes?", min_value=0, max_value=20, step=1)
marital_status = st.selectbox("¿Cuál es tu estado civil?", ["Soltero/a", "Casado/a o en pareja", "Divorciado/a", "Viudo/a"])

# Ask about Latino Ethnic Background
ethnic_background = st.selectbox(
    "¿De dónde eres o de dónde es tu familia?",
    list(CULTURAL_REFERENCES.keys())
)

# Step 3: Financial Goals
st.header("¿En qué te puedo ayudar?")
goal = st.selectbox(
    "¿Qué quieres lograr?",
    ["Ahorrar para la familia", "Comprar una casa", "Saber cuánto carro puedo pagar", "Invertir para el futuro", "Otro"]
)

# Step 4: Goal-Specific Tools
if goal == "Ahorrar para la familia":
    st.write(f"💡 Consejo: 'Ahorrar es {CULTURAL_REFERENCES[ethnic_background]}. Empieza poquito a poquito.'")
elif goal == "Comprar una casa":
    st.write("🏡 Vamos a calcular cuánto puedes gastar en una casa.")
    house_budget = st.number_input("¿Cuánto tienes ahorrado para el enganche?", min_value=0, step=100)
    monthly_payment = st.number_input("¿Cuánto puedes pagar al mes en tu hipoteca?", min_value=0, step=100)
    interest_rate = st.slider("¿Cuál es la tasa de interés promedio (%)?", 2.0, 8.0, 4.5)
    loan_term = st.slider("¿Cuántos años será tu hipoteca?", 10, 30, 30)
    
    home_price = calculate_home_affordability(house_budget, monthly_payment, interest_rate, loan_term)
    st.write(f"🏠 Podrías comprar una casa de hasta ${home_price:,.2f}.")
elif goal == "Saber cuánto carro puedo pagar":
    st.write("🚗 Vamos a calcular cuánto puedes gastar en un carro.")
    car_budget = st.number_input("¿Cuánto tienes ahorrado para el enganche del carro?", min_value=0, step=100)
    monthly_payment = st.number_input("¿Cuánto puedes pagar al mes en el préstamo del carro?", min_value=0, step=100)
    loan_term = st.slider("¿Cuántos años será tu préstamo del carro?", 1, 7, 5)

    car_price = calculate_car_affordability(car_budget, monthly_payment, loan_term)
    st.write(f"🚘 Podrías comprar un carro de hasta ${car_price:,.2f}.")
elif goal == "Invertir para el futuro":
    st.write("📈 Vamos a calcular cómo crecerá tu dinero con el tiempo.")
    initial_investment = st.number_input("¿Cuánto quieres invertir inicialmente?", min_value=0, step=100)
    monthly_contribution = st.number_input("¿Cuánto puedes invertir cada mes?", min_value=0, step=100)
    interest_rate = st.slider("¿Cuál es la tasa de retorno anual esperada (%)?", 1.0, 15.0, 7.0)
    years = st.slider("¿Por cuántos años planeas invertir?", 1, 40, 20)

    future_value = calculate_investment_growth(initial_investment, monthly_contribution, interest_rate, years)
    st.write(f"📊 En {years} años, podrías tener ${future_value:,.2f}.")

# OpenAI chatbot for "Other" goal
elif goal == "Otro":
    user_goal = st.text_area("Describe tu meta financiera:")
    if st.button("Obtener consejo"):
        advice = get_financial_advice(user_goal, language_code)
        st.success(advice)
