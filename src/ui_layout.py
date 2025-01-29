import streamlit as st

def apply_custom_styles():
    """
    Injects custom styles for the chatbot UI.
    """
    st.markdown(
        """
        <style>
            /* Green Title Styling */
            .big-font { 
                font-size: 28px !important; 
                font-weight: bold; 
                text-align: center; 
                color: white; 
                background-color: #4CAF50;  /* Green */
                padding: 15px; 
                border-radius: 10px;
            }

            /* Chat Bubble Styles */
            .chat-bubble {
                background-color: #333333; /* Dark Gray */
                color: #f9f9f9;
                padding: 15px;
                border-radius: 12px;
                margin-bottom: 10px;
                display: inline-block;
                width: auto;
                max-width: 80%;
                box-shadow: 2px 2px 8px rgba(255, 255, 255, 0.1);
            }

            /* User Chat Bubble */
            .user-bubble {
                background-color: #4CAF50; /* Green for user messages */
                color: white;
                padding: 15px;
                border-radius: 12px;
                margin-bottom: 10px;
                display: inline-block;
                width: auto;
                max-width: 80%;
                box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.1);
            }

            /* Dark Mode Input Box */
            .stTextInput > div > div {
                background-color: #222222 !important;
                color: white !important;
                border-radius: 10px;
                border: 1px solid #4CAF50;
            }

            /* Dark Mode Dropdown */
            .stSelectbox > div > div {
                background-color: #222222 !important;
                color: white !important;
                border-radius: 10px;
                border: 1px solid #4CAF50;
            }

            /* Button Styling */
            .stButton>button {
                background-color: #4CAF50;
                color: white;
                border-radius: 10px;
                font-weight: bold;
                width: 100%;
                padding: 10px;
                border: none;
            }
            
            .stButton>button:hover {
                background-color: #45a049;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

def chatbot_title(language_code):
    """
    Displays chatbot title with a green background and white text.
    """
    translations = {
        "en": "💸 Latino Financial Chatbot!",
        "es": "💸 Chatbot Financiero para Latinos!"
    }
    st.markdown(f'<p class="big-font">{translations[language_code]}</p>', unsafe_allow_html=True)
