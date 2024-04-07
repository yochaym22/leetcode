#https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/1226017742/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        unique_index = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[unique_index] = nums[i]
                unique_index += 1

        return unique_index

