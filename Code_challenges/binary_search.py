list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

seven = 7

eleven = 11


def binary_search(lst: list, num: int):
    """
    A function to search for a specified
    numbers index inside a given list
    :param lst:
    :param num:
    :return:
    """
    left = 0
    right = len(lst) - 1

    while left <= right:
        mid = (left + right) // 2

        if lst[mid] == num:
            return mid
        elif lst[mid] < num:
            left = mid + 1
        else:
            right = mid - 1

    return str("Number not present in string.")


print(binary_search(list1, seven))
print(binary_search(list1, eleven))
