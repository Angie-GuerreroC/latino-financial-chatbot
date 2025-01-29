import openai
import streamlit as st

# OpenAI API Key from Streamlit Secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Function to get financial advice using the cheapest GPT-4o-mini model
def get_financial_advice(user_input, language_code):
    """
    Calls OpenAI API using the cheapest model (gpt-4o-mini) for cost efficiency.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",  # Cheapest model
            messages=[
                {"role": "system", "content": f"Eres un chatbot financiero que ayuda a latinos en EE.UU. Usa un tono amigable y referencias culturales. Responde en {language_code}."},
                {"role": "user", "content": user_input},
            ],
            temperature=0.7  # Adjust for response variability
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error: {str(e)}"
