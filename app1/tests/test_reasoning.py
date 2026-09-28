from app1.agent.reasoning import analyze_possible_causes


class FakeMemory:

    def __init__(self, text):
        self.text = text


def test_database_pool_detection():

    memories = [
        FakeMemory(
            "Database timeout caused by connection pool saturation."
        )
    ]

    causes = analyze_possible_causes(
        None,
        memories
    )

    assert "Database connection pool saturation" in causes