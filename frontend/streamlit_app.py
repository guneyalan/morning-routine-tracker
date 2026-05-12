import requests
import streamlit as st


# Konfiguration af Streamlit-siden
st.set_page_config(
    page_title="Morning Routine Tracker",
    page_icon="🌅",
)


# Titel på siden
st.title("🌅 Morning Routine Tracker")

st.write(
    """
    Registrér din morgenrutine og gem data i backend-systemet.
    """
)


# Formular til brugerinput
with st.form("routine_form"):

    # Dato for registreringen
    date = st.text_input(
        "Dato",
        value="2026-05-12",
    )

    # Antal timers søvn
    sleep_hours = st.slider(
        "Søvn (timer)",
        min_value=0.0,
        max_value=12.0,
        value=7.5,
        step=0.5,
    )

    # Antal glas vand
    water_glasses = st.slider(
        "Antal glas vand",
        min_value=0,
        max_value=10,
        value=3,
    )

    # Om brugeren har trænet
    training = st.checkbox("Træning")

    # Om brugeren har mediteret
    meditation = st.checkbox("Meditation")

    # Humør-score
    mood = st.slider(
        "Humør",
        min_value=1,
        max_value=10,
        value=8,
    )

    # Valg af bad-type
    shower_type = st.selectbox(
        "Bad-type",
        [
            "normalt bad",
            "koldt bad",
            "intet bad",
        ],
    )

    # Knap til at gemme rutinen
    submitted = st.form_submit_button("Gem morgenrutine")


# Når brugeren trykker på knappen
if submitted:

    # Data som skal sendes til backend
    routine_data = {
        "date": date,
        "sleep_hours": sleep_hours,
        "water_glasses": water_glasses,
        "training": training,
        "meditation": meditation,
        "mood": mood,
        "shower_type": shower_type,
    }

    # Sender POST-request til FastAPI-backend
    response = requests.post(
        "http://127.0.0.1:8000/routines",
        json=routine_data,
    )

    # Hvis alt gik godt
    if response.status_code == 200:
        st.success("Morgenrutine gemt!")

    else:
        st.error("Noget gik galt ved gemning.")

st.subheader("Gemte morgenrutiner")

try:
    # Henter alle rutiner fra backend
    routines_response = requests.get("http://127.0.0.1:8000/routines")

    if routines_response.status_code == 200:
        routines = routines_response.json()

        if routines:
            st.dataframe(routines)
        else:
            st.info("Der er endnu ingen gemte rutiner.")
    else:
        st.error("Kunne ikke hente rutiner fra backend.")

except requests.exceptions.ConnectionError:
    st.error("Backend kører ikke. Start FastAPI-serveren først.")

    st.subheader("Statistik")

try:
    # Henter statistik fra backend
    statistics_response = requests.get("http://127.0.0.1:8000/statistics")

    if statistics_response.status_code == 200:
        statistics = statistics_response.json()

        st.metric("Gennemsnitlig søvn", f"{statistics['average_sleep']:.1f} timer")
        st.metric("Gennemsnitligt humør", f"{statistics['average_mood']:.1f} / 10")
        st.metric("Træningsdage", statistics["training_days"])
        st.metric("Antal registreringer", statistics["total_entries"])

    else:
        st.error("Kunne ikke hente statistik fra backend.")

except requests.exceptions.ConnectionError:
    st.error("Backend kører ikke. Start FastAPI-serveren først.")


    st.subheader("Humør over tid")

try:
    routines_response = requests.get("http://127.0.0.1:8000/routines")

    if routines_response.status_code == 200:
        routines = routines_response.json()

        if routines:
            import pandas as pd
            import matplotlib.pyplot as plt

            dataframe = pd.DataFrame(routines)

            fig, ax = plt.subplots()
            ax.plot(dataframe["date"], dataframe["mood"], marker="o")
            ax.set_xlabel("Dato")
            ax.set_ylabel("Humør")
            ax.set_title("Humør over tid")
            ax.tick_params(axis="x", rotation=45)

            st.pyplot(fig)
        else:
            st.info("Der er endnu ingen data til grafen.")

    else:
        st.error("Kunne ikke hente data til grafen.")

except requests.exceptions.ConnectionError:
    st.error("Backend kører ikke. Start FastAPI-serveren først.")


st.subheader("AI-feedback")

if st.button("Generér AI-feedback"):
    try:
        # Henter AI-feedback fra backend
        feedback_response = requests.get("http://127.0.0.1:8000/ai-feedback")

        if feedback_response.status_code == 200:
            feedback = feedback_response.json()["feedback"]
            st.info(feedback)
        else:
            st.error("Kunne ikke hente AI-feedback fra backend.")

    except requests.exceptions.ConnectionError:
        st.error("Backend kører ikke. Start FastAPI-serveren først.")