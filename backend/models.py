from pydantic import BaseModel, Field


class RoutineEntry(BaseModel):
    """
    Datamodel for én morgenrutine.

    FastAPI bruger denne klasse til at validere data,
    når frontend sender en ny rutine til backend.
    """

    date: str = Field(..., description="Dato for registreringen")
    sleep_hours: float = Field(..., ge=0, le=24, description="Antal timers søvn")
    water_glasses: int = Field(..., ge=0, le=30, description="Antal glas vand")
    training: bool = Field(..., description="Om brugeren har trænet")
    meditation: bool = Field(..., description="Om brugeren har mediteret")
    mood: int = Field(..., ge=1, le=10, description="Humør fra 1 til 10")
    shower_type: str = Field(..., description="Normalt bad, koldt bad eller intet bad")