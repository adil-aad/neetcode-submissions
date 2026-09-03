class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = l = 0
        charSet = set()

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            res = max(res, r - l + 1)
            charSet.add(s[r])
            r += 1 
        return res