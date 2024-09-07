list1 = [5, 7, 9, 3, 44, 7947, 1]


def reverse_list(lst):

    reverse = []
    for num in lst:
        reverse.insert(0, num)
        print(reverse)
    return reverse


reverse_list(list1)
