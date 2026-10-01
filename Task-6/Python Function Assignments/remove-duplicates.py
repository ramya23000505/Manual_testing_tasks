'''4.	Write a function remove_duplicates(lst) that returns a list containing only unique elements 
while preserving their original order.'''

def remove_duplicates(lst):
    result = []

    for item in lst:
        if item not in result:
            result.append(item)

    return result


numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print(remove_duplicates(numbers))