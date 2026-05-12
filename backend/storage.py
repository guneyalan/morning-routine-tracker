from pathlib import Path

import pandas as pd

from backend.models import RoutineEntry


DATA_FILE = Path("data/routines.csv")


def ensure_data_file_exists() -> None:
    """
    Sikrer at CSV-filen findes og har de rigtige kolonner.

    Funktionen bruges før vi læser eller skriver data,
    så programmet ikke crasher hvis filen er tom eller mangler.
    """

    if not DATA_FILE.exists() or DATA_FILE.stat().st_size == 0:
        columns = [
            "date",
            "sleep_hours",
            "water_glasses",
            "training",
            "meditation",
            "mood",
            "shower_type",
        ]

        empty_dataframe = pd.DataFrame(columns=columns)
        empty_dataframe.to_csv(DATA_FILE, index=False)


def save_routine_entry(entry: RoutineEntry) -> dict:
    """
    Gemmer én morgenrutine i CSV-filen.

    Først læser vi eksisterende data.
    Derefter tilføjer vi den nye række.
    Til sidst gemmer vi hele CSV-filen igen.
    """

    ensure_data_file_exists()

    dataframe = pd.read_csv(DATA_FILE)

    new_row = pd.DataFrame([entry.model_dump()])

    updated_dataframe = pd.concat(
        [dataframe, new_row],
        ignore_index=True,
    )

    updated_dataframe.to_csv(DATA_FILE, index=False)

    return {
        "message": "Rutine gemt",
        "entry": entry.model_dump(),
    }


def get_all_routine_entries() -> list[dict]:
    """
    Henter alle morgenrutiner fra CSV-filen.

    Data returneres som en liste af dictionaries,
    fordi FastAPI nemt kan sende det tilbage som JSON.
    """

    ensure_data_file_exists()

    dataframe = pd.read_csv(DATA_FILE)

    return dataframe.to_dict(orient="records")

def get_routines_dataframe() -> pd.DataFrame:
    """
    Henter alle morgenrutiner som en Pandas DataFrame.

    Denne funktion bruges af analyse-delen,
    fordi Pandas og NumPy arbejder bedst med DataFrames.
    """

    ensure_data_file_exists()

    return pd.read_csv(DATA_FILE)