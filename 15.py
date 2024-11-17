# Write a program to check if a number is within a specified range.

# Request input from the user and convert it to an integer
num_input = int(input("Please enter a number to check if it is in the specified range (1000 to 5000): "))

# Check if num_input is within the range of 1000 to 5000
if 1000 <= num_input <= 5000:
    print("This is in range.")
else:
    print("This is not in range.")
