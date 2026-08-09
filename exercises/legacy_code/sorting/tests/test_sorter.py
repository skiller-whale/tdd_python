from src.sorter import sort


def test_sorts_sequences_of_numbers_in_strings():
    assert sort(["Student Scores", "33", "10", "5", "50", "90"]) == [
        "Student Scores",
        "5",
        "10",
        "33",
        "50",
        "90",
    ]
