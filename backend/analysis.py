import numpy as np
import pandas as pd


def calculate_average_sleep(dataframe: pd.DataFrame) -> float:
    """
    Beregner gennemsnitlig søvn.

    Funktionen bruger Pandas til at hente kolonnen sleep_hours
    og NumPy til at beregne gennemsnittet.
    """

    if dataframe.empty:
        return 0.0

    return float(np.mean(dataframe["sleep_hours"]))


def calculate_average_mood(dataframe: pd.DataFrame) -> float:
    """
    Beregner gennemsnitligt humør.

    Humør måles fra 1 til 10.
    """

    if dataframe.empty:
        return 0.0

    return float(np.mean(dataframe["mood"]))


def count_training_days(dataframe: pd.DataFrame) -> int:
    """
    Tæller hvor mange dage brugeren har trænet.

    Kolonnen training indeholder True eller False.
    """

    if dataframe.empty:
        return 0

    return int(dataframe["training"].sum())