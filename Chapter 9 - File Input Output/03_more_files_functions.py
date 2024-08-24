# f.readline() function to read one full line at a time
# f.readlines() function to show the text in a list format 

f = open("myfile.txt","r")
# read1 = f.readlines()
# print(read1)

# read3 = f.read()
# print(read3)

lines = f.readline()   
while (lines != ""):
    print(lines)
    lines = f.readline()


# print(type(read1)) # List
# print(type(read2)) # String
# print(type(read3)) # String

f.close()