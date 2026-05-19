from pydantic import BaseModel, Field


class RoutineEntry(BaseModel):
    """
    Datamodel for én morgenrutine.
    """

    date: str = Field(..., description="Dato")
    wake_up_time: str = Field(..., description="Tidspunkt brugeren stod op")
    sleep_hours: float = Field(..., ge=0, le=24)

    training: bool = Field(..., description="Træning ja/nej")
    shower_type: str = Field(..., description="Bad-type")
    breakfast: bool = Field(..., description="Morgenmad ja/nej")
    water_glasses: int = Field(..., ge=0, le=30)

    task_1: str = Field(..., description="Vigtig opgave 1")
    task_2: str = Field(..., description="Vigtig opgave 2")
    task_3: str = Field(..., description="Vigtig opgave 3")

    mood: int = Field(..., ge=1, le=10)
    thoughts: str = Field(..., description="Tanker og følelser")