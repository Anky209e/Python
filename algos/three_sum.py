nums = [-1,0,1,2,-1,-4]

"""
return all the triplets 
[nums[i], nums[j], nums[k]]
such that
i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
"""
# NOTE: we will use two pointer approach
def threeSum(nums):
    result_arr = []
    nums.sort()

    for index,current_el in enumerate(nums):
        if index > 0 and current_el == nums[index-1]:
            continue
        
        left_pointer,right_pointer = index+1,len(nums)-1

        while left_pointer < right_pointer:
            three_sum = current_el + nums[left_pointer] + nums[right_pointer]
            if three_sum > 0:
                right_pointer -= 1
            elif three_sum < 0:
                left_pointer += 1
            else:
                result_arr.append([current_el,nums[left_pointer],nums[right_pointer]])
                left_pointer += 1

                while nums[left_pointer] == nums[left_pointer -1 ] and left_pointer < right_pointer:
                    left_pointer += 1
    return result_arr

print(threeSum(nums))