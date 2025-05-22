def is_anagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

print(is_anagram("listen", "silent"))  # Output: True
print(is_anagram("earth", "heart"))  # Output: True
print(is_anagram("hello", "world"))    # Output: False
