import openai
import streamlit as st

# OpenAI API Key from Streamlit Secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

def get_financial_advice(user_input, language_code):
    """
    Calls OpenAI API using gpt-3.5-turbo with the new syntax (v1.0.0+).
    """
    try:
        client = openai.OpenAI(api_key=openai.api_key)  # ✅ New way to initialize API call
        response = client.chat.completions.create(  # ✅ Updated API call for OpenAI v1.0+
            model="gpt-3.5-turbo",  # ✅ Using cost-efficient model
            messages=[
                {"role": "system", "content": f"Eres un chatbot financiero que ayuda a latinos en EE.UU. Usa un tono amigable y referencias culturales. Responde en {language_code}."},
                {"role": "user", "content": user_input},
            ],
            temperature=0.7
        )
        return response.choices[0].message.content  # ✅ Updated response format
    except Exception as e:
        return f"Error: {str(e)}"
