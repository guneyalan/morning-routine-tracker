import requests
import streamlit as st


API_URL = "http://127.0.0.1:8000"


st.set_page_config(
    page_title="AI-feedback",
    layout="wide",
    initial_sidebar_state="expanded",
)


st.markdown(
    """
    <style>
    #MainMenu, footer {visibility: hidden;}
    .stApp {background: #f5f5f3; color: #222;}
    .block-container {max-width: 900px; padding-top: 3rem;}

    div.stButton > button {
        width: 100%;
        height: 70px;
        border-radius: 14px;
        border: none;
        background: #222;
        color: white;
        font-size: 20px;
        font-weight: 600;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


st.title("AI-feedback")

st.write(
    """
    Generér AI-feedback baseret på dine morgenrutiner,
    søvn, træning, meditation og humør.
    """
)


if st.button("Generér AI-feedback"):

    try:
        response = requests.get(f"{API_URL}/ai-feedback")

        if response.status_code == 200:

            feedback = response.json()["feedback"]

            st.success(feedback)

        else:
            st.error("Kunne ikke hente AI-feedback.")

    except requests.exceptions.ConnectionError:
        st.error("Backend kører ikke.")