def contains_duplicate(nums):
    return len(nums) != len(set(nums))

# Example usage:
nums = [1, 2, 3, 4, 5]
print(contains_duplicate(nums))
#output:False

nums2 = [1, 2, 3, 2, 5]
print(contains_duplicate(nums2))
#output:True


