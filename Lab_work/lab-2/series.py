
# Python hints:
# In the function argument, you can specify what kind of argument you are looking for.
# For example, in fibonacci(), num is the argument name. Followed by : int.
# This is specifying what argument value the function is looking for. Improves readability


def fibonacci(num: int):
    """
    A function to return a desired value in the Fibonacci sequence.
    :param num:
    :return num:
    """
    if num == 0:
        return 0
    if num == 1:
        return 1
    return fibonacci(num - 1) + fibonacci(num - 2)


def lucas(num: int):
    """
    A function to return a desired value in the Lucas sequence.
    :param num:
    :return:
    """
    if num == 0:
        return 2
    if num == 1:
        return 1
    return lucas(num - 1) + lucas(num - 2)


if __name__ == '__main__':
    print(fibonacci(12))
    print(lucas(0))
