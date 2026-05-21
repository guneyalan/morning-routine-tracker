import os   
import requests
import streamlit as st


# URL til FastAPI-backend.
# AI-siden bruger dette endpoint til at hente feedback.
API_URL = os.getenv("API_URL", "http://127.0.0.1:8000")


# Konfigurerer Streamlit-siden.
# Sidebar holdes åben, så navigationen er nem under demo.
st.set_page_config(
    page_title="AI-feedback",
    layout="wide",
    initial_sidebar_state="expanded",
)


# Custom CSS styling.
# Holder siden i samme simple og minimalistiske stil som resten af appen.
st.markdown(
    """
    <style>

    /* Skjuler Streamlits standardmenu og footer */
    #MainMenu, footer {
        visibility: hidden;
    }

    /* Appens baggrund og grundfarve */
    .stApp {
        background: #f5f5f3;
        color: #222;
    }

    /* Gør indholdet smallere og mere læsbart */
    .block-container {
        max-width: 900px;
        padding-top: 3rem;
    }

    /* Styling af AI-knappen */
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


# Titel på AI-siden.
st.title("AI-feedback")


# Kort forklaring af hvad brugeren kan gøre på siden.
st.write(
    """
    Generér AI-feedback baseret på dine morgenrutiner,
    søvn, træning, opgaver, tanker og humør.
    """
)


# Når brugeren trykker på knappen, kaldes backendens AI-endpoint.
if st.button("Generér AI-feedback"):

    try:
        # Sender GET-request til backend.
        # Backend håndterer både Mistral API og lokal fallback.
        response = requests.get(f"{API_URL}/ai-feedback")

        # Hvis backend svarer korrekt, vises feedbacken.
        if response.status_code == 200:

            feedback = response.json()["feedback"]

            st.success(feedback)

        # Hvis backend svarer med fejlstatus.
        else:
            st.error("Kunne ikke hente AI-feedback.")

    # Hvis FastAPI-backend ikke kører.
    except requests.exceptions.ConnectionError:
        st.error("Backend kører ikke.")