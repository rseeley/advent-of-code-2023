from src.app.day_1_1 import get_total


def test_get_total() -> None:
    assert (
        get_total(
            [
                "1abc2",
                "pqr3stu8vwx",
                "a1b2c3d4e5f",
                "treb7uchet",
            ]
        )
        == 142
    )
