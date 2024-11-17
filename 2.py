# Take a user’s age as input and display whether they are a minor, adult, or senior citizen.

# User_age input
User_age = int(input("Enter user age: "))

if User_age<18:
    print ("He/She is a minor.")
elif User_age<60:
    print ("He/She is a adult.")
else:
    print ("He/She is a Senior citizen.")
