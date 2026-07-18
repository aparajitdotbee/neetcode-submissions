from typing import Dict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        elem_freq_mapper: Dict[int, int] = {}
        for num in nums:
            if num in elem_freq_mapper:
                return True
            else:
                elem_freq_mapper[num] = 1

        return False
        