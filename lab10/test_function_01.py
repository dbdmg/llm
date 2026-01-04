import pytest
from function_01 import racer_disqualified

def test_racer_disqualified_valid():
    assert not racer_disqualified([120, 110, 90], [100, 100, 100], 2, [20, 10])

def test_racer_disqualified_valid2() :
    assert racer_disqualified([160, 200, 90], [100, 100, 100], 4, [50, 60, 70, 10])

def test_racer_disqualified_invalid():
    with pytest.raises(ValueError):
        racer_disqualified([120, 110], [100, 100, 100], 2, [20, 10])