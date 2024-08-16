# Create an empty dictionary. 
# Allow 4 friends to enter their favorite language as value and use key as their names.
# Assume that the names are unique.

friends_name_language = {}

for friends in range(4):
    name = input("Enter your name: ")
    language = input("Enter your favorite language: ")
    friends_name_language[name] = language
    # friends_name_language.update(name, language) # Wrpng
    # Puts the language "value" into the name "key"

print(friends_name_language)

# Even though name and language are same it'll still return all the datas