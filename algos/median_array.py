
nums1  = [1,2]
nums2 = [3,4]

def find_median_of_two(nums1,nums2):

    
    nums1.extend(nums2)
    nums1.sort()
    
    mid_arr = len(nums1) // 2
    if len(nums1) % 2 == 0:
        return (nums1[mid_arr - 1] + nums1[mid_arr]) / 2
    else:
        return nums1[mid_arr]


print(find_median_of_two(nums1,nums2))