arr = [-4,3,-9,0,4,1]
pos = []
neg = []
zer = []
for i in arr:
    if i >0:
        pos.append(i)
    elif i<0:
        neg.append(i)
    else:
        zer.append(i)
pos_r = len(pos)/len(arr)
neg_r = len(neg)/len(arr)
zero_r = len(zer)/len(arr)
print(pos_r,neg_r,zero_r)