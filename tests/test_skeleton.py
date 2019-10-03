# -*- coding: utf-8 -*-

import pytest
from netbox_site_diagram.skeleton import fib

__author__ = "David Maclagan"
__copyright__ = "David Maclagan"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
