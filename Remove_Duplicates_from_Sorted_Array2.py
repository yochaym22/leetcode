#https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        index = 1
        counter = 1
        allowed_seq = 2

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                counter += 1
            else:
                counter = 1

            if counter <= allowed_seq:
                nums[index] = nums[i]
                index += 1

        return index


a = Solution()
nums = [0,0,1,1,1,1,2,3,3]
print(nums, a.removeDuplicates(nums))
