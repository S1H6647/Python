# Find the greatest among 4 numbers entered by the user
Numbers = []

i = 0
while i<4:
    enteredNum = int(input("Enter 4 numbers: "))
    Numbers.append(enteredNum)
    i += 1

j = 0
if Numbers[j] > Numbers[j+1] and Numbers[j+2] and Numbers[j+3]:
    print("First number is the greatest: ", Numbers[j])
elif Numbers[j+1] > Numbers[j+2] and Numbers[j+3]:
    print("Second number is the greatest: ", Numbers[j+1])
elif Numbers[j+2] > Numbers[j+3]:
    print("Third number is the greatest: ", Numbers[j+2])
else: 
    print("Fourth number is the greatest: ", Numbers[j+3])
    
