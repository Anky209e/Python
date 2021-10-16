arr = [2,5,6,2,7,2,7,3,9,5,0,1,4,8,5,2,7,4,9,92]
in_num = int(input("Enter your number: "))
numbs = []
for i in range(len(arr)):
    if in_num == arr[i]:
        numbs.append(i)
if len(numbs)>0:
    print("These are the indexes where",in_num," is present",numbs)
else:
    print("There is no such elements.")