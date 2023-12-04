s = "A man, a plan, a canal: Panama"

def isPalindrome(s):
    s = s.strip().lower()
    left_pointer = 0
    right_pointer = len(s) - 1

    while left_pointer < right_pointer:
        if not s[left_pointer].isalnum():
            left_pointer += 1
            continue

        if not s[right_pointer].isalnum():
            right_pointer -= 1
            continue

        elif s[left_pointer] != s[right_pointer]:
            return False
        left_pointer += 1
        right_pointer -= 1
    return True

def isPalindromic_short(s):
    s = ''.join(filter(lambda c : c.isalnum(),s)).lower()
    return s == s[::-1]

print(isPalindrome(s))