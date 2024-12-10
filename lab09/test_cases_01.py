import pytest
import ipytest

from function_01 import compute_average


def test_valid_grades():
    grades = [18, 25, 30, 33, 22, 28]
    result = compute_average(grades)
    assert result == pytest.approx(26.25, rel=1e-2)

def test_valid_grades_with_30laude():
    grades = [20, 25, 30, 33, 29, 28]
    result = compute_average(grades)
    assert result == pytest.approx(27.75, rel=1e-2)

# Boundary test cases
def test_lowest_and_highest_valid_grades():
    grades = [18, 19, 20, 30, 33, 25]
    result = compute_average(grades)
    assert result == pytest.approx(23.5, rel=1e-2)

def test_all_30laude():
    grades = [33, 33, 33, 33, 33, 33]
    result = compute_average(grades)
    assert result == 33.0

# Invalid test cases
def test_more_than_six_grades():
    grades = [18, 25, 30, 33, 22, 28, 29]
    with pytest.raises(ValueError):
        compute_average(grades)

def test_less_than_six_grades():
    grades = [18, 25, 30, 33, 22]
    with pytest.raises(ValueError):
        compute_average(grades)

def test_invalid_grade_too_low():
    grades = [17, 25, 30, 33, 22, 28]
    with pytest.raises(ValueError):
        compute_average(grades)

def test_invalid_grade_too_high():
    grades = [18, 25, 30, 34, 22, 28]
    with pytest.raises(ValueError):
        compute_average(grades)

def test_all_grades_are_the_same():
    grades = [25, 25, 25, 25, 25, 25]
    result = compute_average(grades)
    assert result == 25.0

# Test cases with the lowest and highest grade removed
def test_all_grades_except_highest_and_lowest():
    grades = [18, 30, 28, 25, 22, 33]
    result = compute_average(grades)
    assert result == pytest.approx(26.25, rel=1e-2)

# Invalid test cases for non-numeric inputs
def test_non_numeric_input_string():
    grades = ["a", 25, 30, 33, 22, 28]
    with pytest.raises(ValueError):
        compute_average(grades)

def test_non_numeric_input_none():
    grades = [None, 25, 30, 33, 22, 28]
    with pytest.raises(ValueError):
        compute_average(grades)

def test_non_numeric_input_boolean():
    grades = [True, 25, 30, 33, 22, 28]
    with pytest.raises(ValueError):
        compute_average(grades)

def test_non_numeric_input_mixed():
    grades = [18, "25", 30, 33, 22, 28]
    with pytest.raises(ValueError):
        compute_average(grades)