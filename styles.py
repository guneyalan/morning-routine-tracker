# Funktion som returnerer fælles CSS-styling.
# Formålet er at undgå gentaget styling-kode på alle Streamlit-sider.
def apply_base_style() -> str:

    return """
    <style>

    /* Skjuler Streamlits standardmenu og footer */
    #MainMenu, footer {
        visibility: hidden;
    }

    /* Overordnet styling af appens baggrund og tekst */
    .stApp {
        background-color: #f3f4f6;
        color: #111827;
    }

    /* Giver siderne en mere clean og centreret bredde */
    .block-container {
        max-width: 950px;
        padding-top: 2rem;
        padding-bottom: 4rem;
        padding-left: 1rem;
        padding-right: 1rem;
    }

    /* Styling af container-bokse */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #ffffff;
        border: 2px solid #cbd5e1;
        border-radius: 18px;
        padding: 22px;
        margin-bottom: 20px;
        box-shadow: 0 4px 14px rgba(15, 23, 42, 0.08);
    }

    /* Gør tekst tydelig og læsbar */
    h1, h2, h3, label, p, span {
        color: #111827 !important;
    }

    /* Flytter submit-knapper mod højre */
    div[data-testid="stFormSubmitButton"] {
        display: flex;
        justify-content: flex-end;
    }

    /* Styling af submit-knapper */
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

    /* Sikrer hvid tekst inde i knappen */
    div[data-testid="stFormSubmitButton"] button p {
        color: #ffffff !important;
    }

    </style>
    """