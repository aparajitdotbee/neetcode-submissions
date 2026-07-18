import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        pattern = re.compile(r"[^A-Za-z0-9]")
        extracted_string = pattern.sub("", s)

        len_s = len(extracted_string)
        if len_s <= 1:
            return True

        start: int = 0
        end: int = len_s - 1

        while start <= end:
            case_insensitive_valid_char = extracted_string[start].lower() == extracted_string[end].lower()
            if not case_insensitive_valid_char:
                return False

            start += 1
            end -= 1

        return True