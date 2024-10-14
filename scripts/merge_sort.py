import random

# 1. Split array in two recursivily till there's only one number
# 2. Once there is only one number, merge the lists comparing the lists as stacks to build a new array sorted
def mergesort(arr: list[int], start=0, end=None) -> list[int]:
    if end == None:
        end = len(arr)
    if (end - start > 1):
        mid = (end + start) // 2
        mergesort(arr, start, mid)
        mergesort(arr, mid, end)
        merge(arr, start, mid, end)


def merge(arr: list[int], start: int, mid: int, end: int):
    left = arr[start:mid]
    right = arr[mid:end]

    top_left, top_right = 0, 0
    for k in range(start, end):
        # Check if any list has already reached it's end
        if top_left == len(left):
            arr[k] = right[top_right]
            top_right += 1
        elif top_right == len(right):
            arr[k] = left[top_left]
            top_left += 1
        # Compare the top of left w top right
        elif left[top_left] <= right[top_right]:
            arr[k] = left[top_left]
            top_left += 1
        else :
            arr[k] = right[top_right]
            top_right += 1


rand_numbers = random.sample(range(1, 1000), 30)

print("Before merge sort:")
print(rand_numbers)
mergesort(rand_numbers)
print("Sorted:")
print(rand_numbers)
