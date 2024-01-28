import pytest
from um import count()

def test_count_one_coma():
    assert convert("um, how do you do hummer") == 1
def test_count_con_qustion():
    assert convert("um? 'how do you do hummer") == 1




#def test_count_threehournumbers_wozerosbegin():
#    with pytest.raises(ValueError):
#        convert("100 AM to 11 PM")
