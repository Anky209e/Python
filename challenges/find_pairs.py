arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7


def find_pairs(arr1, arr2, target):
    pairs = []
    set1 = set(arr1)
    for num in arr2:
        complement = target - num
        if complement in set1:
            pairs.append((complement, num))
    return pairs


print(find_pairs(arr1=arr1, arr2=arr2, target=target))
