import time as t
initial = t.time()
print(initial)


i = 0
while i <25:
    i = i+1
    t.sleep(1)
    print(i)
print(t.time()-initial)
localtime = t.asctime(t.localtime(t.time()))
print(localtime)

