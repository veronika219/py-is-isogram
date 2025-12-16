import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        pytest.param("", True, id="empty string"),
        pytest.param("Hih", False, id="H and h are repeated letters"),
        pytest.param("book", False, id="small repeated letters"),
        pytest.param("BROOKS", False, id="large repeated letters"),
        pytest.param("Python ", True, id="unic letters + one space"),
        pytest.param("Unic phrase ", False, id="phrase with double spaces"),
    ]
)
def test_check_logic_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected


@pytest.mark.parametrize(
    "invalid_type",
    [ 1, 1.2, None, ["list"], (4, 5), {"a": 1}, True]
)
def test_check_type_argument(invalid_type: object) -> None:
    with pytest.raises(AttributeError):
        is_isogram(invalid_type)
