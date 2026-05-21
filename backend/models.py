from pydantic import BaseModel, Field


# Datamodel for én morgenrutine.
# FastAPI bruger modellen til automatisk validering af data fra frontend.
class RoutineEntry(BaseModel):
   

    # Dato for registreringen.
    date: str = Field(..., description="Dato")

    # Tidspunkt hvor brugeren stod op.
    wake_up_time: str = Field(
        ...,
        description="Tidspunkt brugeren stod op",
    )

    # Antal timers søvn.
    # ge = greater than or equal.
    # le = less than or equal.
    # Brugeren må derfor kun indtaste værdier mellem 0 og 24.
    sleep_hours: float = Field(
        ...,
        ge=0,
        le=24,
    )

    # Boolean-felt som registrerer om brugeren har trænet.
    training: bool = Field(
        ...,
        description="Træning ja/nej",
    )

    # Type af bad brugeren har taget.
    shower_type: str = Field(
        ...,
        description="Bad-type",
    )

    # Boolean-felt som registrerer om brugeren har spist morgenmad.
    breakfast: bool = Field(
        ...,
        description="Morgenmad ja/nej",
    )

    # Antal glas vand brugeren har drukket.
    # Må kun være mellem 0 og 30.
    water_glasses: int = Field(
        ...,
        ge=0,
        le=30,
    )

    # Dagens vigtigste opgaver.
    # Bruges både til struktur og AI-feedback.
    task_1: str = Field(
        ...,
        description="Vigtig opgave 1",
    )

    task_2: str = Field(
        ...,
        description="Vigtig opgave 2",
    )

    task_3: str = Field(
        ...,
        description="Vigtig opgave 3",
    )

    # Humør registreres på en skala fra 1 til 10.
    mood: int = Field(
        ...,
        ge=1,
        le=10,
    )

    # Felt hvor brugeren kan skrive tanker og refleksioner.
    thoughts: str = Field(
        ...,
        description="Tanker og følelser",
    )