from collections import defaultdict

def group_anagrams(words):
    anagram_groups = defaultdict(list)

    for word in words:
        sorted_word = ''.join(sorted(word))
        anagram_groups[sorted_word].append(word)

    return list(anagram_groups.values())

words = ["bat", "tab", "eat", "tea", "tan", "nat", "ate"]
print(group_anagrams(words))
# Output: [['bat', 'tab'], ['eat', 'tea', 'ate'], ['tan', 'nat']]
