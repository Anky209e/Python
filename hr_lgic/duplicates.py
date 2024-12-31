# Given an integer array nums, return 
# true if any value appears more than once in the array, otherwise return false.

nums = [1,2,3,4,5,5]

def hasDuplicate(nums):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] == nums[j]:
                return True
    return False


print(hasDuplicate(nums))