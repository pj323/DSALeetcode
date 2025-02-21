"""
Square of side 'N'
Problem Description: You are given an integer n. Your task is to return a square pattern of size n x n made up of the character '*', represented as a list of strings.

Input Parameters:

n (int): The size of the square (number of rows and columns).

Output:

A list of strings where each string is a row of n characters.

Example:

Input: 3
Output: ['***', '***', '***']
 
Input: 5
Output: ['*****', '*****', '*****', '*****', '*****'
"""

def square_pattern(n):

    pattern = []
    for i in range(n):
        row = '*' * n
        pattern.append(row)
    
    return pattern


# Test the function with the given examples

print(square_pattern(3))
print(square_pattern(5))


"""
Hollow Square of side 'N'
Problem Description:

You are given an integer n. Your task is to return a hollow square pattern of size n x n made up of the character '*', represented as a list of strings. The hollow square has '*' on the border, and spaces ' ' in the middle (except for side lengths of 1 and 2).

Input Parameters:

n (int): The size of the square (number of rows and columns).


Output:

A list of strings where each string is a row of n characters, representing a hollow square.

Example:

Input: 3
Output: ['***', '* *', '***']
 
Input: 5
Output: ['*****', '*   *', '*   *', '*   *', '*****']
"""

def hollow_square_pattern(n):
    

    square = []
    if n == 1:
        return ['*']
    square.append('*' * n)  
    
    for i in range(n - 2):
        square.append('*' + ' ' * (n - 2) + '*')

    square.append('*' * n)  
    return square


print(hollow_square_pattern(3))
print(hollow_square_pattern(5))


"""
Rectangle Pattern
Problem Description:

You are given two integers, n and m. Your task is to return a rectangle pattern of '*', where n represents the number of rows (length) and m represents the number of columns (breadth).



Input:

Two integers n and m, where 1 <= n, m <= 100.



Output:

A list of strings where each string represents a row of the rectangle pattern.



Example:

Input: n = 4, m = 5
Output: ['*****', '*****', '*****', '*****']
 
Input: n = 3, m = 2
Output: ['**', '**', '**']


Disclaimer: This Udemy coding exercise is still in development, so some advanced complexities m
"""

def generate_rectangle(n, m):
    
    rectangle = []
    
    for i in range(n):
        row = "*" * m
        rectangle.append(row)
    return rectangle


print(generate_rectangle(4, 5))
print(generate_rectangle(3, 2))

"""
Right Angled Triangle
Problem Description:

You are given an integer n. Your task is to return a right-angled triangle pattern of '*' where each side has n characters, represented as a list of strings. The triangle has '*' characters, starting with 1 star in the first row, 2 stars in the second row, and so on until the last row has n stars.

Input Parameters:

n (int): The height and base of the right-angled triangle.

Output:

A list of strings where each string is a row of '*' characters that increases in length from 1 to n.

Example:

Input: 3
Output: ['*', '**', '***']
 
Input: 5
Output: ['*', '**', '***', '****', '*****']
"""

def generate_triangle(n):
    
    pattern = []
    
    for i in range(1, n+1):
        row = "*" * i
        pattern.append(row)
    return pattern


print(generate_triangle(3))



"""
Example:

Input: 3
Output: ['***', '**', '*']
 
Input: 5
Output: ['*****', '****', '***', '**', '*']
"""

def generate_inverted_triangle(n):
    
    triangle = []
    
    for i in range(n, 0, -1):
        
        triangle.append("*" * i)
        
    return triangle

print(generate_inverted_triangle(3))
