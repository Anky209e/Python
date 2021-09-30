st = "({)}"
sum = 0
for c in st:
    if c == '{' or c== '[' or c == '(':
        sum+=1
    else:
        sum-=1
if sum == 0:
    print('Symmetrical')
else:
    print("non-symmetrical")
