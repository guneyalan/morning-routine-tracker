import streamlit as st


st.set_page_config(
    page_title="",
    layout="wide",
    initial_sidebar_state="expanded",
)


st.markdown(
    """
    <style>
    #MainMenu, footer{visibility: hidden;}
    .stApp {background: #f5f5f3; color: #222;}
    .block-container {max-width: 900px; padding-top: 5rem;}
    </style>
    """,
    unsafe_allow_html=True,
)


st.title("Den gode morgen")

st.write(
    """
    Det er vigtigt med en god start på dagen. 

    En fast morgenrutine er guld værd. 
    
    Her kan du registrere dine morgenrutiner og få AI-feedback på dine rutiner

    Vi holder det simpelt og fokuserer på det vigtigste.
    """
)


col1, col2, col3 = st.columns(3)

with col1:
    st.page_link("pages/1_Dagen_i_dag.py", label="Registrering")

with col2:
    st.page_link("pages/2_Registreringer.py", label="Statistik")

with col3:
    st.page_link("pages/3_AI_Coach.py", label="AI-feedback")