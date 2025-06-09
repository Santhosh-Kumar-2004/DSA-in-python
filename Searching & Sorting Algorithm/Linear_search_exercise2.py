'''
Write a function in Python that takes an array and a target value, and returns a tuple of the first and last index where the target appears.
If the target is not found, return (-1, -1).
'''
#MY WRONG ANSWER
# def first_and_last_occurrence(arr, target):
#     # Your code here
#     indices = []
#     first_last = []
#     for index in range(0, len(arr)):
#         if arr[index] == target:
#             indices.append(index)
#             return indices
#     first_index = first_last.append(indices[0])
#     last_index = first_last.append(indices[-1])
#     return first_index, last_index

# sample_array = [1, 3, 7, 8, 7, 5, 7]
# target = 7  

# result = first_and_last_occurrence(sample_array, target)
# print(result)

#CORRECT ANSWER
def first_and_last_occurrence(arr, target):
    first = -1
    last = -1

    for i in range(len(arr)):
        if arr[i] == target:
            if first == -1:
                first = i
            last = i  # always update last when target is found

    return (first, last)

sample_array = [1, 3, 7, 8, 7, 5, 7]
target = 7  

result = first_and_last_occurrence(sample_array, target)
print(result)