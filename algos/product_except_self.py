
nums = [1,2,3,4]

def productExceptSelf(nums):
    nums_len = len(nums)
    result_store = [1] * nums_len
    prefix = 1
    postfix = 1

    for i in range(nums_len):
        # Calculating and storing prefix values
        result_store[i] = prefix
        prefix *= nums[i]
    
    for i in range(nums_len-1,-1,-1):
        # Multiplying postfix values to already stored prefixes
        result_store[i] *= postfix
        postfix *= nums[i]
    return result_store
    

print(productExceptSelf(nums))

