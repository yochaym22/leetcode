#https://leetcode.com/problems/majority-element/description/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    """
    n = length of input array
    m = count of unique numbers
    hash map solution time: o(n), space o(m),
    """
    # def majorityElement(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     target = n // 2 if n % 2 == 0 else n // 2 + 1
    #     map = {}
    #     for num in nums:
    #         if num in map:
    #             map[num] += 1
    #         else:
    #             map[num] = 1
    #         if map[num] == target:
    #             return num

    """
    runtime: o(n), space: o(1)
    """

    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        element = 0

        for num in nums:
            if count == 0:
                element = num
                count = 1
            elif element == num:
                count += 1
            else:
                count -= 1

        return element


a = Solution()
print(a.majorityElement([2, 2, 2, 1, 1, 1]))
