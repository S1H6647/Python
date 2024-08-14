# Python | Program to accept the strings which contains all vowels

enteredString = input("Enter a string")
lowerString = enteredString.lower()

def is_all_vowels(enteredString):

    # set() function contverts words into individual characters
    vowels = "aeiou"
    set(vowels)

    s = set({})

    for characters in lowerString: # for each characters in the entered string

        if characters in vowels: # if characters of the entered string are are in the vowels
            s.add(characters) # add the characters to the set (s)


    if len(s) == len(lowerString): 
        return ("Accepted")
    else:
        return ("Not_accepted")

if __name__ == "__main__":
    print(is_all_vowels(enteredString))
    
    