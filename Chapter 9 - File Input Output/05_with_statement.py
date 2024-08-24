# With statement:

f = open("file.txt", "r")
print(f.read())
f.close()

# The same can be written using the statement like this:

with open("file.txt") as f:
    print(f.read())

# You don't have to explicitly close the file