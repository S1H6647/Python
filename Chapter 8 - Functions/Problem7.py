# Program to remove a given word from a list and strip it at the same time

def rem(list, word):
    for items in list:
        list.remove(word)
        return list

list = ["Ram", "read", "happen"]
print(list)
word = input("Enter the word you want to remove: ")
output = rem(list, word)
print(output)