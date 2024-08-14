# While using function, a new string is created to return to follow the change.

name = "Sanjit"

# len(str) = prints length of string
print(len(name))

# str.endswith("..") = checks if the str ends with ..
print(name.endswith("i")) 

# str.startswith("..") = checks if the str starts with ..
print(name.startswith("S"))

print(name.capitalize()) # Capitalizes first word of str

[
    {
        "method": "str.lower()",
        "description": "Converts all characters in the string to lowercase.",
        "example": "text = 'Hello World'; print(text.lower())  # Output: 'hello world'"
    },
    {
        "method": "str.upper()",
        "description": "Converts all characters in the string to uppercase.",
        "example": "text = 'Hello World'; print(text.upper())  # Output: 'HELLO WORLD'"
    },
    {
        "method": "str.title()",
        "description": "Capitalizes the first letter of each word in the string.",
        "example": "text = 'hello world'; print(text.title())  # Output: 'Hello World'"
    },
    {
        "method": "str.capitalize()",
        "description": "Capitalizes the first letter of the string and makes all other characters lowercase.",
        "example": "text = 'hello world'; print(text.capitalize())  # Output: 'Hello world'"
    },
    {
        "method": "str.strip()",
        "description": "Removes leading and trailing whitespace from the string.",
        "example": "text = '   Hello World   '; print(text.strip())  # Output: 'Hello World'"
    },
    {
        "method": "str.lstrip()",
        "description": "Removes leading whitespace (or specified characters) from the string.",
        "example": "text = '   Hello World'; print(text.lstrip())  # Output: 'Hello World'"
    },
    {
        "method": "str.rstrip()",
        "description": "Removes trailing whitespace (or specified characters) from the string.",
        "example": "text = 'Hello World   '; print(text.rstrip())  # Output: 'Hello World'"
    },
    {
        "method": "str.replace(old, new)",
        "description": "Replaces occurrences of a substring with another substring.",
        "example": "text = 'Hello World'; print(text.replace('World', 'Python'))  # Output: 'Hello Python'"
    },
    {
        "method": "str.split(sep)",
        "description": "Splits the string into a list of substrings based on the delimiter `sep`.",
        "example": "text = 'Hello World'; print(text.split())  # Output: ['Hello', 'World']"
    },
    {
        "method": "str.join(iterable)",
        "description": "Joins elements of an iterable into a single string, separated by the string on which the method is called.",
        "example": "words = ['Hello', 'World']; print(' '.join(words))  # Output: 'Hello World'"
    },
    {
        "method": "str.find(sub)",
        "description": "Returns the lowest index where the substring `sub` is found, or `-1` if not found.",
        "example": "text = 'Hello World'; print(text.find('World'))  # Output: 6"
    },
    {
        "method": "str.rfind(sub)",
        "description": "Returns the highest index where the substring `sub` is found, or `-1` if not found.",
        "example": "text = 'Hello World World'; print(text.rfind('World'))  # Output: 12"
    },
    {
        "method": "str.startswith(prefix)",
        "description": "Checks if the string starts with the specified prefix.",
        "example": "text = 'Hello World'; print(text.startswith('Hello'))  # Output: True"
    },
    {
        "method": "str.endswith(suffix)",
        "description": "Checks if the string ends with the specified suffix.",
        "example": "text = 'Hello World'; print(text.endswith('World'))  # Output: True"
    },
    {
        "method": "str.isdigit()",
        "description": "Returns `True` if all characters in the string are digits.",
        "example": "text = '12345'; print(text.isdigit())  # Output: True"
    },
    {
        "method": "str.isalpha()",
        "description": "Returns `True` if all characters in the string are alphabetic.",
        "example": "text = 'Hello'; print(text.isalpha())  # Output: True"
    },
    {
        "method": "str.isnumeric()",
        "description": "Returns `True` if all characters in the string are numeric.",
        "example": "text = '1234'; print(text.isnumeric())  # Output: True"
    },
    {
        "method": "str.islower()",
        "description": "Returns `True` if all characters in the string are lowercase.",
        "example": "text = 'hello'; print(text.islower())  # Output: True"
    },
    {
        "method": "str.isupper()",
        "description": "Returns `True` if all characters in the string are uppercase.",
        "example": "text = 'HELLO'; print(text.isupper())  # Output: True"
    },
    {
        "method": "str.zfill(width)",
        "description": "Pads the string with zeros on the left, to make the string of length `width`.",
        "example": "text = '42'; print(text.zfill(5))  # Output: '00042'"
    }
]
