import math
# Ask the user to enter the coordinates of the first point
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
# Ask the user to enter the coordinates of the second point
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Compute the distance using the distance formula
distance = math.sqrt(math.pow(x2 - x1, 2) + (math.pow(y2 - y1, 2)))
## Display the result
print("The distance between the two points is: ", distance)

"""
Using the library made it more practical as it provides built-in functions for mathematical operations, making the code more efficient 
to manipulate and run through. The built-in functions sqrt and pow were easier to use
as without them, I would have to manually carry out the calculations, which would have made the program longer and more complex.
The program would be more difficult without the functions sqrt() and pow() as manually, it would have made it more time-consuming
and prone to errors.
"""
