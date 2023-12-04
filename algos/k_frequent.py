nums = [1,1,1,2,2,3,]
k = 2
from collections import defaultdict
def topKFrequent(nums,k):
    counter = defaultdict(int)
    for number in nums:
        counter[number] += 1

    st = dict(sorted(counter.items(),key=lambda x:x[1],reverse=True)[:k])
    return list(st.keys())

print(topKFrequent(nums,k))