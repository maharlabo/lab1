import pytest
from src.toolkit.calculator import expession_calculate


def test1():
    assert expession_calculate("26+12*8") == "122.0"

def test2():
    assert expession_calculate("(12+34*47)//54") == "29.0"

def test3():
    assert expession_calculate("(32/8+43)%11") == "3.0"

def test4():
    assert expession_calculate("(314//(213-86)+13)%73") == "15.0"

def test5():
    assert expession_calculate("(87-+----+-13)*-----(100-99)") == "-100.0"

def test6():
    assert expession_calculate("(0.78/2.34)*0.03") == "0.01"

def test_error1():
    with pytest.raises(SystemExit) as test_data:
        expession_calculate("")
    assert test_data.value.code == 2


def test_error2():
    with pytest.raises(SystemExit) as test_data:
        expession_calculate("2;2")
    assert test_data.value.code == 2


def test_error3():
    with pytest.raises(SystemExit) as test_data:
        expession_calculate("4*(69+5+)")
    assert test_data.value.code == 2


def test_error4():
    with pytest.raises(SystemExit) as test_data:
        expession_calculate("5**6")
    assert test_data.value.code == 2
