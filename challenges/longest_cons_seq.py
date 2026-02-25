def longest_consecutive_sequence(nums):
    num_set = set(nums)
    longest_seq = 0

    for num in nums:
        if num - 1 not in num_set:
            current_num = num
            current_seq = 1
            while current_num + 1 in num_set:
                current_num += 1
                current_seq += 1
            longest_seq = max(longest_seq, current_seq)
    return longest_seq


print(longest_consecutive_sequence([100, 4, 200, 1, 3, 2]))
