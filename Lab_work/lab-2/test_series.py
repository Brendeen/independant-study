
from series import fibonacci
from series import lucas


def test_fib_0():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected


def test_fib_1():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected


def test_fib_2():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected


def test_fib_5():
    actual = fibonacci(5)
    expected = 5
    assert actual == expected


def test_fib_7():
    actual = fibonacci(7)
    expected = 13
    assert actual == expected


def test_luc_0():
    actual = lucas(0)
    expected = 2
    assert actual == expected
