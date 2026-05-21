from pathlib import Path
import pandas as pd
from backend.models import RoutineEntry


# Sti til CSV-filen hvor alle morgenrutiner gemmes.
DATA_FILE = Path("data/routines.csv")


# Alle kolonner som CSV-filen skal indeholde.
# Bruges for at sikre korrekt struktur i datafilen.
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


# Sikrer at CSV-filen eksisterer og har de korrekte kolonner.
# Hvis filen mangler eller er tom, oprettes en ny CSV-fil.
def ensure_data_file_exists() -> None:

    # Opretter tom CSV-fil hvis filen ikke findes endnu.
    if not DATA_FILE.exists() or DATA_FILE.stat().st_size == 0:
        pd.DataFrame(columns=COLUMNS).to_csv(DATA_FILE, index=False)
        return

    # Indlæser eksisterende datafil som Pandas DataFrame.
    dataframe = pd.read_csv(DATA_FILE)

    # Sikrer at alle nødvendige kolonner eksisterer.
    # Hvis en kolonne mangler, oprettes den automatisk.
    for column in COLUMNS:
        if column not in dataframe.columns:
            dataframe[column] = ""

    # Sørger for korrekt rækkefølge på kolonnerne.
    dataframe = dataframe[COLUMNS]

    # Gemmer den opdaterede CSV-fil.
    dataframe.to_csv(DATA_FILE, index=False)


# Gemmer én ny morgenrutine i CSV-filen.
def save_routine_entry(entry: RoutineEntry) -> dict:

    # Sikrer at datafilen eksisterer før vi arbejder med den.
    ensure_data_file_exists()

    # Indlæser eksisterende registreringer.
    dataframe = pd.read_csv(DATA_FILE)

    # Genererer automatisk næste id.
    # Hvis filen er tom starter id ved 1.
    next_id = 1 if dataframe.empty else int(dataframe["id"].max()) + 1

    # Konverterer Pydantic-modellen til dictionary.
    new_data = entry.model_dump()

    # Tilføjer det genererede id til registreringen.
    new_data["id"] = next_id

    # Konverterer registreringen til DataFrame.
    new_row = pd.DataFrame([new_data])

    # Tilføjer den nye registrering til eksisterende data.
    updated_dataframe = pd.concat(
        [dataframe, new_row],
        ignore_index=True,
    )

    # Gemmer den opdaterede CSV-fil.
    updated_dataframe.to_csv(DATA_FILE, index=False)

    return {
        "message": "Rutine gemt",
        "entry": new_data,
    }


# Henter alle registreringer fra CSV-filen.
# Bruges blandt andet af frontend til visning af registreringer.
def get_all_routine_entries() -> list[dict]:

    ensure_data_file_exists()

    # Indlæser alle data som DataFrame.
    dataframe = pd.read_csv(DATA_FILE)

    # Konverterer DataFrame til liste af dictionaries.
    return dataframe.to_dict(orient="records")


# Returnerer hele datasættet som Pandas DataFrame.
# Bruges især til statistik og analyse.
def get_routines_dataframe() -> pd.DataFrame:

    ensure_data_file_exists()

    return pd.read_csv(DATA_FILE)


# Sletter én registrering ud fra dens id.
def delete_routine_entry(entry_id: int) -> dict:

    ensure_data_file_exists()

    # Indlæser alle registreringer.
    dataframe = pd.read_csv(DATA_FILE)

    # Tjekker om registreringen eksisterer.
    # Hvis ikke returneres en fejlbesked.
    if dataframe.empty or entry_id not in dataframe["id"].values:
        return {"message": "Registrering ikke fundet"}

    # Fjerner den valgte registrering fra DataFrame.
    dataframe = dataframe[dataframe["id"] != entry_id]

    # Gemmer den opdaterede CSV-fil.
    dataframe.to_csv(DATA_FILE, index=False)

    return {"message": "Registrering slettet"}