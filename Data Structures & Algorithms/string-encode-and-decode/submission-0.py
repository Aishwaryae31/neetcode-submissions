class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i

            # Find the '#'
            while s[j] != "#":
                j += 1

            # Get length of the string
            length = int(s[i:j])

            # Move past '#'
            i = j + 1

            # Take exactly 'length' characters
            res.append(s[i:i + length])

            # Move to next encoded string
            i += length

        return res
