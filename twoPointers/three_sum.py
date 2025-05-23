def three_sum(nums):
    # Sort the array to use the two-pointer technique
    nums.sort()
    result = []

    for i in range(len(nums) - 2):
        # Skip duplicates for the anchor element
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                result.append([nums[i], nums[left], nums[right]])

                # Skip duplicates for left pointer
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                # Skip duplicates for right pointer
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1
            elif total < 0:
                left += 1  # Increase the sum by moving left pointer to the right
            else:
                right -= 1  # Decrease the sum by moving right pointer to the left

    return result
nums = [-2, 0, 1, 1, 2]
print(three_sum(nums))
# Output: [[-2, 0, 2], [-2, 1, 1]]
