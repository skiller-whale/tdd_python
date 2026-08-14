import pytest


def test_compares_values_and_collections() -> None:
    values = [2, 4, 6]

    assert values[2] == 6
    assert values == [2, 4, 6]


def test_checks_containment_and_length() -> None:
    values = [2, 4, 6]

    assert 4 in values
    assert len(values) == 3


def test_checks_failures() -> None:
    with pytest.raises(ValueError):
        raise ValueError("bad input")
