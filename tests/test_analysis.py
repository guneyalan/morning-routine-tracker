import pandas as pd

from backend.analysis import (
    calculate_average_mood,
    calculate_average_sleep,
    count_training_days,
)


# Tester funktionen som beregner gennemsnitlig søvn.
# Testen sikrer at NumPy og Pandas-beregningen virker korrekt.
def test_calculate_average_sleep():
    """
    Tester at gennemsnitlig søvn beregnes korrekt.
    """

    # Opretter test-data som DataFrame.
    dataframe = pd.DataFrame(
        {
            "sleep_hours": [7.0, 8.0, 6.0],
        }
    )

    # Kalder funktionen som skal testes.
    result = calculate_average_sleep(dataframe)

    # Forventer gennemsnittet 7.0.
    assert result == 7.0


# Tester funktionen som beregner gennemsnitligt humør.
def test_calculate_average_mood():
    """
    Tester at gennemsnitligt humør beregnes korrekt.
    """

    # Test-data med humør-værdier.
    dataframe = pd.DataFrame(
        {
            "mood": [8, 6, 10],
        }
    )

    # Kalder analysefunktionen.
    result = calculate_average_mood(dataframe)

    # Gennemsnittet forventes at være 8.0.
    assert result == 8.0


# Tester funktionen som tæller træningsdage.
def test_count_training_days():
    """
    Tester at antal træningsdage tælles korrekt.
    """

    # True betyder at brugeren har trænet.
    # False betyder ingen træning.
    dataframe = pd.DataFrame(
        {
            "training": [True, False, True],
        }
    )

    # Kalder funktionen som tæller træningsdage.
    result = count_training_days(dataframe)

    # Forventer at to dage tælles som træningsdage.
    assert result == 2