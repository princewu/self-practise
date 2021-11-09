# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 08:32:13 2021

@author: admin
"""

'''
367 有效的完全平方数
'''

# 方法1：暴力解法
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """

        i = 0
        while (i**2) <= num:
            if (i**2) == num:
                return True
            else:
                i += 1
        return False


# 方法2：二分法
# 时间复杂度： log(n)
# 空间复杂度： log(1)
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """

        if num < 2:
            return True

        left, right = 2, num//2  
        while left <= right:
            mid = left + (right - left) // 2
            target = mid * mid
            if num > target:
                left = mid + 1
            if num < target:
                right = mid -1
            if num == target:
                return True
        return False
    

# 方法3：牛顿迭代法
# 时间复杂度：O(logn)
# 空间复杂度：O(1)

# 牛顿迭代法的推导要会！！
# https://leetcode-cn.com/problems/valid-perfect-square/solution/you-xiao-de-wan-quan-ping-fang-shu-by-leetcode/

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """

        if num < 2:
            return True

        x = num // 2
        while x * x > num:
            x = (x + num // x) // 2
        return x * x == num