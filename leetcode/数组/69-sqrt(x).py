# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 09:16:24 2021

@author: admin
"""

'''
69  sqrt(x)
'''


# 二分法  自己写的
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x <= 1:
            return x
        left, right = 2, x//2
        while left <= right:
            mid = left + (right - left) // 2
            print(mid)
            target = mid * mid
            if target == x:
                return mid
            elif x < target:
                right = mid -1
            else:
                left = mid +1
        return left-1
    

# 二分法 答案
class Solution:
    def mySqrt(self, x: int) -> int:
        l, r, ans = 0, x, -1
        while l <= r:
            mid = (l + r) // 2
            if mid * mid <= x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans


# 牛顿迭代法
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x <= 1:
            return x
        ans = x 
        while ans * ans > x :
            ans = int(0.5 * (ans + x//ans))
        return ans