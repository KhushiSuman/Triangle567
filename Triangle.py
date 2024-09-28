def classifyTriangle(a, b, c):
    """Classify the triangle based on the sides."""
    
    # Check for valid input: All inputs must be integers before any other validation
    if not(isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return 'InvalidInput'
    
    # Check for valid input range
    if a <= 0 or b <= 0 or c <= 0 or a > 200 or b > 200 or c > 200:
        return 'InvalidInput'
    
    # Check for valid triangle
    if a + b <= c or a + c <= b or b + c <= a:
        return 'NotATriangle'
    
    # Check for equilateral
    if a == b == c:
        return 'Equilateral'
    
    # Check for right triangle using the Pythagorean theorem
    if (a ** 2 + b ** 2 == c ** 2) or (a ** 2 + c ** 2 == b ** 2) or (b ** 2 + c ** 2 == a ** 2):
        return 'Right'
    
    # Check for isosceles
    if a == b or b == c or a == c:
        return 'Isoceles'
    
    # If none of the above, it must be scalene
    return 'Scalene'
