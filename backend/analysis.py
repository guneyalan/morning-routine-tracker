import numpy as np
import pandas as pd


# Beregner gennemsnitlig søvn ud fra alle registreringer.
# Funktionen bruger både Pandas og NumPy.
def calculate_average_sleep(dataframe: pd.DataFrame) -> float:
    

    # Hvis DataFrame er tom returneres 0,
    # så programmet ikke crasher.
    if dataframe.empty:
        return 0.0

    # Beregner gennemsnittet af kolonnen sleep_hours.
    return float(np.mean(dataframe["sleep_hours"]))


# Beregner gennemsnitligt humør.
# Humør registreres på en skala fra 1 til 10.
def calculate_average_mood(dataframe: pd.DataFrame) -> float:
    

    # Returnerer 0 hvis der endnu ikke findes data.
    if dataframe.empty:
        return 0.0

    # Beregner gennemsnittet af alle humør-registreringer.
    return float(np.mean(dataframe["mood"]))


# Tæller hvor mange dage brugeren har trænet.
# Kolonnen training indeholder True eller False.
def count_training_days(dataframe: pd.DataFrame) -> int:
    

    # Returnerer 0 hvis der ikke findes registreringer endnu.
    if dataframe.empty:
        return 0

    # Summerer alle True-værdier i training-kolonnen.
    # True tælles som 1 og False som 0.
    return int(dataframe["training"].sum())