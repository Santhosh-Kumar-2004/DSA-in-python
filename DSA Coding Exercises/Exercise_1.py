'''
Square of side 'N'
Problem Description: 
    You are given an integer n. Your task is to return a square pattern of size n x n made up of the character '*', represented as a list of strings.

Input Parameters:
    n (int): The size of the square (number of rows and columns).


Output:
    A list of strings where each string is a row of n characters.

Example:

Input: 3
Output: ['***', '***', '***']

Input: 5
Output: ['*****', '*****', '*****', '*****', '*****']
'''

def generate_square(n):
    if n <= 0:
        return n

    pattern = []
    row_string = '*' * n  # Create the string for a single row 

    for _ in range(n): 
        pattern.append(row_string)
    
    print(pattern)
    return pattern
        
user_input = int(input("Enter a number to generate square of it: "))    
generate_square(user_input)
