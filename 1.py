
# Write a program that checks if a given number is positive, negative, or zero.

# x assume to get input from user

x = int(input("Please enter a number to check if it is positive, negative, or zero: "))

# to check number is +,- or 0

if x>0:
    print ("Number is positive")
elif x<0:
    print ("Number is Negative")
else:
    print ("Number is zero")