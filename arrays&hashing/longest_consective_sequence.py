# Code for only length(Actually asking)
def longest_consecutive_sequence(nums):
    num_set = set(nums)
    longest = 0

    for num in num_set:
        if num - 1 not in num_set:  # start of a sequence
            current = num
            streak = 1

            while current + 1 in num_set:
                current += 1
                streak += 1

            if streak > longest:
                longest = streak

    return longest

nums = [100, 4, 200, 1, 3, 2]
length = longest_consecutive_sequence(nums)
print("Length:", length)
# Output: Length: 4

------------------------------------------------------------------------------------------------------------------------------------------------------

#code for length and sequence(more Extension)
def longest_consecutive_sequence(nums):
    num_set = set(nums)
    longest = 0
    longest_sequence = []

    for num in num_set:
        if num - 1 not in num_set:  # start of a sequence
            current = num
            streak = 1
            current_sequence = [current]

            while current + 1 in num_set:
                current += 1
                current_sequence.append(current)
                streak += 1

            if streak > longest:
                longest = streak
                longest_sequence = current_sequence

    return longest, longest_sequence

nums = [100, 4, 200, 1, 3, 2]
length, sequence = longest_consecutive_sequence(nums)
print("Length:", length)
print("Sequence:", sequence)
#Output: Length: 4
#        Sequence: [1, 2, 3, 4]



