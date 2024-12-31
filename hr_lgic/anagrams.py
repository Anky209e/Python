"""
Given two strings s and t, return true 
if the two strings are anagrams of each other, otherwise return false.
An anagram is a string that contains the exact same characters as another string,
but the order of the characters can be different.
"""

s = "jar"
t = "par"

def isAnagram(s,t):
    if len(s) != len(t):
        return False
    
    sCount,tCount = {},{}

    for i in range(len(s)):
        sCount[s[i]] = 1 + sCount.get(s[i],0)
        tCount[t[i]] = 1 + tCount.get(t[i],0)
    
    return sCount == tCount

print(isAnagram(s,t))