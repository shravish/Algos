# this is two-pointer method
def two_sum(numbers, target):
    left, right = 0, len(numbers) - 1
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left + 1, right + 1]  # 1-based indices
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []
numbers = [2, 7, 11, 15]
target = 9
print(two_sum(numbers, target))  
# Output: [1, 2]

------------------------------------------------------------------------------------------------------

# this is arrays&hashing method
def two_sum_with_values_and_indices(nums, target):
    seen = {}
    # start is 1, bcoz 1-indexed
    for i, num in enumerate(nums, start = 1):
        complement = target - num
        if complement in seen:
            return {
                "indices": [seen[complement], i],
                "values": [complement, num]
            }
        seen[num] = i
    return {}
nums = [2, 7, 11, 15]
target = 9
result = two_sum_with_values_and_indices(nums, target)
print(result) 
# Output: {"indices": [0, 1], "values": [2, 7]}
print("Indices:", result["indices"])  
# Output: [0, 1]
print("Values:", result["values"])    
# Output: [2, 7]
