# Check if a string input is uppercase, lowercase, or a mix.

value= str(input("Please enter to check it is in uppercase, lowercase, or a mix: "))

x=value.upper()
y=value.lower()

if value ==x:
    print ("Uppercase")
elif value ==y:
    print ("Lowercase")
else:
    print ("Mix case")