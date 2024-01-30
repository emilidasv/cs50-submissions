import pytest
from working import convert

def test_convert_at_begnningng_of_day():
    assert convert("12:00 AM to 12:59 AM") == "00:00 to 00:59"

def test_convert_endOif_day():
    assert convert("11:50 PM to 11:59 PM") == "23:50 to 23:59"

def test_convert_one_hournumber():
    assert convert("1:04 AM to 2:35 PM") == "01:04 to 14:35"

def test_convert_two_hournumber():
    assert convert("10:55 AM to 11:46 PM") == "10:55 to 23:46"

def test_convert_one_hournumber():
    assert convert("1 AM to 2 PM") == "01:00 to 14:00"

def test_convert_two_hournumber_Wo_min():
    assert convert("10 AM to 11 PM") == "10:00 to 23:00"

def test_convert_threehournumbers_begin():
    with pytest.raises(ValueError):
        convert("113:00 AM to 5:00AM")

def test_convert_60min_begin():
    with pytest.raises(ValueError):
        convert("10:60 AM to 11:05 PM")

def test_convert_60min_end():
    with pytest.raises(ValueError):
        convert("10:00 AM to 11:65 PM")
def test_convert_no_to():
    with pytest.raises(ValueError):
        convert("10:00 AM 11:65 PM")

