import pytest
from src.toolkit.converter import measures_convert


def test1():
    assert measures_convert(45, "Kg", "g") == "45000.0"


def test_error1():
    with pytest.raises(SystemExit) as test_data:
        measures_convert(34, "c", "g")
    assert test_data.value.code == 2
