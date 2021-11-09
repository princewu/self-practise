# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 20:10:35 2021

@author: admin
"""

'''
35 搜索插入位置
'''

# 方法1：左右均闭区间
class Solution(object):
    def searchInsert(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                return middle
        return left
        # return right + 1


# 方法2：左闭右开
class Solution(object):
    def searchInsert(self, nums, target):
        left, right = 0, len(nums) 

        while left < right:
            middle = (left + right) // 2

            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle 
            else:
                return middle
        return left 