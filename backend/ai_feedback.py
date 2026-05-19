import os

import requests
from dotenv import load_dotenv


load_dotenv(".env")


def generate_simple_feedback(routine: dict) -> str:
    """
    Lokal fallback-feedback hvis Mistral API ikke svarer.
    """

    sleep_hours = float(routine.get("sleep_hours", 0) or 0)
    mood = int(routine.get("mood", 0) or 0)
    training = routine.get("training")
    shower_type = routine.get("shower_type", "ukendt")
    thoughts = routine.get("thoughts", "")

    feedback_parts = []

    if sleep_hours < 6:
        feedback_parts.append("Du har sovet lidt i nat, så det giver mening at holde dagen enkel.")
    else:
        feedback_parts.append("Din søvn ser fornuftig ud og giver et godt udgangspunkt for dagen.")

    if training is True:
        feedback_parts.append("Det er stærkt, at du har fået træning ind i rutinen.")
    else:
        feedback_parts.append("Hvis du har energi senere, kan en kort gåtur være et godt og realistisk valg.")

    feedback_parts.append(f"Dit valg af bad var: {shower_type}.")

    if mood <= 5:
        feedback_parts.append("Dit humør ligger lidt lavt, så vær ekstra venlig mod dig selv i dag.")
    else:
        feedback_parts.append("Dit humør ser stabilt ud, og det er et godt tegn.")

    if thoughts:
        feedback_parts.append("Det er positivt, at du sætter ord på dine tanker, fordi det giver mere klarhed.")

    feedback_parts.append("Fortsæt med små stabile skridt — det er sådan gode rutiner bygges.")

    return " ".join(feedback_parts)


def generate_ai_feedback(routine: dict) -> str:
    """
    Forsøger at hente feedback fra Mistral.
    Hvis API'et fejler, bruges lokal fallback-feedback.
    """

    api_key = os.getenv("MISTRAL_API_KEY")

    if not api_key:
        return generate_simple_feedback(routine)

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

        if response.status_code != 200:
            return generate_simple_feedback(routine)

        data = response.json()
        return data["choices"][0]["message"]["content"]

    except requests.exceptions.RequestException:
        return generate_simple_feedback(routine)