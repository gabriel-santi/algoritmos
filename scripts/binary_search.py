# Complexity: O(log n)

# Binary search only works if the list is sorted

def binary_search(list, item):
    start = 0
    end = len(list) - 1

    while start <= end:
        middle = (end + start) // 2
        current = list[middle]

        if current == item:
            return middle
        if current > item:
            end = middle - 1
        else:
            start = middle + 1

    return None

my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 9))


""" Leetcode medium
Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length)
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target,
return the index of target if it is in nums, or -1 if it is not in nums.
"""

def binary_search_pivot(nums, target):
        start = 0
        end = len(nums)-1

        while start <= end:
            middleIdx = (start+end)//2
            current = nums[middleIdx]

            if current == target:
                return middleIdx

            if  nums[start] <= current:
                if (nums[start] <= target <= current):
                    end = middleIdx - 1
                else:
                    start = middleIdx + 1
            else:
                if (nums[end] >= target > current):
                    start = middleIdx + 1
                else:
                    end = middleIdx - 1
        return -1


print(binary_search_pivot([1,3], 3))
print(binary_search_pivot([1,3,5], 1))
print(binary_search_pivot([4,5,6,7,8,1,2,3], 8))


"""
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
"""

def searchMatrix(matrix, target):
        startLine = 0
        endLine = len(matrix) - 1
        
        while startLine <= endLine:
            midLine = (startLine + endLine) // 2
            currentLine = matrix[midLine]

            if currentLine[0] <= target <= currentLine[-1]:
                return binary_search(currentLine, target)
            elif target > currentLine[-1]:
                startLine = midLine + 1
            else: 
                endLine = midLine - 1
        

def binary_search(row, target):
    start = 0
    end = len(row) - 1

    while start <= end:
        mid = (start+end) // 2
        midElement = row[mid]

        if target == midElement:
            return True
        elif target > midElement:
            start = mid + 1
        else:
            end = mid - 1
    
    return False

'''
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/?envType=problem-list-v2&envId=array

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
'''
# Binary search
class Solution(object):
    def searchRange(self, nums, target):
        def find_start(row, target):
            left = 0
            right = len(row) - 1
            first = -1

            while left <= right:
                mid = (left+right) // 2
                midElement = row[mid]

                if midElement < target:
                    left = mid + 1
                else:
                    if midElement == target:
                        first = mid
                    right = mid - 1
            
            return first

        def find_end(row, target):
            left = 0
            right = len(row) - 1
            last = -1

            while left <= right:
                mid = (left+right) // 2
                midElement = row[mid]

                if midElement > target:
                        right = mid - 1
                else:
                    if target == midElement:
                        last = mid
                    left = mid + 1
            
            return last

        return [find_start(nums, target), find_end(nums, target)]
        
s = Solution()
print(s.searchRange([5,7,7,8,8,8,8,10], 8))