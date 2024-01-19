from fuel import convert, gauge
import pytest

def test_convert_ok_input():
    assert convert("1/3") == 33

def test_convert_char():
    with pytest.raises(ValueError):
        convert("cat/dog")

def test_convert_div_zero():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
def test_convert_low():
    assert convert("1/99") == 1

def test_convert_high():
    assert convert("99/100") == 99

def test_gauge_high():
    assert gauge(99) == 'F'
def test_gauge_low():
    assert gauge(1) == 'E'
def test_gauge_ok_input():
    assert gauge(33) == "33%"
