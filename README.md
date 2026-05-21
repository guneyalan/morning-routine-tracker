# Den Gode Morgen

Er en simpel og morgenrutine-app bygget i Python.

Appen gør det muligt at registrere sine morgenrutiner, gemme data lokalt, se statistik og få AI-genereret feedback baseret på dagens registrering. 

Formålet med dette projekt er at kombinere:
- frontend
- backend
- dataanalyse
- AI-integration
-softwarestruktur

i én samlet applikation.

---

# Features

- Registrering af morgenrutiner
- Statistik og visualiseringer
- AI-feedback via Mistral API
- Lokal lagring af data i CSV
- Mulighed for at slette registreringer
- Moderne og minimalistisk brugerflade

---

# Morgenregistrering

Brugeren kan registrere:

- Dato
- Dagens 3 vigtigste opgaver
- Søvn og tidspunkt man stod op
- Træning
- Bad
- Morgenmad
- Vandindtag
- Humør
- Tanker og refleksioner

---

# Teknologier

Projektet er bygget med:

- Python
- Streamlit
- FastAPI
- Pandas
- NumPy
- Matplotlib
- Mistral API
- Pytest
- MyPy
- Ruff

---

# Projektstruktur

```text
backend/
frontend/
tests/
data/

---


# Installation

1. klon repository
git clone https://github.com/guneyalan/morning-routine-tracker.git

2. gå ind i projektmappen
cd morning-routine-tracker

3. Opret virtual environment
python3 -m venv .venv

4. Aktiver virtual environment
source .venv/bin/activate

5. Installér dependencies
pip install -r requirements.txt


---

# Start applikationen

1. Start backend
python3 -m uvicorn backend.main:app --reload
backend kører her: http://127.0.0.1:8000

2. start frontend
streamlit run frontend/Den_Gode_Morgen.py
frontend kører her: http://localhost:8501


---

# AI feedback

Appen bruger Mistral API til at generere personlig feedback baseret på brugerens morgenrutine.

AI-feedback tager højde for:

Søvn
Humør
Træning
Bad
Vand
Opgaver
Tanker og refleksioner

Hvis AI-servicen ikke er tilgængelig, bruges lokal fallback-feedback.

----

#Statistik
Appen viser blandt andet:

Gennemsnitlig søvn
Gennemsnitligt humør
Antal registreringer
Graf over humør over tid

-----

#Test og kodekvalitet

1. Kør test:
pytest

Type Checking:
mypy backend

Kode analyse:
ruff check .

# Data

Data gemmes lokalt i data/routines.csv










