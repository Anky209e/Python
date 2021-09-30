arr = [[11,2,4],[4,5,6],[10,8,-12]]

d1 = 0
d2 = 0
for i in range(len(arr)):
    d1 = d1+arr[i][i]
    d2 = d2 + arr[i-1][-(i)]
print(d1-d2)