from plates import is_valid

def test_is_valid_SHorter_than_two():
    assert is_valid("A") == False

def test_is_valid_longer_than_siz():
    assert is_valid("AJJKKKL") == False

def test_is_valid_contains_min_two_char():
    assert is_valid("d12345") == False

def test_is_valid_only_num_end():
    assert is_valid("AJ2JS2") == False

def test_is_valid_start_with_twochar():
    assert is_valid("A12233") == False

def test_is_valid_ok():
    assert is_valid("AAA222") == True
def test_is_valid_first_number_zero():
    assert is_valid("AA0322") == False

def test_is_valid_onlyalfaandnum():
    assert is_valid("AA.233") == False





