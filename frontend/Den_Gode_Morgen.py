import streamlit as st

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


# Navigation til appens tre hovedsider.
col1, col2, col3 = st.columns(3)


# Link til registreringssiden.
with col1:
    st.page_link(
        "pages/1_Dagen_i_dag.py",
        label="Registrering",
    )


# Link til statistik- og registreringssiden.
with col2:
    st.page_link(
        "pages/2_Registreringer.py",
        label="Statistik",
    )


# Link til AI-feedback-siden.
with col3:
    st.page_link(
        "pages/3_AI_Coach.py",
        label="AI-feedback",
    )