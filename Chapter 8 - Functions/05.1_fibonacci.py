# To print first 10 Fibonacci series

# By using recursion: 
def fibo(n):
    if (n <= 1):
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)
    
for n in range(10):
    print(fibo(n), end=" ")

print("\t")

# Increamenting values: 
def fibo(n):
    a, b = 0,1
    for i in range(n):
        print(a, end=" ")
        a,b = b, (a+b)

fibo(10)