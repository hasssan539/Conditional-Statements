# Write a program to find the largest of three numbers.
num1=int(input("Please enter first number: "))
num2=int(input("Please enter second number: "))
num3=int(input("Please enter third number: "))

# code to which num is greatest

if num1 > num2 and num1 > num3:
        print("First number is the largest.")
elif num2 > num1 and num2 > num3:
        print("Second number is the largest.")
else:
    print("Third number is the largest.")
    