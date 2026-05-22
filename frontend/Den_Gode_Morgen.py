import sys
from pathlib import Path

import streamlit as st

sys.path.append(str(Path(__file__).resolve().parents[1]))

from styles import apply_base_style


# Konfigurerer forsiden.
# wide-layout giver mere plads til sidens indhold.
st.set_page_config(
    page_title="Den gode morgen",
    layout="wide",
    initial_sidebar_state="expanded",
)


# Indlæser fælles CSS-styling.
# Styling ligger i styles.py for at undgå gentaget CSS-kode.
st.markdown(
    apply_base_style(),
    unsafe_allow_html=True,
)


# Forsidens hovedtitel.
st.title("Den gode morgen")


# Kort introduktion til appens formål.
st.write(
    """
    Det er vigtigt med en god start på dagen.

    En fast morgenrutine er guld værd.

    Her kan du registrere dine morgenrutiner og få AI-feedback på dine rutiner.

    Vi holder det simpelt og fokuserer på det vigtigste.
    """
)

