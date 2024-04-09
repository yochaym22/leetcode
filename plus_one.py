# https://leetcode.com/problems/palindrome-number/?envType=study-plan-v2&envId=top-interview-150
from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        add_counter = 0
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
                add_counter += 1
            else:
                digits[i] += 1
                break

        if add_counter == len(digits):
            digits[:] = [1] + [0] * add_counter

        return digits


a = Solution()
arr = [9,9,9,9]
a.plusOne(arr)
print(arr)