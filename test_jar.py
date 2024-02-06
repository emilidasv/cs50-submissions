import pytest
from jar import Jar


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit_to_many():
    myjar = Jar()
    with pytest.raises(ValueError):
        myjar.deposit(13)

def test_depoist_more_than_capacity():
    myjar = Jar()
    with pytest.raises(ValueError):
        myjar.deposit(13)

def test_deposit_one_more_when_at_capacity():
    myjar = Jar()
    myjar.deposit(12)
    with pytest.raises(ValueError):
        myjar.deposit(1)

def test_depoit_end_up_at_capacity():
    myjar = Jar()
    myjar.deposit(12)
    assert str(myjar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_withdraw_one_more_than_capacity():
    myjar = Jar()
    myjar.deposit(12)
    with pytest.raises(ValueError):
        myjar.withdraw(13)

def test_deposit_and_witdraw():
    myjar = Jar()
    myjar.deposit(12)
    myjar.withdraw(2)
    assert myjar.size == 10
    myjar.withdraw(2)
    assert myjar.size == 8

def test_depostit_and_witdraw2():
    myjar = Jar()
    assert myjar.size== 0
    assert myjar.capacity == 12






