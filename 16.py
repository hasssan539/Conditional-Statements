# Take the length of three sides and classify the triangle (equilateral, isosceles, or scalene).

side1= int(input("Enter first side measurment: "))
side2= int(input("Enter second side measurment: "))
side3= int(input("Enter third side measurment: "))

# 3 sides equal then equilateral, 2 sides equal != third then isosceles, if 3 sides != to each other then scalene 
if side1==side2==side3:
    print ("This is a equilateral triangle.")
elif side1==side2 !=side3 or side2==side3 !=side1 or side1==side3 !=side2:
    print ("This is a isosceles triangle")
elif side1 != side2 !=side3 :
    print (" This is a scalene triangle")
else:
    print ("Enter valid input")