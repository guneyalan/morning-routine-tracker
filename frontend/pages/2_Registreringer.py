
import matplotlib.pyplot as plt
import pandas as pd

import sys
from pathlib import Path

import os
import requests
import streamlit as st

sys.path.append(str(Path(__file__).resolve().parents[2]))

from styles import apply_base_style


# URL til FastAPI-backend.
# Denne side bruger backend til at hente registreringer og statistik.
API_URL = os.getenv("API_URL", "http://127.0.0.1:8000")


# Konfigurerer Streamlit-siden.
# wide-layout giver god plads til statistik og graf.
st.set_page_config(
    page_title="Statistik",
    layout="wide",
)


# Indlæser fælles CSS-styling.
# Styling ligger i styles.py for at undgå gentaget CSS-kode.
st.markdown(
    apply_base_style(),
    unsafe_allow_html=True,
)



# Titel på siden.
st.title("Registreringer og statistik")


try:
    # Henter alle gemte registreringer fra backend.
    routines = requests.get(f"{API_URL}/routines").json()

    # Henter beregnet statistik fra backend.
    statistics = requests.get(f"{API_URL}/statistics").json()

    # Viser statistik i fire kolonner.
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Søvn", f"{statistics['average_sleep']:.1f} timer")
    col2.metric("Humør", f"{statistics['average_mood']:.1f} / 10")
    col3.metric("Træningsdage", statistics["training_days"])
    col4.metric("Registreringer", statistics["total_entries"])

    st.divider()

    # Hvis der findes registreringer, vises graf og tabel.
    if routines:
        st.subheader("Humør over tid")

        # Konverterer JSON-data til Pandas DataFrame.
        # Det gør data lettere at arbejde med i Matplotlib.
        df = pd.DataFrame(routines)

        # Opretter Matplotlib-figur og akse.
        fig, ax = plt.subplots(figsize=(10, 4))

        # Matcher grafens baggrund med sidens baggrund.
        fig.patch.set_facecolor("#f5f5f3")
        ax.set_facecolor("#f5f5f3")

        # Tegner graf over humør over tid.
        ax.plot(
            df["date"],
            df["mood"],
            marker="o",
            linewidth=2.5,
        )

        # Tilføjer let udfyldning under grafen for bedre visuelt udtryk.
        ax.fill_between(
            df["date"],
            df["mood"],
            alpha=0.12,
        )

        # Navne på akser.
        ax.set_xlabel("Dato")
        ax.set_ylabel("Humør")

        # Roterer datoer på x-aksen så de er lettere at læse.
        ax.tick_params(axis="x", rotation=25)

        # Fjerner øverste og højre kant for et mere moderne look.
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

        # Tilføjer diskret grid.
        ax.grid(alpha=0.2)

        # Viser grafen i Streamlit.
        st.pyplot(fig, use_container_width=True)

        # Viser alle registreringer i en tabel.
        st.subheader("Data")
        st.dataframe(routines, use_container_width=True)

    # Hvis der ikke findes data endnu.
    else:
        st.info("Der er endnu ingen data.")

# Hvis backend ikke kører, vises en tydelig fejlbesked.
except requests.exceptions.ConnectionError:
    st.error("Backend kører ikke. Start FastAPI-serveren først.")