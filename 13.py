# Take two numbers and an operator (+, -, *, /) as input and perform the corresponding operation.

num1= int(input("Enter first number: "))
num2= int(input("Enter second number: "))

# operation guidence
oper= str(input("Select which operation do you want to perform (+, -, *, /): "))

if oper == "+":
    print ("The addition of numbers is=" , (num1+num2))
elif oper == "-":
    print ("The subtraction of these numbers is=" , (num1-num2))
elif oper== "*":
    print ("The multiplication of these numbers is=" , (num1*num2))
elif oper== "/":
    print ("The division of these numbers is=" , (num1/num2))
else:
    print ("invalid operation")