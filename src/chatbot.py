import openai
import streamlit as st

# OpenAI API Key from Streamlit Secrets
API_KEY = st.secrets["OPENAI_API_KEY"]

# Initialize OpenAI Client
client = openai.OpenAI(api_key=API_KEY)

def get_financial_advice(user_input, language_code):
    """
    Calls OpenAI API using gpt-3.5-turbo to provide financial advice.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"Eres un chatbot financiero que ayuda a latinos en EE.UU. Usa un tono amigable y referencias culturales. Responde en {language_code}."},
                {"role": "user", "content": user_input},
            ],
            temperature=0.7
        )
        return response.choices[0].message.content if response.choices else "Lo siento, no tengo una respuesta en este momento. 😕"
    
    except openai.OpenAIError as e:
        return f"❌ OpenAI API Error: {str(e)}"
    except Exception as e:
        return f"⚠️ Error inesperado: {str(e)}"

def get_cultural_reference(country, goal, language_code):
    """
    Uses OpenAI to generate a culturally relevant financial reference
    based on the user's country and financial goal.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"Eres un experto en finanzas culturales. Crea una analogía relevante para un latino basado en su país y objetivo financiero. Responde en {language_code}."},
                {"role": "user", "content": f"Genera una analogía financiera culturalmente relevante para alguien de {country} que quiere {goal}."}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content if response.choices else "No se encontró una referencia cultural. 🤔"

    except openai.OpenAIError as e:
        return f"❌ OpenAI API Error: {str(e)}"
    except Exception as e:
        return f"⚠️ Error inesperado: {str(e)}"
