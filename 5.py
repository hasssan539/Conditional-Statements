# Ask the user for a grade percentage and display the corresponding letter grade (A, B, C, D, F).

marks= int(input("Please enter marks of the student to checck the grade: "))

if marks>=80:
    print("This student got A grade.")
elif marks>=70:
    print("This student got B grade.")
elif marks>=60:
    print("This student got C grade.")
elif marks>=50:
    print("This student got D grade.")
else:
    print("This student got F grade")