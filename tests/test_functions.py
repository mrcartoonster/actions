# -*- coding: utf-8 -*-
"""
Simple functions tested with pytests.
"""
from examples.arithmetic import add


def test_add():
    """
    Testing adding function.
    """
    answer = add(5, 5)
    assert answer == 10
