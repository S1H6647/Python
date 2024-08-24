# Write a program to read the text from a given file 'poems.txt' and find out whether it contains the word 'twinkle'

with open("poems.txt") as f:
    contents = f.read()
    print(contents)
    if ("twinkle" in contents):
        print("'poems.txt' contains the word 'twinkle'")

    else:
        print("'poems.txt' doesn't contain the word 'twinkle'")