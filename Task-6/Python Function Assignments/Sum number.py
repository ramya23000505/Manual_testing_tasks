'''2.	Write a function sum_numbers(*args) that accepts any number of arguments 
and returns their sum.'''
'''
def sum_numbers(nums):
    total = 0
    for num in nums:
        total += num
    return total
nums = list(map(int, input("Enter numbers separated by space: ").split()))
print("Sum:", sum_numbers(nums))
'''
#arguments method

def sum_numbers(args):
    total = 0
    for num in args:
        total += num
    return total
def get_number():
    num = list(map(int, input("Enter numbers separated by space: ").split()))
    return num
num=get_number()
result = sum_numbers(*num)
print("Result:", result)