from fastapi import FastAPI

from backend.ai_feedback import generate_ai_feedback
from backend.analysis import (
    calculate_average_mood,
    calculate_average_sleep,
    count_training_days,
)
from backend.models import RoutineEntry
from backend.storage import (
    delete_routine_entry,
    get_all_routine_entries,
    get_routines_dataframe,
    save_routine_entry,
)


# Opretter selve FastAPI-applikationen.
# Det er denne app, som uvicorn starter, når backend-serveren køres.
app = FastAPI()


# Simpelt root-endpoint.
# Bruges primært til hurtigt at teste om backend-serveren svarer.
@app.get("/")
def root():
    return {
        "message": "Morning Routine Tracker API virker"
    }


# Health-check endpoint.
# Bruges til at kontrollere at backend-serveren kører stabilt.
@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


# POST-endpoint til at oprette en ny morgenrutine.
# FastAPI bruger RoutineEntry-modellen til automatisk at validere inputdata.
@app.post("/routines")
def create_routine(entry: RoutineEntry):
    # Sender den validerede registrering videre til storage-laget,
    # hvor den bliver gemt i CSV-filen.
    return save_routine_entry(entry)


# GET-endpoint til at hente alle gemte morgenrutiner.
# Bruges af frontend, når registreringerne skal vises i appen.
@app.get("/routines")
def read_routines():
    return get_all_routine_entries()


# GET-endpoint til statistik.
# Her hentes data som Pandas DataFrame og analyseres med hjælpefunktioner.
@app.get("/statistics")
def get_statistics():
    dataframe = get_routines_dataframe()

    # Returnerer de vigtigste nøgletal som JSON,
    # så Streamlit kan vise dem i frontend.
    return {
        "average_sleep": calculate_average_sleep(dataframe),
        "average_mood": calculate_average_mood(dataframe),
        "training_days": count_training_days(dataframe),
        "total_entries": len(dataframe),
    }


# GET-endpoint til AI-feedback.
# Bruger den seneste registrering som grundlag for feedbacken.
@app.get("/ai-feedback")
def get_ai_feedback():
    dataframe = get_routines_dataframe()

    # Hvis der ikke findes data endnu, returneres en venlig besked
    # i stedet for at backend crasher.
    if dataframe.empty:
        return {
            "feedback": "Der er endnu ingen registreringer at give feedback på."
        }

    # Henter den nyeste registrering fra CSV-filen.
    # tail(1) tager den sidste række i DataFrame.
    latest_entry = dataframe.tail(1).to_dict(orient="records")[0]

    # Sender den seneste registrering til AI-modulet,
    # som enten bruger Mistral API eller lokal fallback-feedback.
    feedback = generate_ai_feedback(latest_entry)

    return {
        "feedback": feedback
    }


# DELETE-endpoint til at slette en bestemt registrering.
# Frontend sender id'et på den registrering, der skal slettes.
@app.delete("/routines/{entry_id}")
def delete_routine(entry_id: int):
    return delete_routine_entry(entry_id)