marks = []

i = 0 
while i<=6:
    stdMarks = int(input("Enter marks: "))
    marks.append(stdMarks)
    i = i + 1

marks.sort()
print(marks)