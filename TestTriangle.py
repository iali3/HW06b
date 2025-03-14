# -*- coding: utf-8 -*-
"""
Updated March 14, 2025
The primary goal of this file is to demonstrate a simple unittest implementation

@author: Imran Ali
@author: ia
"""

import unittest
from Triangle import classifyTriangle

class TestTriangles(unittest.TestCase):
    # Test for invalid inputs
    def testInvalidInputs(self):
        self.assertEqual(classifyTriangle(-1, 2, 3), 'InvalidInput')
        self.assertEqual(classifyTriangle(201, 2, 3), 'InvalidInput')
        self.assertEqual(classifyTriangle("a", 2, 3), 'InvalidInput')

    # Test for non-triangle cases
    def testNotATriangle(self):
        self.assertEqual(classifyTriangle(1, 2, 3), 'NotATriangle')
        self.assertEqual(classifyTriangle(5, 1, 1), 'NotATriangle')
    
    # Test for equilateral triangles
    def testEquilateralTriangles(self):
        self.assertEqual(classifyTriangle(3, 3, 3), 'Equilateral')
        self.assertEqual(classifyTriangle(10, 10, 10), 'Equilateral')
    
    # Test for isosceles triangles
    def testIsoscelesTriangles(self):
        self.assertEqual(classifyTriangle(5, 5, 3), 'Isosceles')
        self.assertEqual(classifyTriangle(7, 7, 10), 'Isosceles')
    
    # Test for scalene triangles
    def testScaleneTriangles(self):
        self.assertEqual(classifyTriangle(4, 5, 6), 'Scalene')
        self.assertEqual(classifyTriangle(10, 15, 20), 'Scalene')
    
    # Test for right triangles
    def testRightTriangles(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right')
        self.assertEqual(classifyTriangle(5, 12, 13), 'Right')
        self.assertEqual(classifyTriangle(8, 15, 17), 'Right')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
