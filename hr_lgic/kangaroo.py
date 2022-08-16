x1 = 2
v1 = 1
x2 = 1
v2 = 2

if x1 == x2:
    print("YES")
if (v2>v1 and x2>x1):
    print("NO")
else:
    for i in range(0,10000):
        print(x1,x2)
        if x1 == x2:
            break
        x1+=v1
        x2+=v2
    
        