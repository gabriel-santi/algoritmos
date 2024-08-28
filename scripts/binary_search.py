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