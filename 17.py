# Write a program that asks for an integer and checks if it’s divisible by 2, 3, or both.

num= int(input("Please enter a value to check it is divisible by 2, 3 or both: "))

if num % 2==0 and num % 3==0:
    print ("Number is divisible by both 2 and 3")
elif num % 2==0:
        print ("Number is divisible by 2")
elif num % 3==0:
        print ("Number is divisible by 3")
else :
    print ("Number not divisible by 2 and 3")