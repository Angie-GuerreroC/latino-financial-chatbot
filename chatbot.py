import openai
from settings import OPENAI_API_KEY 

# Set OpenAI API Key
openai.api_key = OPENAI_API_KEY

def get_financial_advice(user_input, language_code):
    """
    Calls OpenAI API using GPT-4o Mini for cost efficiency.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": f"Eres un chatbot financiero que ayuda a latinos en EE.UU. Usa un tono amigable y referencias culturales. Responde en {language_code}."},
                {"role": "user", "content": user_input},
            ],
            temperature=0.7
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error: {str(e)}"
