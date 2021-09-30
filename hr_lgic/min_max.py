arr = [1,3,5,7,9]
max1 = 0
min1 = 0
for i in arr:
    max1 = (max1+i)
    min1 = min1+i
max1 = max1-max(arr)
min1 = min1-min(arr)
print(max1,min1)


        
