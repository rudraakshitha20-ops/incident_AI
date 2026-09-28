def record_outcome(
    memory_service,
    incident,
    analysis,
    actual_root_cause,
    actual_resolution,
    outcome
):

    recommendation_text = "\n".join(
        analysis.get("recommendation", [])
    )

    successful_approach = (
        actual_resolution
        if outcome.lower() == "resolved"
        else ""
    )

    failed_approach = ""

    if (
        actual_root_cause
        not in analysis.get("possible_root_causes", [])
    ):
        failed_approach = (
            "Initial historical hypothesis did not match "
            "the actual root cause."
        )

    lesson_learned = (
        f"Incident {incident.incident_id}: "
        f"actual root cause was {actual_root_cause}. "
        f"Outcome: {outcome}. "
        f"Future investigations should compare current "
        f"evidence against this outcome."
    )

    memory_content = f"""
Incident ID:
{incident.incident_id}

Incident:
{incident.incident}

Symptoms:
{incident.symptoms}

Service:
{incident.service}

Error:
{incident.error}

Logs:
{incident.logs}

Root Cause:
{actual_root_cause}

Investigation:
{incident.investigation}

Hypothesis:
{incident.hypothesis}

Action:
{incident.action}

Resolution:
{actual_resolution}

Outcome:
{outcome}

Recommendation:
{recommendation_text}

Recommendation Usefulness:
Not yet manually evaluated.

Failed Approach:
{failed_approach}

Successful Approach:
{successful_approach}

Lesson Learned:
{lesson_learned}
"""

    return memory_service.retain(
        content=memory_content,
        context="Incident outcome and learning",
        metadata={
            "incident_id": incident.incident_id,
            "actual_root_cause": actual_root_cause,
            "outcome": outcome
        }
    )


def learn_from_outcome(
    memory_service,
    incident,
    analysis,
    actual_root_cause,
    actual_resolution,
    outcome
):

    return record_outcome(
        memory_service=memory_service,
        incident=incident,
        analysis=analysis,
        actual_root_cause=actual_root_cause,
        actual_resolution=actual_resolution,
        outcome=outcome
    )