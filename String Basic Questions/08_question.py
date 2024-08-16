# Python program to capitalize the first and last character of each word in a string

def convert(input):
    words = input.split() 
    capitalized_words = [capitalize_first_last(word) for word in words]
    return ' '.join(capitalized_words)

def capitalize_first_last(word):
    if len(word) > 1:
        return word[0].upper() + word[1:-1] + word[-1].upper()
    return word.upper()

input= input("Enter a string: ")
output = convert(input) 
print(output)
