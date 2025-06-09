'''
Linear Search with Reporting All Occurrences:
    Write a Python function to search for a target element in an array and return all indices where the target is found. If the target is not found, return an empty list.
'''
def find_all_indices(arr, target):
    # Your code here
    indices = []
    for i in range(len(arr)):
        if arr[i] == target:
            indices.append(i)
    return indices  # Return the full list after loop finishes

sample_arr = [4, 2, 7, 4, 9, 4]
target = 4  

result = find_all_indices(sample_arr, target)
print(result)