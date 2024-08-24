# Repeat problem 4 for a list of such words to be censored.

words = ["Donkey","Bad","Guu"]

with open("A file.txt", "r") as f:
    data = f.read()
    print(data)

for word in words:
    data = data.replace(word, "#" * len(word))

with open("A file.txt", "w") as f:
    f.write(data)
    print(data)