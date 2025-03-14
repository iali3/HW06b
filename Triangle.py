# -*- coding: utf-8 -*-
"""
Created on March 14, 2025
Updated March 14, 2025

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: Imran Al
@author: ia
"""

def classifyTriangle(a, b, c):
    """
    Classifies a triangle based on side lengths.
    """
    # Check if inputs are valid integers within range
    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return 'InvalidInput'
    if a <= 0 or b <= 0 or c <= 0 or a > 200 or b > 200 or c > 200:
        return 'InvalidInput'
    
    # Check for a valid triangle using the triangle inequality theorem
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return 'NotATriangle'
    
    # Check for equilateral triangle
    if a == b == c:
        return 'Equilateral'
    
    # Check for right triangle using the Pythagorean theorem
    if (a ** 2 + b ** 2 == c ** 2) or (a ** 2 + c ** 2 == b ** 2) or (b ** 2 + c ** 2 == a ** 2):
        return 'Right'
    
    # Check for isosceles triangle
    if a == b or b == c or a == c:
        return 'Isosceles'
    
    # If none of the above, it's a scalene triangle
    return 'Scalene'

