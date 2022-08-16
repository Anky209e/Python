import random

arr = [1,1,2,2,3,4,5]

from collections import Counter

def migratoryBirds(arr):
    all = dict(Counter(arr))
    x = dict(all)
    # print(x)
    sort_by_value = dict(sorted(x.items(), key=lambda item: item[1],reverse=True))
    keys_values = list(sort_by_value.keys())
    # print(keys_values)
    max_value_of_highest_id = sort_by_value[keys_values[0]]
    temp = []
    for i in keys_values:
        if sort_by_value[i] == max_value_of_highest_id:
            temp.append(i)
    # print(min(temp))
    return min(temp)

        






migratoryBirds(arr)