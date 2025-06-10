def characterReplacement(s: str, k: int) -> int:
    max_len = 0
    max_count = 0
    count = [0] * 26
    left = 0

    for right in range(len(s)):
        count[ord(s[right]) - ord('A')] += 1
        max_count = max(max_count, count[ord(s[right]) - ord('A')])

        # If more than k characters need to be replaced, shrink window
        while (right - left + 1) - max_count > k:
            count[ord(s[left]) - ord('A')] -= 1
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len

print(characterReplacement("AABABBA", 1))  # Output: 4
