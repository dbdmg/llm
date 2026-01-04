import pytest

from function_01 import racer_disqualified

# Test function to check if a racer is disqualified
def test_disqualified_based_on_penalties():
    # Valid input with disqualification due to excessive penalty (greater than 100)
    times = [100, 110, 120]
    winner_times = [80, 100, 110]
    n_penalties = 1
    penalties = [150]
    
    assert racer_disqualified(times, winner_times, n_penalties, penalties) == True

def test_disqualified_due_to_total_penalty():
    # Valid input with disqualification due to total penalties > 100
    times = [100, 110, 120]
    winner_times = [80, 100, 110]
    n_penalties = 3
    penalties = [50, 30, 40]
    
    assert racer_disqualified(times, winner_times, n_penalties, penalties) == True

def test_disqualified_due_to_excessive_number_of_penalties():
    # Valid input with disqualification due to too many penalties (more than 5)
    times = [100, 110, 120]
    winner_times = [80, 100, 110]
    n_penalties = 6
    penalties = [10, 10, 10, 10, 10, 10]
    
    assert racer_disqualified(times, winner_times, n_penalties, penalties) == True

def test_disqualified_due_to_exceeding_time_limit():
    # Valid input with disqualification due to a time exceeding 1.5 * winner time
    times = [120, 140, 160]
    winner_times = [80, 100, 110]
    n_penalties = 1
    penalties = [5]
    
    assert racer_disqualified(times, winner_times, n_penalties, penalties) == True

def test_not_disqualified_due_to_valid_input():
    # Valid input without any disqualification
    times = [80, 100, 110]
    winner_times = [80, 100, 110]
    n_penalties = 2
    penalties = [10, 15]
    
    assert racer_disqualified(times, winner_times, n_penalties, penalties) == False

# Invalid input test cases

def test_invalid_times_type():
    # Invalid input: 'times' is not a list of integers
    times = "100, 110, 120"
    winner_times = [80, 100, 110]
    n_penalties = 2
    penalties = [10, 15]
    
    with pytest.raises(ValueError):
        racer_disqualified(times, winner_times, n_penalties, penalties)

def test_invalid_winner_times_type():
    # Invalid input: 'winner_times' is not a list of integers
    times = [100, 110, 120]
    winner_times = "80, 100, 110"
    n_penalties = 2
    penalties = [10, 15]
    
    with pytest.raises(ValueError):
        racer_disqualified(times, winner_times, n_penalties, penalties)

def test_invalid_n_penalties_type():
    # Invalid input: 'n_penalties' is not an integer
    times = [100, 110, 120]
    winner_times = [80, 100, 110]
    n_penalties = "two"
    penalties = [10, 15]
    
    with pytest.raises(ValueError):
        racer_disqualified(times, winner_times, n_penalties, penalties)

def test_invalid_penalties_type():
    # Invalid input: 'penalties' is not a list of integers
    times = [100, 110, 120]
    winner_times = [80, 100, 110]
    n_penalties = 2
    penalties = "10, 15"
    
    with pytest.raises(ValueError):
        racer_disqualified(times, winner_times, n_penalties, penalties)

def test_mismatch_between_n_penalties_and_penalties_list():
    # Invalid input: The number of penalties does not match n_penalties
    times = [100, 110, 120]
    winner_times = [80, 100, 110]
    n_penalties = 3
    penalties = [10, 15]
    
    with pytest.raises(ValueError):
        racer_disqualified(times, winner_times, n_penalties, penalties)

# Edge cases

def test_edge_case_penalties_empty():
    # Edge case: Empty penalties list, no penalties
    times = [100, 110, 120]
    winner_times = [80, 100, 110]
    n_penalties = 0
    penalties = []
    
    assert racer_disqualified(times, winner_times, n_penalties, penalties) == False

def test_edge_case_no_time_exceeding():
    # Edge case: Times are exactly equal to winner times (no disqualification)
    times = [80, 100, 110]
    winner_times = [80, 100, 110]
    n_penalties = 0
    penalties = []
    
    assert racer_disqualified(times, winner_times, n_penalties, penalties) == False
