#!/usr/bin/python3
"""
function generates a pascal triangle
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle of size n.

    Args:
        n (int): The number of rows in the Pascal's triangle.

    Returns:
        list: A list of lists representing Pascal's triangle.

    If n is less than or equal to 0, an empty list is returned.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize the triangle with the first row [1]
    for i in range(1, n):
        row = [1]  # Each row starts with 1
        for j in range(1, i):
            # Calculate each element of the row
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)  # Each row ends with 1
        triangle.append(row)

    return triangle
