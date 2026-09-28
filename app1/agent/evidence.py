def separate_evidence(
    current_incident,
    historical_memories
):
    """
    Clearly separates:
    CURRENT EVIDENCE
    HISTORICAL EVIDENCE
    """

    current_evidence = {
        "incident": current_incident.incident,
        "symptoms": current_incident.symptoms,
        "service": current_incident.service,
        "error": current_incident.error,
        "logs": current_incident.logs
    }

    historical_evidence = []

    for memory in historical_memories:

        if hasattr(memory, "text"):
            historical_evidence.append(memory.text)
        else:
            historical_evidence.append(str(memory))

    return {
        "current_evidence": current_evidence,
        "historical_evidence": historical_evidence
    }