# Check if a year input by the user is a century year.

year= int(input("Enter a year to check it is a century year: "))

if year % 100==0:
    print ("It is a century year.")
else:
    print (" its not a century year.")