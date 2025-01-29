import streamlit as st

# OpenAI API Key (Stored in Streamlit Secrets)
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]

# Cultural references based on ethnicity
CULTURAL_REFERENCES = {
    "México": "como cuando ahorrabas para las piñatas de los cumpleaños",
    "Puerto Rico": "como un buen arroz con habichuelas, necesitas planear bien",
    "Cuba": "como cuando juntas para una fiesta en el malecón",
    "Colombia": "como un buen café, lleva tiempo pero vale la pena",
    "Venezuela": "como ahorrar para las hallacas de diciembre",
    "El Salvador": "como cuando juntas para las pupusas del domingo",
    "Guatemala": "como cuando ahorras para las ferias patronales",
    "Otro": "como cuando ahorras para las tradiciones de tu país"
}
