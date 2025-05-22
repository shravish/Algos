from collections import Counter
import heapq

def top_k_frequent(nums, k):
    # Count frequencies
    freq_map = Counter(nums)
    
    # Use a heap to get the k most common elements
    return [item for item, count in heapq.nlargest(k, freq_map.items(), key=lambda x: x[1])]

nums = [1, 1, 1, 2, 2, 3]
k = 2
print(top_k_frequent(nums, k))  # Output: [1, 2]
