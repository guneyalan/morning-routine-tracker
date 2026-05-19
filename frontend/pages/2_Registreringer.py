import matplotlib.pyplot as plt
import pandas as pd
import requests
import streamlit as st


API_URL = "http://127.0.0.1:8000"


st.set_page_config(
    page_title="Statistik",
    layout="wide",
)


st.markdown(
    """
    <style>
    #MainMenu, footer{visibility: hidden;}
    .stApp {background: #f5f5f3; color: #222;}
    .block-container {max-width: 1100px; padding-top: 2rem;}
    </style>
    """,
    unsafe_allow_html=True,
)


st.title("Registreringer og statistik")

try:
    routines = requests.get(f"{API_URL}/routines").json()
    statistics = requests.get(f"{API_URL}/statistics").json()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Søvn", f"{statistics['average_sleep']:.1f} timer")
    col2.metric("Humør", f"{statistics['average_mood']:.1f} / 10")
    col3.metric("Træningsdage", statistics["training_days"])
    col4.metric("Registreringer", statistics["total_entries"])

    st.divider()

    if routines:
        st.subheader("Humør over tid")

        df = pd.DataFrame(routines)

        fig, ax = plt.subplots(figsize=(10, 4))

        fig.patch.set_facecolor("#f5f5f3")
        ax.set_facecolor("#f5f5f3")

        ax.plot(
            df["date"],
            df["mood"],
            marker="o",
            linewidth=2.5,
        )

        ax.fill_between(
            df["date"],
            df["mood"],
            alpha=0.12,
        )

        ax.set_xlabel("Dato")
        ax.set_ylabel("Humør")
        ax.tick_params(axis="x", rotation=25)

        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.grid(alpha=0.2)

        st.pyplot(fig, use_container_width=True)

        st.subheader("Data")
        st.dataframe(routines, use_container_width=True)
        
      





    else:
        st.info("Der er endnu ingen data.")

except requests.exceptions.ConnectionError:
    st.error("Backend kører ikke. Start FastAPI-serveren først.")


 