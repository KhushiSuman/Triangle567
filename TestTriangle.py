import unittest
from Triangle import classifyTriangle

class TestTriangles(unittest.TestCase):

    # Test right triangles
    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', '5,3,4 is a Right triangle')

    # Test equilateral triangles
    def testEquilateralTriangles(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')

    # Test isosceles triangles
    def testIsoscelesTriangle(self):
        self.assertEqual(classifyTriangle(3, 3, 5), 'Isoceles', '3,3,5 should be isosceles')

    # Test scalene triangles
    def testScaleneTriangle(self):
        self.assertEqual(classifyTriangle(3, 4, 6), 'Scalene', '3,4,6 should be scalene')

    # Test invalid triangles
    def testInvalidTriangle(self):
        self.assertEqual(classifyTriangle(1, 1, 3), 'NotATriangle', '1,1,3 should not be a valid triangle')

    # Test for non-integer inputs
    def testInvalidInput(self):
        self.assertEqual(classifyTriangle('a', 1, 1), 'InvalidInput', 'Non-integer input should return InvalidInput')
        self.assertEqual(classifyTriangle(1.5, 2, 3), 'InvalidInput', 'Float input should return InvalidInput')

    # Test for negative or zero values
    def testZeroOrNegative(self):
        self.assertEqual(classifyTriangle(0, 1, 1), 'InvalidInput', 'Zero side length should return InvalidInput')
        self.assertEqual(classifyTriangle(-1, 1, 1), 'InvalidInput', 'Negative side length should return InvalidInput')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
