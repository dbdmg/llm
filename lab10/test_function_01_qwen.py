import pytest
from function_01 import racer_disqualified

# Valid input cases
def test_valid_input_not_disqualified():
    assert racer_disqualified([10, 20, 30], [10, 20, 30], 0, []) == False

def test_valid_input_disqualified_by_time():
    assert racer_disqualified([20, 35, 50], [10, 20, 30], 0, []) == True

def test_valid_input_disqualified_by_single_large_penalty():
    assert racer_disqualified([10, 20, 30], [10, 20, 30], 1, [101]) == True

def test_valid_input_disqualified_by_total_penalties():
    assert racer_disqualified([10, 20, 30], [10, 20, 30], 3, [30, 40, 31]) == True

def test_valid_input_disqualified_by_number_of_penalties():
    assert racer_disqualified([10, 20, 30], [10, 20, 30], 6, [10, 10, 10, 10, 10, 10]) == True

# Invalid input cases
def test_invalid_times_not_list():
    with pytest.raises(ValueError):
        racer_disqualified("not a list", [10, 20, 30], 0, [])

def test_invalid_times_wrong_length():
    with pytest.raises(ValueError):
        racer_disqualified([10, 20], [10, 20, 30], 0, [])

def test_invalid_times_non_integer_elements():
    with pytest.raises(ValueError):
        racer_disqualified([10, "20", 30], [10, 20, 30], 0, [])

def test_invalid_winner_times_not_list():
    with pytest.raises(ValueError):
        racer_disqualified([10, 20, 30], "not a list", 0, [])

def test_invalid_winner_times_wrong_length():
    with pytest.raises(ValueError):
        racer_disqualified([10, 20, 30], [10, 20], 0, [])

def test_invalid_winner_times_non_integer_elements():
    with pytest.raises(ValueError):
        racer_disqualified([10, 20, 30], [10, "20", 30], 0, [])

def test_invalid_n_penalties_not_integer():
    with pytest.raises(ValueError):
        racer_disqualified([10, 20, 30], [10, 20, 30], "not an integer", [])

def test_invalid_penalties_not_list():
    with pytest.raises(ValueError):
        racer_disqualified([10, 20, 30], [10, 20, 30], 0, "not a list")

def test_invalid_penalties_non_integer_elements():
    with pytest.raises(ValueError):
        racer_disqualified([10, 20, 30], [10, 20, 30], 1, [10, "20"])

def test_invalid_penalties_length_mismatch():
    with pytest.raises(ValueError):
        racer_disqualified([10, 20, 30], [10, 20, 30], 2, [10])

# Edge cases
def test_edge_case_zero_penalties():
    assert racer_disqualified([10, 20, 30], [10, 20, 30], 0, []) == False

def test_edge_case_five_penalties_total_100():
    assert racer_disqualified([10, 20, 30], [10, 20, 30], 5, [20, 20, 20, 20, 20]) == False

def test_edge_case_five_penalties_total_101():
    assert racer_disqualified([10, 20, 30], [10, 20, 30], 5, [20, 20, 20, 20, 21]) == True

def test_edge_case_exactly_1_5_times_winner_time():
    assert racer_disqualified([15, 30, 45], [10, 20, 30], 0, []) == False

def test_edge_case_exceeding_1_5_times_winner_time():
    assert racer_disqualified([16, 31, 46], [10, 20, 30], 0, []) == True