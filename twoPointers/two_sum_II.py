def two_sum_with_values_and_indices(nums, target):
    seen = {}
    for i, num in enumerate(nums):
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
