# Write a program to find out whether a file is identical & matches the content of another file.

with open("this.txt","r") as f:
    contents1 = f.read()

with open("this_copy.txt","r") as f:
    contents2 = f.read()

if (contents1 == contents2):
    print("'this.txt' matches the contents of 'this_copy.txt'")
else:
    print("Doesn't match the contents!")