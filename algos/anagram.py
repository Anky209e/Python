s = 'anagram'
t = 'nagadram'

from collections import defaultdict

# def isAnagram(s,t):
#     count = defaultdict(int)
#     for c in s:
#         count[c] += 1

#     for c in t:
#         count[c] -= 1
#     for c in count.values():
#         if c != 0:
#             return False
#     return True


def isAnagram(s,t):
    if len(s) != len(t):
        return False
    
    uniq_c = set(s)

    for i in uniq_c:
        if s.count(i) != t.count(i):
            return False

    return True


print(isAnagram(s,t))