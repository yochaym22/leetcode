# https://leetcode.com/problems/reverse-words-in-a-string/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    # o(n) memory
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        s = ''
        for i in range(len(words) - 1, -1, -1):
            if words[i] != '':
                s += f'{words[i]} '
        return s.strip()


a = Solution()
print(a.reverseWords("the sky is blue"))


