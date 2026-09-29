'''10.	Fibonacci series using recursion'''

n=int(input("Enter a number: "))
def fibo(n):         
    if n <= 1:
        return n
    return fibo(n-1) + fibo (n-2)
for i in range(n):
    print(fibo(i),end=" ")