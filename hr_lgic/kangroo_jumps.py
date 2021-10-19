
x1,v1,x2,v2 = [0,2,5,3]

meet = False
while (True):
    if x1 == x2:
        meet = True
        break
    if (v1>v2 and x1>x1) or(v2>v1 and x2>x1) or(v2==v1 and x2!=x1):
        break
    x1+=v1
    x2+=v2

if meet:
    print("YES")
else:
    print("NO")