class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps = {}
        for word in strs:
            freq_map = [0] * 26
            for char in word:
                freq_map[ord(char) - ord('a')] += 1
            freq_map = tuple(freq_map)
            if freq_map in maps:
                maps[freq_map].append(word)
            else:
                maps[freq_map] = [word]

        result = []
        for key in maps:
            result.append(maps[key])

        return result

