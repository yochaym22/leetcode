#https://leetcode.com/problems/valid-parentheses/description/
def valid_parentheses(in_str):
    parentheses_map = {']': '[', '}': '{', ')': '('}
    stack = []
    for char in in_str:
        if char in parentheses_map.values():
            stack.append(char)
        elif char in parentheses_map.keys():
            if parentheses_map[char] in stack:
                stack.pop()
            else:
                return False

    return True if len(stack) == 0 else False


print(valid_parentheses("([aasc()]b)"))
