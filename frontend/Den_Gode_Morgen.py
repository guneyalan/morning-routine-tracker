import streamlit as st


# Konfigurerer Streamlit-siden.
# wide-layout giver mere plads til indholdet.
# expanded gør at sidebar starter åben.
st.set_page_config(
    page_title="",
    layout="wide",
    initial_sidebar_state="expanded",
)


# Custom CSS styling.
# Bruges til at skabe et mere moderne og minimalistisk design.
st.markdown(
    """
    <style>

    /* Skjuler Streamlits standardmenu og footer */
    #MainMenu, footer{
        visibility: hidden;
    }

    /* Overordnet styling af appens baggrund og tekstfarver */
    .stApp {
        background: #f5f5f3;
        color: #222;
    }

    /* Begrænser bredden på indholdet
       så layoutet bliver mere clean og læsbart */
    .block-container {
        max-width: 900px;
        padding-top: 5rem;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# Hovedtitel på forsiden.
st.title("Den gode morgen")


# Kort introduktion til appens formål.
# Forklarer brugeren hvad applikationen bruges til.
st.write(
    """
    Det er vigtigt med en god start på dagen. 

    En fast morgenrutine er guld værd. 
    
    Her kan du registrere dine morgenrutiner og få AI-feedback på dine rutiner.

    Vi holder det simpelt og fokuserer på det vigtigste.
    """
)


# Opretter tre kolonner som bruges til navigation mellem siderne.
col1, col2, col3 = st.columns(3)


# Link til registreringssiden.
with col1:
    st.page_link(
        "pages/1_Dagen_i_dag.py",
        label="Registrering",
    )


# Link til statistik-siden.
with col2:
    st.page_link(
        "pages/2_Registreringer.py",
        label="Statistik",
    )


# Link til AI-feedback siden.
with col3:
    st.page_link(
        "pages/3_AI_Coach.py",
        label="AI-feedback",
    )