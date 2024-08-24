# A file contains a word "Donkey" multiple times. 
# You need to write a program which replace this word with ##### by updating the same file.

word = "Donkey"
replace = "######"

with open("A file.txt", "r") as f:
    data = f.read()
    print(data)
    
dataNew = data.replace(word, replace)

with open("A file.txt", "w") as f:
    f.write(dataNew)
    print(dataNew)