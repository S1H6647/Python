# Used to store datas in a file
# Normal codes are stored in RAM 

f = open("file.txt","r") # read mode is default
data = f.read()
print(data)
f.close()

# This program reads the text written in "file.txt"