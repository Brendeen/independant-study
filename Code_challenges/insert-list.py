list1 = [1, 2, 4, 5]

list2 = [1, 2, 3, 5, 6]


def insert_middle(lst: list, num: int):

    length = len(lst)

    if length % 2 == 0:
        middle_index = length // 2
    else:
        middle_index = (length // 2) + 1

    lst.insert(middle_index, num)
    print(lst)

    return lst


insert_middle(list1, 3)
insert_middle(list2, 4)
