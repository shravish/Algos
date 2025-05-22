class Codec:
    def encode(self, strs: list[str]) -> str:
        """Encodes a list of strings to a single string."""
        return ''.join(f'{len(s)}/{s}' for s in strs)

    def decode(self, s: str) -> list[str]:
        """Decodes a single string to a list of strings."""
        res = []
        i = 0
        while i < len(s):
            slash = s.find('/', i)
            length = int(s[i:slash])
            i = slash + 1
            res.append(s[i:i + length])
            i += length
        return res

codec = Codec()
original = ["hello", "world", "leetcode"]
encoded = codec.encode(original)
print("Encoded:", encoded)
# output: Encoded: 5/hello5/world8/leetcode

# Use encoded here not original
decoded = codec.decode(encoded)
print("Decoded:", decoded)
#output: Decoded: ['hello', 'world', 'leetcode']

