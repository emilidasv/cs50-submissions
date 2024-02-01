import pytest
from seasons import calculate_minutes
from seasons import check_input


def test_count_one_year():
    assert calculate_minutes("2023-01-31", "2022-01-31") == 525600
def test_count_twoyear():
    assert calculate_minutes("2024-01-31", "2022-01-31" ) == 1051200

def test_invalid_month():
    with pytest.raises(SystemExit):
        check_input("2000-31-31")
