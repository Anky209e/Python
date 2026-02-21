def hash(string):
    my_hash = 0
    for c in string:
        my_hash = my_hash + ord(c)
    return my_hash


def group_anagrams(strings):
    my_dict = {}

    for string in strings:
        index = hash(string)
        if my_dict.get(index, None) is None:
            my_dict[index] = []
        my_dict[index].append(string)

    return list(my_dict.values())


group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
