# factorial of given number using for loop 

num = int(input("Enter a number: ")) # 4

facto = 1
for i in range(1,num+1): # from 1 to 5 but calculates upto 4
    facto = i * facto # 1*1 >> 2*1 >> 3*2 >> 4*6 = 24

print(facto) # 24