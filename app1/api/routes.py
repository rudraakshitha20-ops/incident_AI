from fastapi import APIRouter

from app1.models.incident import Incident
from app1.memory.hindsight_service import HindsightService
from app1.agent.agent import IncidentAgent
from app1.learning.learning import learn_from_outcome


router = APIRouter()

memory_service = HindsightService()

agent = IncidentAgent(
    memory_service=memory_service
)


@router.get("/")
def home():

    return {
        "message": "Incident AI Agent is running"
    }


@router.post("/analyze")
def analyze_incident(incident: Incident):

    result = agent.analyze_incident(
        incident
    )

    return result


@router.post("/learn")
def learn_incident(
    incident: Incident,
    actual_root_cause: str,
    actual_resolution: str,
    outcome: str,
    analysis: dict
):

    result = learn_from_outcome(
        memory_service=memory_service,
        incident=incident,
        analysis=analysis,
        actual_root_cause=actual_root_cause,
        actual_resolution=actual_resolution,
        outcome=outcome
    )

    return {
        "message": "Outcome stored successfully",
        "result": str(result)
    }