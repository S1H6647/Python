# Write a program to print the following star pattern.
'''
***
* *
***
n = 3
'''
n = 3
for i in range(1,n+1):
    if (i==1 or i==3):
      print("*"*3, end="")
    else:
      print("*", end="") 
      print(" ", end="") 
      print("*", end="") 
    print("")