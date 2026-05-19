from pathlib import Path

import pandas as pd

from backend.models import RoutineEntry


DATA_FILE = Path("data/routines.csv")

COLUMNS = [
    "id",
    "date",
    "wake_up_time",
    "sleep_hours",
    "training",
    "shower_type",
    "breakfast",
    "water_glasses",
    "task_1",
    "task_2",
    "task_3",
    "mood",
    "thoughts",
]



def ensure_data_file_exists() -> None:
    """
    Sikrer at CSV-filen findes og har de rigtige kolonner.
    """

    if not DATA_FILE.exists() or DATA_FILE.stat().st_size == 0:
        pd.DataFrame(columns=COLUMNS).to_csv(DATA_FILE, index=False)
        return

    dataframe = pd.read_csv(DATA_FILE)

    for column in COLUMNS:
        if column not in dataframe.columns:
            dataframe[column] = ""

    dataframe = dataframe[COLUMNS]
    dataframe.to_csv(DATA_FILE, index=False)


def save_routine_entry(entry: RoutineEntry) -> dict:
    """
    Gemmer én morgenrutine.
    """

    ensure_data_file_exists()

    dataframe = pd.read_csv(DATA_FILE)

    next_id = 1 if dataframe.empty else int(dataframe["id"].max()) + 1

    new_data = entry.model_dump()
    new_data["id"] = next_id

    new_row = pd.DataFrame([new_data])

    updated_dataframe = pd.concat(
        [dataframe, new_row],
        ignore_index=True,
    )

    updated_dataframe.to_csv(DATA_FILE, index=False)

    return {
        "message": "Rutine gemt",
        "entry": new_data,
    }


def get_all_routine_entries() -> list[dict]:
    """
    Henter alle rutiner.
    """

    ensure_data_file_exists()

    dataframe = pd.read_csv(DATA_FILE)

    return dataframe.to_dict(orient="records")


def get_routines_dataframe() -> pd.DataFrame:
    """
    Returnerer data som Pandas DataFrame.
    """

    ensure_data_file_exists()

    return pd.read_csv(DATA_FILE)



def delete_routine_entry(entry_id: int) -> dict:
    """
    Sletter én registrering ud fra dens id.
    """

    ensure_data_file_exists()

    dataframe = pd.read_csv(DATA_FILE)

    if dataframe.empty or entry_id not in dataframe["id"].values:
        return {"message": "Registrering ikke fundet"}

    dataframe = dataframe[dataframe["id"] != entry_id]
    dataframe.to_csv(DATA_FILE, index=False)

    return {"message": "Registrering slettet"}