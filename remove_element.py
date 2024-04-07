#https://leetcode.com/problems/remove-element/?envType=study-plan-v2&envId=top-interview-150
from typing import List
import math

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = 51
                count += 1
        return len(nums) - count


a = Solution()
nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
sol = a.removeElement(nums, val=2)
print(nums, sol)
