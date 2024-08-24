# Progrma to read in which line "python" is present in problem 6.

with open("log.txt","r") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if("python" in line):
        print(f"Yes, python is present in line  no. {lineno}")
        break
    lineno += 1
    
else:
    print("NO, python is not present")

# print(lines)