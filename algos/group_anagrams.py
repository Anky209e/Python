from collections import defaultdict

strs = ["eat","tea","tan","ate","nat","bat"]

def isAnagram(s,t):
    if len(s) != len(t):
        return False
    u_c = set(s)

    for c in u_c:
        if s.count(c) != t.count(c):
            return False
        
    return True
      
def groupAnagrams(strs):
    store = defaultdict(list)

    for word in strs:
        sorted_word_key = ''.join(sorted(word))
        store[sorted_word_key].append(word)
    return list(store.values())
groupAnagrams(strs)
