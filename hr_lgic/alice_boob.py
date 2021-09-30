a = [1,2,3,3,6,5]
b = [3,2,1,0,2,3]
ap = 0
bp = 0
for i in range(len(a)):
    if(a[i]>b[i]):
        ap+=1
    elif(b[i]>a[i]):
        bp+=1
    else:
        ap+=0
        bp+=0
arr = [ap,bp]
print(arr)