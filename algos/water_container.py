height = [2,3,4,5,18,17,6]

def maxArea(height):
    
    area = 0
    left_pointer,right_pointer = 0,len(height) - 1

    while left_pointer < right_pointer:

        new_area = (right_pointer - left_pointer) * \
            min(height[left_pointer],height[right_pointer])
        
        area = max(area,new_area)
        
        if height[left_pointer] < height[right_pointer]:
            left_pointer += 1
        else:
            right_pointer -= 1

    return area
    
print(maxArea(height))
