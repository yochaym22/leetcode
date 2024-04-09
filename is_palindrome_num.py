# https://leetcode.com/problems/palindrome-number/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        i, j = 0, len(s) - 1
        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

a = Solution()
print(a.isPalindrome(1221))