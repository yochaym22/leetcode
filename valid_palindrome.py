# https://leetcode.com/problems/valid-palindrome/description/?envType=study-plan-v2&envId=top-interview-150

# o(n) time complexity o(n) space complexity
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         chars = filter(lambda char: char.isalnum(), s)
#         chars = [char.lower() for char in chars]
#         i, j = 0, len(chars) - 1
#         while i <= j:
#             if chars[i] != chars[j]:
#                 return False
#             i, j = i + 1, j - 1
#
#         return True
#

# o(n) time complexity, o(n) space complexity
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        while i < j:
            if not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1
            elif s[i].lower() == s[j].lower() and s[i].isalnum() and s[j].isalnum():
                i += 1
                j -= 1
            else:
                return False
        return True


a = Solution()
print(a.isPalindrome('A man, a plan, a canal: Panama'))
