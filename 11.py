# Check if a given number is a multiple of both 3 and 5.

number=int(input("Enter a number to check it is a multiple of both 3 and 5: "))

if number % 3 ==0:
    if number % 5==0:
        print("This is multiple of both 3 and 5.")
    else:
        print("This is not multiple of both 3 and 5.")
else:
    print("This is not multiple of both 3 and 5.")