# Complexity: O(n²)

# 1. Run the list looking for the lowest value(if is sorting by lower)
# 2. Once find the lower, remove from the original arr and add to the sorted 
# 3. Do that for each element in the arr

def selection_sort(arr: list[int]) -> list[int]:
    sorted_list = []

    for _ in range(0, len(arr)):
        min = arr[0]
        min_idx = 0
        for j in range(0, len(arr)):
            e = arr[j]
            if(e < min):
                min = e
                min_idx = j
        sorted_list.append(arr.pop(min_idx))
    
    return sorted_list

print(selection_sort([2,7,3,5,8,4,1,6]))
print(selection_sort([5,3,6,2,10]))