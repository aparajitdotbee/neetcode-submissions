from typing import Dict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len_t = len(t)

        s_char_mapper: Dict[str, int] = {}
        t_char_mapper: Dict[str, int] = {}

        if len(s) != len_t:
            return False

        for idx in range(len_t):
            if s[idx] not in s_char_mapper:
                s_char_mapper[s[idx]] = 1
            else:
                s_char_mapper[s[idx]] += 1

            if t[idx] not in t_char_mapper:
                t_char_mapper[t[idx]] = 1
            else:
                t_char_mapper[t[idx]] += 1

        return s_char_mapper == t_char_mapper
        