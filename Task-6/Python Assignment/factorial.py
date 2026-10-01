'''2.	Factorial using recursion'''
# for loop
'''
def factorial(n):
    fact=1
    for i in range(n):
        fact = fact * (i+1)
    return fact
n=int(input("Enter a number: "))
print(factorial(n))
'''
#recursion

def factorial_recursive(n):
    if n==0 or n==1:
        return 1
    return n* factorial_recursive(n-1)
n=int(input("Enter a number: "))    
print(factorial_recursive(n))