import os
import requests
import streamlit as st
from styles import apply_base_style


# URL til FastAPI-backend.
# Frontend bruger denne adresse til at sende og hente data.
API_URL = os.getenv("API_URL", "http://127.0.0.1:8000")


# Konfigurerer Streamlit-siden.
# centered-layout gør formularen mere fokuseret og læsbar.
st.set_page_config(
    page_title="Registrering",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Indlæser fælles CSS-styling.
# Styling ligger i styles.py for at undgå gentaget CSS-kode.
st.markdown(
    apply_base_style(),
    unsafe_allow_html=True,
)



# Titel på registreringssiden.
st.title("Registrering")


# Opretter formular til dagens morgenrutine.
# Formularen samler alle inputfelter før data sendes samlet.
with st.form("routine_form"):

    # Dato-container.
    with st.container(border=True):
        st.subheader("Dato")

        date = st.date_input("Dato")


    # Container til dagens vigtigste opgaver.
    with st.container(border=True):
        st.subheader("Dagens tre vigtigste opgaver")

        task_1 = st.text_input("Opgave 1")
        task_2 = st.text_input("Opgave 2")
        task_3 = st.text_input("Opgave 3")


    # Søvn-container.
    with st.container(border=True):
        st.subheader("Søvn")

        # Tidspunkt brugeren stod op.
        wake_up_time = st.text_input(
            "Hvornår stod du op?",
            "05:30",
        )

        # Antal timers søvn.
        sleep_hours = st.number_input(
            "Timer sovet",
            0.0,
            24.0,
            7.5,
            0.5,
        )


    # Trænings-container.
    with st.container(border=True):
        st.subheader("Træning")

        # Radio-knapper returnerer tekst,
        # derfor omdannes svaret til True eller False.
        training = st.radio(
            "Har du trænet?",
            ["Ja", "Nej"],
            horizontal=True,
        ) == "Ja"


    # Bad-container.
    with st.container(border=True):
        st.subheader("Bad")

        # Brugeren vælger type af bad.
        shower_type = st.selectbox(
            "Bad-type",
            [
                "normalt bad",
                "koldt bad",
                "intet bad",
            ],
        )


    # Morgenmads-container.
    with st.container(border=True):
        st.subheader("Morgenmad")

        breakfast = st.radio(
            "Har du spist morgenmad?",
            ["Ja", "Nej"],
            horizontal=True,
        ) == "Ja"


    # Vand-container.
    with st.container(border=True):
        st.subheader("Vand")

        # Registrerer antal glas vand.
        water_glasses = st.number_input(
            "Antal glas vand",
            0,
            30,
            3,
        )


    # Humør-container.
    with st.container(border=True):
        st.subheader("Humør")

        # Humør registreres på en skala fra 1 til 10.
        mood = st.slider(
            "Humør",
            1,
            10,
            8,
        )

        # Brugeren kan skrive tanker og refleksioner.
        thoughts = st.text_area(
            "Hvilke tanker fylder i dag?",
            height=120,
        )


    # Formularens submit-knap.
    submitted = st.form_submit_button("Gem morgenrutine")


# Kører kun når brugeren trykker på submit-knappen.
if submitted:

    # Samler alle inputdata i dictionary-format.
    # Data sendes som JSON til FastAPI-backend.
    data = {
        "date": str(date),
        "wake_up_time": wake_up_time,
        "sleep_hours": sleep_hours,
        "training": training,
        "shower_type": shower_type,
        "breakfast": breakfast,
        "water_glasses": water_glasses,
        "task_1": task_1,
        "task_2": task_2,
        "task_3": task_3,
        "mood": mood,
        "thoughts": thoughts,
    }

    try:
        # Sender registreringen til backend via HTTP POST-request.
        response = requests.post(
            f"{API_URL}/routines",
            json=data,
        )

        # Hvis registreringen lykkes vises succesbesked.
        if response.status_code == 200:
            st.success("Morgenrutine gemt")

        # Hvis backend returnerer fejl vises fejlbesked.
        else:
            st.error("Noget gik galt")

    # Hvis backend-serveren ikke kører.
    except requests.exceptions.ConnectionError:
        st.error("Backend kører ikke")