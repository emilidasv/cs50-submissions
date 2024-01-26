import pytest
from working import convert

def test_convert_at_begnningng_of_day():
    assert convert("12:00 AM to 12:59 AM") == "00:00 to 00:59"

def test_convert_endOif_day():
    assert convert("11:50 PM to 11:59 PM") == "23:50 to 23:59"

def test_convert_one_hournumber():
    assert convert("1:04 AM to 2:35 PM") == "1:04 to 14:35"

def test_convert_two_hournumber():
    assert convert("10:55 AM to 11:46 PM") == "10:55 to 23:46"

def test_convert_one_hournumber():
    assert convert("1 AM to 2 PM") == "1 to 14"

def test_convert_two_hournumber_Wo_min():
    assert convert("10 AM to 11 PM") == "10 to 23"

#def test_convert_three_hournumber_begin():
    #assert convert("100 AM to 11 PM") == "None"

#def test_convert_three_hournumber_end():
    #assert convert("10 AM to 112 PM") == "None"

def test_convert_60min_begin():
    assert convert("10:60 AM to 11:05 PM") == "None"

def test_convert_60min_end():
    assert convert("10:00 AM to 11:65 PM") == "None"

#def test_convert_mix():
    #assert convert("10 AM to 11:35 PM") == "None"

