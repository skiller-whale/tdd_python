from src.wordle_app import WordleApp


def test_returns_empty_list_for_now() -> None:
    assert WordleApp().run(["_____", "FTH", "ISYCA"]) == []
