from numb3rs import validate
import pytest

def test_validate_4_period_ok():
    assert validate("1.1.1.1") == True
def test_validate_less_4_period():
    assert validate("1.1.1") == False
def test_validate_more_4_period():
    assert validate("1.1.1.1.1") == False
def test_validate_275_1_2_2():
    assert validate("275.1.2.2") == False
def test_validate_255_256_1_2():
    assert validate("255.256.2.2") == False
def test_validate_255_255_256_2():
    assert validate("255.255.256.2") == False
def test_validate_255_256_255_256():
    assert validate("255.255.255.256") == False

