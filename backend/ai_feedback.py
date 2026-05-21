import os

import requests
from dotenv import load_dotenv


# Indlæser miljøvariabler fra .env-filen.
# Her ligger blandt andet Mistral API-nøglen.
load_dotenv(".env")


# Lokal fallback-funktion.
# Bruges hvis Mistral API ikke svarer, eller hvis API-nøglen mangler.
def generate_simple_feedback(routine: dict) -> str:
   

    # Henter centrale værdier fra den seneste morgenregistrering.
    # Hvis en værdi mangler, bruges en sikker standardværdi.
    sleep_hours = float(routine.get("sleep_hours", 0) or 0)
    mood = int(routine.get("mood", 0) or 0)
    training = routine.get("training")
    shower_type = routine.get("shower_type", "ukendt")
    thoughts = routine.get("thoughts", "")

    # Liste som samler de enkelte dele af feedbacken.
    feedback_parts = []

    # Søvn vurderes først, fordi søvn har stor betydning for resten af dagen.
    if sleep_hours < 6:
        feedback_parts.append("Du har sovet lidt i nat, så det giver mening at holde dagen enkel.")
    else:
        feedback_parts.append("Din søvn ser fornuftig ud og giver et godt udgangspunkt for dagen.")

    # Træning vurderes som et simpelt ja/nej-felt.
    if training is True:
        feedback_parts.append("Det er stærkt, at du har fået træning ind i rutinen.")
    else:
        feedback_parts.append("Hvis du har energi senere, kan en kort gåtur være et godt og realistisk valg.")

    # Bad-type nævnes direkte, fordi det er en del af brugerens morgenrutine.
    feedback_parts.append(f"Dit valg af bad var: {shower_type}.")

    # Humør vurderes ud fra en skala fra 1 til 10.
    if mood <= 5:
        feedback_parts.append("Dit humør ligger lidt lavt, så vær ekstra venlig mod dig selv i dag.")
    else:
        feedback_parts.append("Dit humør ser stabilt ud, og det er et godt tegn.")

    # Hvis brugeren har skrevet tanker, anerkendes det i feedbacken.
    if thoughts:
        feedback_parts.append("Det er positivt, at du sætter ord på dine tanker, fordi det giver mere klarhed.")

    # Feedbacken afsluttes altid positivt.
    feedback_parts.append("Fortsæt med små stabile skridt — det er sådan gode rutiner bygges.")

    # Samler alle dele til én samlet tekst.
    return " ".join(feedback_parts)


# AI-feedback-funktion.
# Forsøger først at bruge Mistral API og falder ellers tilbage på lokal feedback.
def generate_ai_feedback(routine: dict) -> str:
    

    # Henter Mistral API-nøglen fra miljøvariabler.
    api_key = os.getenv("MISTRAL_API_KEY")

    # Hvis nøglen ikke findes, bruges fallback med det samme.
    if not api_key:
        return generate_simple_feedback(routine)

    # Prompten er den tekst, vi sender til Mistral.
    # Her fortæller vi modellen præcis hvilken rolle den har,
    # hvilke data den skal bruge, og hvordan den skal svare.
    prompt = f"""
Du er en rolig og støttende morgenrutine-coach.

Giv kort og personlig feedback på denne morgenregistrering:

Dato: {routine.get("date")}
Stod op: {routine.get("wake_up_time")}
Søvn: {routine.get("sleep_hours")} timer
Træning: {routine.get("training")}
Bad: {routine.get("shower_type")}
Morgenmad: {routine.get("breakfast")}
Vand: {routine.get("water_glasses")} glas
Humør: {routine.get("mood")}/10

Dagens tre vigtigste opgaver:
1. {routine.get("task_1")}
2. {routine.get("task_2")}
3. {routine.get("task_3")}

Tanker:
{routine.get("thoughts")}

Krav:
- Svar på dansk
- Maksimalt 5 sætninger
- Kommentér rutiner, opgaver og tanker
- Giv ét konkret råd
- Slut positivt og opløftende
- Brug aldrig emojis
"""

    try:
        # Sender HTTP POST-request til Mistral API.
        # Authorization-headeren indeholder API-nøglen.
        response = requests.post(
            "https://api.mistral.ai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
            json={
                "model": "open-mistral-7b",
                "messages": [{"role": "user", "content": prompt}],
            },
            timeout=8,
        )

        # Hvis Mistral ikke svarer korrekt, bruges fallback.
        # Det gør appen mere stabil til demo og eksamen.
        if response.status_code != 200:
            return generate_simple_feedback(routine)

        # Konverterer Mistrals svar fra JSON til Python-dict.
        data = response.json()

        # Returnerer selve AI-teksten fra Mistrals response.
        return data["choices"][0]["message"]["content"]

    # Hvis requestet fejler helt, bruges fallback.
    except requests.exceptions.RequestException:
        return generate_simple_feedback(routine)