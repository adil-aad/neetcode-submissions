class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for st in strs:
            count = [0] * 26

            for c in st:
                count[ord(c) - ord('a')] += 1

            result[tuple(count)].append(st)

        return list(result.values())