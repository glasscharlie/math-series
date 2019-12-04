from series import fibonacci, lucas, sum_series
# fibonacci tests
def test_one():
    expected = 0
    actual = fibonacci(1)
    assert actual == expected


def test_two():
    expected = 1
    actual = fibonacci(2)
    assert actual == expected

def test_three():
    expected = 1
    actual = fibonacci(3)
    assert actual == expected

def test_four():
    expected = 2
    actual = fibonacci(4)
    assert actual == expected

def test_five():
    expected = 3
    actual = fibonacci(5)
    assert actual == expected
    
def test_six():
    expected = 5
    actual = fibonacci(6)
    assert actual == expected

# lucas tests

def test_seven():
    expected = 2
    actual = lucas(1)
    assert actual == expected

def test_eight():
    expected = 1
    actual = lucas(2)
    assert actual == expected

def test_nine():
    expected = 3
    actual = lucas(3)
    assert actual == expected

def test_ten():
    expected = 4
    actual = lucas(4)
    assert actual == expected

def test_eleven():
    expected = 7
    actual = lucas(5)
    assert actual == expected
    
def test_twelve():
    expected = 11
    actual = lucas(6)
    assert actual == expected

#sum tests

def test_thirteen():
    expected = 0
    actual = sum_series(1)
    assert actual == expected

def test_fourteen():
    expected = 2
    actual = sum_series(1, 2, 3)
    assert actual == expected

def test_fifteen():
    expected = 3
    actual = sum_series(5)
    assert actual == expected

def test_fifteen():
    expected = 4
    actual = sum_series(3, 2, 2)
    assert actual == expected

def test_sixteen():
    expected = 18
    actual = sum_series(5, 3, 4)
    assert actual == expected

