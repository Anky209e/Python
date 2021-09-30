arr = [1,2,3,4,5,6,7,8,9,0,2,8,3,0,1,5,2,8,3,0,3,6,4,8,2,4,9,7,8,5,3]
# Write a function rotate(ar[], d, n) that rotates arr[] of size n by d elements. 
def rotate(array,d):
    temp = []
    for i in range(d):
        temp.append(array[i])     
    for t in temp:
        array.append(t)
    for c in range(d):
        array.pop(0)
    
    return array

print(rotate(arr, 10))