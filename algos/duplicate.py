a = [1,2,3,5,5]
def containsDuplicate(nums):
    if len(a) == len(set(a)):
        return False
    return True

print(containsDuplicate(a))