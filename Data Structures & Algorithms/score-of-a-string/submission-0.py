from itertools import pairwise

class Solution:
    def scoreOfString(self, s: str) -> int:
        return sum(map(lambda pair_chars: abs(ord(pair_chars[1]) - ord(pair_chars[0])), pairwise(s)))
        