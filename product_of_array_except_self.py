def product_except_self(nums):
    n = len(nums)
    result = [1] * n

    # Calculate prefix product for each index
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    # Multiply with suffix product for each index
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result
nums = [1, 2, 3, 4]
print(product_except_self(nums))  
# Output: [24, 12, 8, 6]
