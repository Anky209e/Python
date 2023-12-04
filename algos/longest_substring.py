string = "abcdabc"

def longest_substring(string):
    # Hashmap for storing seen characters
    seen_chars = {}
    # Pointers for sliding
    left_pointer = 0
    # Var containing max length
    max_length = 0

    # Iterating string once
    for right_pointer in range(len(string)):
        # Our current character
        current_char = string[right_pointer]
        
        # If current character is alreay seen and if its in anywhere between
        if current_char in seen_chars and seen_chars[current_char] >= left_pointer:
            # slide left pointer
            left_pointer = seen_chars[current_char] + 1
        else:
            # Getting max_length substring also including current pointers
            max_length = max(max_length,right_pointer-left_pointer+1)
        # Adding seen chars to map
        seen_chars[current_char] = right_pointer
    
    return max_length

print(longest_substring(string))