# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_needle, len_haystack = len(needle), len(haystack)
        if len_needle > len_haystack:
            return -1

        for i in range(len_haystack):
            if i + len_needle > len_haystack:
                return -1
            if haystack[i:i+len_needle] == needle:
                return i
        return -1


a = Solution()
a.strStr("mississippi", "a")