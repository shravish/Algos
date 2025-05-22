def two_sum(nums, target):
    index_map = {}  # stores number as key and its index as value
    for i, num in enumerate(nums):
        complement = target - num
        if complement in index_map:
            return [index_map[complement], i]
        index_map[num] = i
    return []

nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))  # Output: [0, 1]
