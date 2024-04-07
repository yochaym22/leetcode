# https://leetcode.com/problems/rotate-array/description/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        # nums[:] modifies the list in place!!!
        nums[:] = nums[-k:] + nums[:-k]


a = Solution()
nums = [1,2,3,4,5,6,7]
k = 3
a.rotate(nums, k)
print(nums)