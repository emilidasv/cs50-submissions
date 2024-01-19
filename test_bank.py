from bank import value

def test_value_start_with_hello():
    assert value("hello") == 0
def test_value_start_with_hello_and_more():
    assert value("hello, David") ==  0

def test_value_start_with_caputalized_hello():
    assert value("HELLO") == 0

def test_value_start_with_caputalized_hello_andmmore():
    assert value("HELLO, David") == 0

def test_value_start_with_h():
    assert value("hi") == 20

def test_value_start_withsomething():
    assert value("What's happening") == 100
