# https://leetcode.com/problems/valid-parentheses/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_map = {']': '[', '}': '{', ')': '('}
        stack = []
        for char in s:
            if char in parentheses_map.values():
                stack.append(char)
            elif char in parentheses_map.keys():
                if len(stack) > 0 and parentheses_map[char] == stack[len(stack) - 1]:
                    stack.pop()
                else:
                    return False

        return True if len(stack) == 0 else False


a = Solution()
print(a.isValid(']'))