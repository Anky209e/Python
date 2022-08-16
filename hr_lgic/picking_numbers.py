from collections import Counter

a = [4, 6, 5, 3, 3, 1]

d  = Counter(a)
t = []
for i in range(0,101):
    a = d[i]+d[i+1]
    t.append(a)
print(max(t))

