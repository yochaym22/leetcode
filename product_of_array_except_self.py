# https://leetcode.com/problems/product-of-array-except-self/?envType=study-plan-v2&envId=top-interview-150
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        prod = 1
        for i in range(n):
            res[i] = prod
            prod *= nums[i]
        prod = 1
        for i in range(n - 1, -1, -1):
            res[i] *= prod
            prod *= nums[i]
        return res


a = Solution()
a.productExceptSelf([1, 2, 3, 4])
