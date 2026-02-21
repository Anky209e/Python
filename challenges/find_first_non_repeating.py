def first_non_repeating_char(string):
    my_dict = {}
    for c in string:
        my_dict[c] = my_dict.get(c, 0) + 1

    for k, v in my_dict.items():
        if v == 1:
            return k

    return None


string = "leetcode"
print(first_non_repeating_char(string))
