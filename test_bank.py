from bank import value

def test_value_start_with_hello():
    assert value("hello") == "$0"

def test_value_start_with_h():
    assert value("hi") == "$20"

def test_value_start_withsomething():
    assert value("What's happening") == "$100"
