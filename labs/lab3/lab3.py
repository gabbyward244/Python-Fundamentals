# NAME FIXME
# DATE

def slope(x1, y1, x2, y2):
    pass

def intercept(x1, y1, x2, y2):
    pass

def test_slope():
    assert slope(5, 3, 4, 2) == 1.0
    assert slope(1, 2, 3, 2) == 0.0
    assert slope(1, 2, 3, 3) == 0.5
    assert slope(2, 4, 1, 2) == 2.0
    print('all test cases passed for slope()')

def test_intercept():
    assert intercept(1, 6, 3, 12) == 3.0
    assert intercept(6, 1, 1, 6) == 7.0
    assert intercept(4, 6, 12, 8) == 5.0
    print('all test cases passed for intercept()')

test_slope()
test_intercept()