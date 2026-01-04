import pytest

# Import the function to be tested
from function_01 import racer_disqualified as your_function_name

def test_valid_inputs():
    # Valid input test case 1: No penalties, times within limits
    assert your_function_name([100, 200, 300], [90, 180, 270], 0, []) == False

    # Valid input test case 2: Some penalties, times within limits
    assert your_function_name([100, 200, 300], [90, 180, 270], 3, [10, 20, 30]) == False

    # Valid input test case 3: Penalties exceed limit, disqualified
    assert your_function_name([100, 200, 300], [90, 180, 270], 2, [101, 20]) == True

    # Valid input test case 4: Total penalties exceed limit, disqualified
    assert your_function_name([100, 200, 300], [90, 180, 270], 2, [51, 60]) == True

    # Valid input test case 5: Times exceed 1.5 times winner time, disqualified
    assert your_function_name([200, 200, 300], [90, 180, 270], 0, []) == True

def test_invalid_inputs():
    # Invalid input test case 1: Times is not a list
    with pytest.raises(ValueError):
        your_function_name("100, 200, 300", [90, 180, 270], 0, [])

    # Invalid input test case 2: Times does not have exactly three elements
    with pytest.raises(ValueError):
        your_function_name([100, 200], [90, 180, 270], 0, [])

    # Invalid input test case 3: Elements of times are not integers
    with pytest.raises(ValueError):
        your_function_name([100, "200", 300], [90, 180, 270], 0, [])

    # Invalid input test case 4: Winner times is not a list
    with pytest.raises(ValueError):
        your_function_name([100, 200, 300], "90, 180, 270", 0, [])

    # Invalid input test case 5: Winner times does not have exactly three elements
    with pytest.raises(ValueError):
        your_function_name([100, 200, 300], [90, 180], 0, [])

    # Invalid input test case 6: Elements of winner times are not integers
    with pytest.raises(ValueError):
        your_function_name([100, 200, 300], [90, "180", 270], 0, [])

    # Invalid input test case 7: n_penalties is not an integer
    with pytest.raises(ValueError):
        your_function_name([100, 200, 300], [90, 180, 270], "0", [])

    # Invalid input test case 8: Penalties is not a list
    with pytest.raises(ValueError):
        your_function_name([100, 200, 300], [90, 180, 270], 0, "10, 20")

    # Invalid input test case 9: Elements of penalties are not integers
    with pytest.raises(ValueError):
        your_function_name([100, 200, 300], [90, 180, 270], 1, ["10"])

    # Invalid input test case 10: n_penalties does not match the length of the penalties list
    with pytest.raises(ValueError):
        your_function_name([100, 200, 300], [90, 180, 270], 2, [10])

def test_edge_cases():
    # Edge case test: Maximum number of penalties, not disqualified
    assert your_function_name([100, 200, 300], [90, 180, 270], 5, [20, 20, 20, 20, 20]) == False

    # Edge case test: Single penalty exactly 100, not disqualified
    assert your_function_name([100, 200, 300], [90, 180, 270], 1, [100]) == False

    # Edge case test: Total penalties exactly 100, not disqualified
    assert your_function_name([100, 200, 300], [90, 180, 270], 2, [50, 50]) == False

    # Edge case test: Time exactly 1.5 times the winner time, not disqualified
    assert your_function_name([135, 270, 405], [90, 180, 270], 0, []) == False

pytest.main()
