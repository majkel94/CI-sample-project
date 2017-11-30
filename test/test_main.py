from .. import main

def test_sample():
    assert main.inc(3) == 4

def test_fail():
    assert main.inc(2) == 6
