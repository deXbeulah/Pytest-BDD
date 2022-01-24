"""
This module contains basic unit tests for math operations.
Their purpose is to show how to use the pytest framework by example.
"""

# -------------------------------------------------------------------
# imports
# -------------------------------------------------------------------

import pytest 


# -------------------------------------------------------------------
# A most basic test function
# -------------------------------------------------------------------

def test_one_plus_one():
    assert 1 + 1 == 2

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0

    assert 'division by zero' in str(e.value)