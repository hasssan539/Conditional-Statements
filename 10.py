# Write a program to determine if a given character is a vowel or consonant.

char_input = str(input("Please enter a charater to check if it is a vowel or consonant: "))

vowels = "a , e, i, o ,u, A, E, I, O, U"
if char_input in vowels:
    print ("This is a vowel")
else:
    print ("This is consonant")