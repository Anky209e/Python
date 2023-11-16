nums = [3,2,4]
target = 6

# O(n^2)
def two_sum(nums,target):
    len_nums = len(nums)
    for i in range(len_nums):
        for j in range(len_nums):
            if i != j and nums[i]+nums[j] == target:
                return [i,j]
            
def two_sum_hash(nums,target):
    storeMap = {}
    for index,el in enumerate(nums):
        complement = target - el
        if complement in storeMap:
            return [storeMap[complement],index]
        storeMap[el] = index
    return None

            
print(two_sum_hash(nums,target))