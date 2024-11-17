# Write a program that takes a temperature in Celsius and checks if it’s freezing, moderate, or hot.

temp= int(input("Enter temperature in Celsius and checks its freezing, moderate, or hot: "))

# code to check

if temp<=0:
    print("Its freezing.")
elif temp<=35:
    print("Its moderate.")
else:
    print("Its hot.")