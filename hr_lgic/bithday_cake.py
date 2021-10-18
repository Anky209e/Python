arr = [5,4,5,1]
a = max(arr)
store = []
for i in range(0,len(arr)):
    if arr[i] == a:
        store.append(i)
print(store)
    