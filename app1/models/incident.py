from pydantic import BaseModel
from typing import Optional


class Incident(BaseModel):
    incident_id: str

    incident: str
    symptoms: str

    service: Optional[str] = None
    error: Optional[str] = None
    logs: Optional[str] = None

    root_cause: Optional[str] = None
    investigation: Optional[str] = None

    hypothesis: Optional[str] = None
    action: Optional[str] = None
    resolution: Optional[str] = None

    outcome: Optional[str] = None

    recommendation: Optional[str] = None
    recommendation_usefulness: Optional[str] = None

    failed_approach: Optional[str] = None
    successful_approach: Optional[str] = None

    lesson_learned: Optional[str] = None