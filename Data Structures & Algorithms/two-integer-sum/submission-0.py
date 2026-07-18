class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Map to store values and their indices from the array
        values_indices_map: Dict[int, int] = {}

        for idx in range(len(nums)):
            # Check if the value exists in the map
            # If not, store the difference of the target and the value in the map with the current index
            # if the value exists, return the index of the difference and the current index
            if nums[idx] in values_indices_map:
                return [values_indices_map[nums[idx]], idx]
            else:
                values_indices_map[target - nums[idx]] = idx

        return []