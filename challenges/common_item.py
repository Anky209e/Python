list1 = [1, 2, 3]
list2 = [5, 6, 1]


def is_common(list1, list2):
    store_dict = {}
    for i in list1:
        store_dict[i] = True
    for j in list2:
        if j in store_dict:
            return True
    return False


print(is_common(list1, list2))
