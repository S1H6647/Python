# Python program to check if a string has at least one letter and one number

enteredString = input("Enter a string: ")
def check_string(enteredString):
    # Flag initalization
    has_letter = False
    has_digit = False

    # checking 
    for item in enteredString:
        if item.isalpha():
            has_letter = True
        elif item.isdigit():
            has_digit = True

    return has_letter and has_digit

print(check_string(enteredString))