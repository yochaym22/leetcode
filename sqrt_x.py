# https://leetcode.com/problems/sqrtx/description/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 1, x
        while left <= right:
            mid = (left+right)//2
            if mid*mid == x:
                return mid
            if mid*mid > x:
                right = mid-1
            else:
                left = mid+1
        return right


a = Solution()
print(a.mySqrt(17))