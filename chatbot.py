import openai
from settings.py import OPENAI_API_KEY

# Set OpenAI API Key
openai.api_key = OPENAI_API_KEY

def get_financial_advice(user_input, language_code):
    """
    Calls OpenAI API to generate personalized financial advice.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": f"Eres un chatbot financiero que ayuda a padres latinos, parejas latinas y latinos en EE.UU. Usa un tono amigable, referencias culturales, y ajusta tu respuesta según el contexto. Responde en {language_code}."},
                {"role": "user", "content": user_input},
            ],
            temperature=0.8
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error: {str(e)}"
