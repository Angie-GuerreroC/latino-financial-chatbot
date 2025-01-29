import openai
from src.settings import OPENAI_API_KEY

# Set OpenAI API Key
openai.api_key = OPENAI_API_KEY

def get_financial_advice(user_input, language_code):
    """
    Calls OpenAI API to generate financial advice based on user input.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Using cost-effective model
            messages=[
                {"role": "system", "content": f"Eres un chatbot financiero que ayuda a latinos en EE.UU. Usa un tono amigable y referencias culturales. Responde en {language_code}."},
                {"role": "user", "content": user_input},
            ],
            temperature=0.7  # Adjust for response variability
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error: {str(e)}"
