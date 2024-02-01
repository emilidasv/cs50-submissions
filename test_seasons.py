import pytest
from seasons import calculate_minutes

def test_count_one_year():
    assert calculate_minutes("2023-01-31") == 525600
def test_count_twoyear():
    assert calculate_minutes("2022-01-31") == 1051200
def test_count_random():
    assert calculate_minutes("2024-01-02") == 1051200
