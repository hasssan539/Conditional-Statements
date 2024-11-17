# Create a program that checks if a given string is a palindrome.

# Get user input
x = str(input("Enter a string to check it is a palindrome or not: "))
# To make all alphabets to lower case
x = x.lower()
# To remove spaces in string
x = x.replace(" ","")

# To check it is a palindrome or not
if x==x[ : : -1]:
    print ("This string is a palindrome")
else:
    print ("This string is not a palindrome")
