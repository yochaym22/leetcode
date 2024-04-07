#https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1, p2 = m - 1, n - 1
        p = m + n - 1
        # Merge nums1 and nums2 from the end
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        if p2 >= 0:
            nums1[:p2 + 1] = nums2[:p2 + 1]


s = Solution()
nums1 = [1,2,6,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
s.merge(nums1, m, nums2, n)