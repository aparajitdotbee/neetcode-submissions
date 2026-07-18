class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_group_mapper: Dict[str, List[str]] = {}

        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in anagram_group_mapper:
                anagram_group_mapper[sorted_word] = [word]
            else:
                anagram_group_mapper[sorted_word].append(word)

        return list(anagram_group_mapper.values())
        