# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 19:13:45 2021

@author: admin
"""

'''
34. 在排序数组中查找元素的第一个和最后一个位置
'''

# 方法1
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def getLeftBoarder(nums, target):
            left, right = 0, len(nums) - 1
            leftBoarder = -2
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
                    leftBoarder = right 
            return leftBoarder

        def getRightBoarder(nums, target):
            left, right = 0, len(nums) - 1
            rightBoarder = -2
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] <= target:
                    left = mid + 1
                    rightBoarder = left
                else:
                    right = mid - 1
            return rightBoarder

        leftBoarder = getLeftBoarder(nums, target)
        rightBoarder = getRightBoarder(nums, target)

        if rightBoarder - leftBoarder > 1 and leftBoarder != -2 and rightBoarder != -2:
            return [leftBoarder + 1, rightBoarder -1]
        else:
            return [-1, -1]


# 方法2

# 1、首先，在 nums 数组中二分查找 target；
# 2、如果二分查找失败，则 binarySearch 返回 -1，表明 nums 中没有 target。此时，searchRange 直接返回 {-1, -1}；
# 3、如果二分查找成功，则 binarySearch 返回 nums 中值为 target 的一个下标。然后，通过左右滑动指针，来找到符合题意的区间
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def binarySearch(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
        
        index = binarySearch(nums, target)
        print(index)
        if index == -1:
            return [-1, -1]
        else:
            l, r = index, index
            while l -1 >= 0 and nums[l-1] == target:
                l -= 1
            while r +1 <= len(nums)-1 and nums[r+1] == target:
                r += 1
            return [l, r]
        

# 方法4

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 1、首先，在 nums 数组中二分查找得到第一个大于等于 target的下标leftBorder；
        # 2、在 nums 数组中二分查找得到第一个大于等于 target+1的下标， 减1则得到rightBorder；
        # 3、如果开始位置在数组的右边或者不存在target，则返回[-1, -1] 。否则返回[leftBorder, rightBorder]

        def binarySearch(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] >= target:
                    right = mid - 1
                else: left = mid +1
            return left

        leftBorder = binarySearch(nums,target)
        rightBorder = binarySearch(nums, target+1) - 1
        if leftBorder == len(nums) or nums[leftBorder] != target:
            return [-1,-1]
        
        return [leftBorder, rightBorder]
