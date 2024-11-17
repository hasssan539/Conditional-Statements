# Create a program that evaluates if an inputted number is prime.

value= int(input("Please enter a value to check whether it is prime number or not: "))

if value % 2==0 or value %3==0 :
    print ("Its a prime number")
else: 
    print ("Its not a prime number")