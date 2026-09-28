from app1.memory.hindsight_service import HindsightService


memory = HindsightService()

try:

    print("Testing Hindsight...")

    memory.retain(
        content="""
        Incident INC-001:
        Database timeout occurred in the payments service.
        Investigation found database connection pool saturation.
        Increasing the database connection pool resolved the incident.
        """,
        context="Production incident"
    )

    print("Memory stored successfully.")

    results = memory.recall(
        "What previous incidents involved database timeout?"
    )

    print("\nRecalled memories:")

    for result in results:
        print("--------------------")
        print(result.text)

except Exception as e:

    print("\nERROR:")
    print(e)

finally:

    memory.close()
    print("\nHindsight client closed.")