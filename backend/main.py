from backend.ai_feedback import generate_ai_feedback

from backend.analysis import (
    calculate_average_mood,
    calculate_average_sleep,
    count_training_days,
)
from backend.storage import get_routines_dataframe

from backend.storage import delete_routine_entry
from fastapi import FastAPI

from backend.models import RoutineEntry
from backend.storage import get_all_routine_entries, save_routine_entry


# Opretter FastAPI-applikationen
app = FastAPI()


@app.get("/")
def root():
    """
    Simpelt endpoint som bruges til at teste,
    om backend-serveren kører korrekt.
    """

    return {
        "message": "Morning Routine Tracker API virker"
    }


@app.get("/health")
def health_check():
    """
    Health-check endpoint.
    Bruges til at kontrollere om serveren er stabil.
    """

    return {
        "status": "healthy"
    }


@app.post("/routines")
def create_routine(entry: RoutineEntry):
    """
    Modtager én morgenrutine fra frontend.

    FastAPI validerer automatisk data med RoutineEntry-modellen.
    Derefter gemmes rutinen i CSV-filen via storage.py.
    """

    return save_routine_entry(entry)


@app.get("/routines")
def read_routines():
    """
    Henter alle gemte morgenrutiner.

    Data læses fra CSV-filen og sendes tilbage som JSON.
    """

    return get_all_routine_entries()

@app.get("/statistics")
def get_statistics():
    """
    Beregner statistik for alle gemte morgenrutiner.

    Endpointet viser at backend ikke kun gemmer data,
    men også kan analysere data med Pandas og NumPy.
    """

    dataframe = get_routines_dataframe()

    return {
        "average_sleep": calculate_average_sleep(dataframe),
        "average_mood": calculate_average_mood(dataframe),
        "training_days": count_training_days(dataframe),
        "total_entries": len(dataframe),
    }


@app.get("/ai-feedback")
def get_ai_feedback():
    """
    Genererer AI-feedback på den seneste morgenrutine.

    Feedbacken bruger både tal, valg, opgaver og brugerens egne tanker.
    """

    dataframe = get_routines_dataframe()

    if dataframe.empty:
        return {
            "feedback": "Der er endnu ingen registreringer at give feedback på."
        }

    latest_entry = dataframe.tail(1).to_dict(orient="records")[0]

    feedback = generate_ai_feedback(latest_entry)

    return {
        "feedback": feedback
    }