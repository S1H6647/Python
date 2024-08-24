# append mode writes the text in a file without replacing the text already written in it.
# There's a "Hello World!" text in "file.txt"

text = "Hello World from append mode"
f = open("file.txt", "a")
appendWrite = f.write(text)
f.close()
