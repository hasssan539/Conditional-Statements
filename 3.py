# Write a program that checks if a given year is a leap year.


year = int(input("Enter year to check: "))

# Code to check leap year
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("This is a leap year")
        else:
            print("This is not a leap year")
    else:
        print("This is a leap year")
else:
    print("This is not a leap year")
