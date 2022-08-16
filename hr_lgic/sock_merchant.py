n = 7
ar = [1,2,1,2,1,3,2]


from collections import Counter
data = Counter(ar)

vals = list(dict(data).values())
a = 0
for i in vals:
    a+= (i//2)

print(a)
