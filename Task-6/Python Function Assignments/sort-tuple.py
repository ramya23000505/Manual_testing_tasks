'''5.	Using a lambda function, sort a list of tuples based on the second element. 
Example: [(1,5), (2,3), (4,1)].'''

def sort_tuples(numbers):
    numbers.sort(key=lambda x: x[1])
    return numbers


numbers = []

n = int(input("Enter number of tuples: "))

for i in range(n):
    a, b = map(int, input(f"Enter tuple {i + 1}: ").split())
    numbers.append((a, b))

print("Sorted list:", sort_tuples(numbers))