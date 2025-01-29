import streamlit as st

def apply_custom_styles():
    """
    Injects custom styles for the chatbot UI.
    """
    st.markdown(
        """
        <style>
            .big-font { 
                font-size: 28px !important; 
                font-weight: bold; 
                text-align: center; 
                color: white; 
                background-color: #8FBC8F;  /* Neutral Green */
                padding: 10px; 
                border-radius: 10px;
            }
            
            /* Chat Bubble Styles */
            .chat-bubble {
                background-color: #f9f9f9;
                color: #333333;
                padding: 15px;
                border-radius: 12px;
                margin-bottom: 10px;
                display: inline-block;
                width: auto;
                max-width: 80%;
                box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.1);
            }

            /* User Chat Bubble */
            .user-bubble {
                background-color: #D1ECF1;
                color: #004085;
                padding: 15px;
                border-radius: 12px;
                margin-bottom: 10px;
                display: inline-block;
                width: auto;
                max-width: 80%;
                box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.1);
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

def chatbot_title(language_code):
    """
    Displays chatbot title.
    """
    translations = {
        "en": "💸 Latino Financial Chatbot!",
        "es": "💸 Chatbot Financiero para Latinos!"
    }
    st.markdown(f'<p class="big-font">{translations[language_code]}</p>', unsafe_allow_html=True)
