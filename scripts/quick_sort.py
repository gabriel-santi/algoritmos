# Complexity: O(n²) - worst case | O(n log n) - best case

"""
Logic: Divide to conquer. Select a random number in array as pivot create two subarrays based on pivot, 
one keeps the elements lower than pivot, other keep elements higher than pivot. Join the left array with the pivot and rigth,
applying the same orderer logic recursively for both arrays until there's only one or none element. 
"""

def quick_sort(arr: list[int]) -> list[int]:
    if(len(arr) < 2):
        return arr
    
    mid = len(arr)//2
    pivot = arr[mid]
    left = []
    right = []
    for i in range(0, len(arr)):
        if i == mid:
            continue

        e = arr[i]
        if e > pivot:
            right.append(e)
        else:
            left.append(e)

    return quick_sort(left) + [pivot] + quick_sort(right)


my_arr = [1,5,7,3,2,9,4,6]
print(quick_sort(my_arr))