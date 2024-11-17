# Take three sides of a triangle as input and check if they form a valid triangle.

# Get input from user to get measurment of the triangle sides

first_side = int(input("Please enter first side measurment: "))
second_side = int(input("Please enter second side measurment: "))
third_side = int(input("Please enter third side measurment: "))

#code to check 
if first_side==second_side==third_side:
    print ("Yhis is a valid triangle")
else:
    print ("This is not a valid triangle")