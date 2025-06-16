'''
✍️ Problem Statement:
Write a function to find the first occurrence of a target element in a sorted array. The array may contain duplicate elements. If the target is not found, return -1.
'''

def first_occurance_binary_search(arr, target):
    size = len(arr)

    start = 0
    end = size - 1

    while(start <= end):
        mid = (end + start) // 2

        if(arr[mid] == target):
            return mid 
        elif(arr[mid] > target):
            end = mid - 1
        elif(arr[mid] < target):
            start = mid + 1

    return -1


sample_array = [20, 40, 50, 30, 20, 100, 30, 70]
sorted_array = sorted(sample_array, reverse=True)
target = 30
print(sorted_array)

result = first_occurance_binary_search(sample_array, target)
print(result)