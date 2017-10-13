from main import inc

def test_sample():
    assert inc(3) == 4

def test_fail():
    assert inc(2) == 6
