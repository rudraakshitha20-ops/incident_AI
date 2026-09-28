def test_learning_module_import():

    from app1.learning.learning import (
        record_outcome,
        learn_from_outcome
    )

    assert record_outcome is not None
    assert learn_from_outcome is not None