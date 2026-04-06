#Module 3 Tutorial - Binary Search
def binary_search(arr, k):
    low = 0
    high = len(arr) - 1
    result = -1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == k:
            result = mid
            high = mid - 1  
        elif arr[mid] < k:
            low = mid + 1
        else:
            high = mid - 1
    
    return result

print(binary_search([1, 2, 3, 4, 5], 4))
print(binary_search([11, 22, 33, 44, 55], 445))
print(binary_search([1, 1, 1, 1, 2], 1))