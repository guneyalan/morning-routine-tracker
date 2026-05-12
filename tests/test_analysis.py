import pandas as pd

from backend.analysis import (
    calculate_average_mood,
    calculate_average_sleep,
    count_training_days,
)


def test_calculate_average_sleep():
    """
    Tester at gennemsnitlig søvn beregnes korrekt.
    """

    dataframe = pd.DataFrame(
        {
            "sleep_hours": [7.0, 8.0, 6.0],
        }
    )

    result = calculate_average_sleep(dataframe)

    assert result == 7.0


def test_calculate_average_mood():
    """
    Tester at gennemsnitligt humør beregnes korrekt.
    """

    dataframe = pd.DataFrame(
        {
            "mood": [8, 6, 10],
        }
    )

    result = calculate_average_mood(dataframe)

    assert result == 8.0


def test_count_training_days():
    """
    Tester at antal træningsdage tælles korrekt.
    """

    dataframe = pd.DataFrame(
        {
            "training": [True, False, True],
        }
    )

    result = count_training_days(dataframe)

    assert result == 2