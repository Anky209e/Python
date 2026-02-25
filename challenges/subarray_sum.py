nums = [-1, 2, 3, -4, 5]
target = 0


def sub_array_sum(nums=nums, target=target):
    store = {0: -1}
    current_sum = 0
    for i, value in enumerate(nums):
        current_sum = current_sum + value
        if (current_sum - target) in store.keys():
            start_index = store[current_sum - target] + 1
            return [start_index, i]
        store[current_sum] = i
    return []


print(sub_array_sum())
