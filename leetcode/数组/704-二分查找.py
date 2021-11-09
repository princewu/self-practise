# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 19:53:39 2021

@author: admin
"""

'''
704  二分查找

时间复杂度：  O(logn)

二分法前提：1.有序数列；2.无重复项

相关题目推荐
● 35.搜索插入位置(opens new window)
● 34.在排序数组中查找元素的第一个和最后一个位置
● 69.x 的平方根
● 367.有效的完全平方数
'''

# 版本1：左右区间均闭合
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) 
        while left < right:
            mid = (right + left)//2 
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
        return -1

    
# 版本2：左闭右开区间
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) 
        while left < right:
            mid = (right + left)//2 
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid
            elif target > nums[mid]:
                left = mid + 1
        return -1
