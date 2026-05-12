import os

import requests
from dotenv import load_dotenv


load_dotenv()


def generate_simple_feedback(statistics: dict) -> str:
    """
    Laver en simpel fallback-feedback uden API.

    Denne funktion gør projektet stabilt til eksamen,
    selv hvis Mistral API-nøglen ikke er sat op.
    """

    average_sleep = statistics.get("average_sleep", 0)
    average_mood = statistics.get("average_mood", 0)

    if average_sleep < 6:
        return "Du sover forholdsvis lidt. Prøv at prioritere mere søvn."

    if average_mood >= 8:
        return "Dit gennemsnitlige humør ser stærkt ud. Din rutine virker stabil."

    return "Din morgenrutine er registreret fint. Fortsæt med at samle data."


def generate_ai_feedback(statistics: dict) -> str:
    """
    Forsøger at hente AI-feedback fra Mistral API.

    Hvis der ikke findes en API-nøgle, bruger programmet
    en simpel lokal fallback-feedback.
    """

    api_key = os.getenv("MISTRAL_API_KEY")

    if not api_key:
        return generate_simple_feedback(statistics)

    prompt = f"""
    Giv kort og konkret feedback på denne morgenrutine-statistik:
    {statistics}

    Svar på dansk i 2-3 sætninger.
    """

    response = requests.post(
        "https://api.mistral.ai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json={
            "model": "mistral-small-latest",
            "messages": [
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        },
        timeout=20,
    )

    if response.status_code != 200:
        return generate_simple_feedback(statistics)

    data = response.json()

    return data["choices"][0]["message"]["content"]