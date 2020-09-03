import function
import math
import pytest

def test_add():
    assert function.add(1, 2) == 3

def test_add_2():
    assert function.add(2, 4) == 6

def test_add_3():
    assert function.add(3, 7) == 10

def test_add_4():
    assert function.add(10, 20) == 30