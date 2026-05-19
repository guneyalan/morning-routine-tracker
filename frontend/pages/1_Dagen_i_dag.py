import requests
import streamlit as st


API_URL = "http://127.0.0.1:8000"


st.set_page_config(
    page_title="Registrering",
    layout="centered",
    initial_sidebar_state="expanded",
)


st.markdown(
    """
    <style>
    #MainMenu, footer {
        visibility: hidden;
    }

    .stApp {
        background-color: #f3f4f6;
        color: #111827;
    }

    .block-container {
    max-width: 950px;
    padding-top: 2rem;
    padding-bottom: 4rem;
    padding-left: 1rem;
    padding-right: 1rem;
    }

    div[data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #ffffff;
        border: 2px solid #cbd5e1;
        border-radius: 18px;
        padding: 22px;
        margin-bottom: 20px;
        box-shadow: 0 4px 14px rgba(15, 23, 42, 0.08);
    }

    h1, h2, h3, label, p, span {
        color: #111827 !important;
    }

div[data-testid="stFormSubmitButton"] {
    display: flex;
    justify-content: flex-end;
}

div[data-testid="stFormSubmitButton"] button {
    width: 260px;
    height: 55px;
    border-radius: 12px;
    border: none;
    background-color: #111827 !important;
    color: #ffffff !important;
    font-size: 18px;
    font-weight: 600;
}

div[data-testid="stFormSubmitButton"] button p {
    color: #ffffff !important;


}
</style>
    """,
    unsafe_allow_html=True,
)


st.title("Registrering")


with st.form("routine_form"):

    with st.container(border=True):
        st.subheader("Dato")

        date = st.date_input("Dato")


    with st.container(border=True):
        st.subheader("Dagens tre vigtigste opgaver")

        task_1 = st.text_input("Opgave 1")
        task_2 = st.text_input("Opgave 2")
        task_3 = st.text_input("Opgave 3")


    with st.container(border=True):
        st.subheader("Søvn")

        wake_up_time = st.text_input(
            "Hvornår stod du op?",
            "05:30",
        )

        sleep_hours = st.number_input(
            "Timer sovet",
            0.0,
            24.0,
            7.5,
            0.5,
        )


    with st.container(border=True):
        st.subheader("Træning")

        training = st.radio(
            "Har du trænet?",
            ["Ja", "Nej"],
            horizontal=True,
        ) == "Ja"


    with st.container(border=True):
        st.subheader("Bad")

        shower_type = st.selectbox(
            "Bad-type",
            [
                "normalt bad",
                "koldt bad",
                "intet bad",
            ],
        )


    with st.container(border=True):
        st.subheader("Morgenmad")

        breakfast = st.radio(
            "Har du spist morgenmad?",
            ["Ja", "Nej"],
            horizontal=True,
        ) == "Ja"


    with st.container(border=True):
        st.subheader("Vand")

        water_glasses = st.number_input(
            "Antal glas vand",
            0,
            30,
            3,
        )


    with st.container(border=True):
        st.subheader("Humør")

        mood = st.slider(
            "Humør",
            1,
            10,
            8,
        )

        thoughts = st.text_area(
            "Hvilke tanker fylder i dag?",
            height=120,
        )


    submitted = st.form_submit_button("Gem morgenrutine")


if submitted:

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
        response = requests.post(
            f"{API_URL}/routines",
            json=data,
        )

        if response.status_code == 200:
            st.success("Morgenrutine gemt")

        else:
            st.error("Noget gik galt")

    except requests.exceptions.ConnectionError:
        st.error("Backend kører ikke")