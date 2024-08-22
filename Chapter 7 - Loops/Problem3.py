# Prime or not

def isPrime(num):
    for i in range(2,num):
        if num % i == 0:
            print("Not Prime number!")
            break
        else:
            print("Prime number!")
            break
    return None 
    
num = int(input("Enter any number: "))
isPrime(num)