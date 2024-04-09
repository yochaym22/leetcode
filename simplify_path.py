# https://leetcode.com/problems/simplify-path/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        temp = path.split('/')

        for i in temp:
            if i != '.' and i != '' and i != '..':
                stack.append(i)  # add if it is directory

            elif i == '..':
                if stack:
                    stack.pop()

        return '/' + '/'.join(stack)

a = Solution()
print(a.simplifyPath("/../a/b/../c"))
