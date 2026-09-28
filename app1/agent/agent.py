from app1.agent.evidence import separate_evidence
from app1.agent.reasoning import (
    analyze_possible_causes,
    build_reasoning
)
from app1.agent.recommendation import (
    generate_recommendation
)


class IncidentAgent:

    def __init__(self, memory_service):

        self.memory = memory_service

    def analyze_incident(self, incident):

        # --------------------------------
        # 1. RECALL HISTORICAL EXPERIENCE
        # --------------------------------

        query = (
            f"Previous incidents similar to: "
            f"{incident.incident}. "
            f"Symptoms: {incident.symptoms}. "
            f"Service: {incident.service}. "
            f"Error: {incident.error}"
        )

        historical_result = self.memory.recall(query)

        historical_memories = historical_result.results

        # --------------------------------
        # 2. SEPARATE EVIDENCE
        # --------------------------------

        evidence = separate_evidence(
            incident,
            historical_memories
        )

        # --------------------------------
        # 3. FIND POSSIBLE ROOT CAUSES
        # --------------------------------

        possible_root_causes = analyze_possible_causes(
            incident,
            historical_memories
        )

        # --------------------------------
        # 4. REASON
        # --------------------------------

        reasoning = build_reasoning(
            incident,
            historical_memories,
            possible_root_causes
        )

        # --------------------------------
        # 5. RECOMMEND
        # --------------------------------

        recommendations = generate_recommendation(
            incident,
            possible_root_causes
        )

        # --------------------------------
        # 6. CONFIDENCE
        # --------------------------------

        if len(historical_memories) >= 3:
            confidence = "medium"
        elif len(historical_memories) >= 1:
            confidence = "low"
        else:
            confidence = "very low"

        # --------------------------------
        # 7. UNCERTAINTY
        # --------------------------------

        uncertainty = (
            "Historical incidents are evidence for comparison, "
            "not proof that the current incident has the same root cause."
        )

        # --------------------------------
        # 8. RISK
        # --------------------------------

        risk = (
            "Taking corrective action without confirming the "
            "root cause may worsen the incident."
        )

        # --------------------------------
        # 9. NEXT STEPS
        # --------------------------------

        next_steps = [
            "Check current logs and metrics.",
            "Compare current symptoms with historical incidents.",
            "Validate the suspected root cause.",
            "Apply the recommended diagnostic checks.",
            "Record the actual outcome."
        ]

        return {
            "summary": (
                f"Analyzed incident {incident.incident_id}"
            ),

            "current_evidence":
                evidence["current_evidence"],

            "historical_evidence":
                evidence["historical_evidence"],

            "similar_incidents":
                len(historical_memories),

            "possible_root_causes":
                possible_root_causes,

            "recommendation":
                recommendations,

            "reasoning":
                reasoning,

            "confidence":
                confidence,

            "uncertainty":
                uncertainty,

            "risk":
                risk,

            "next_steps":
                next_steps
        }