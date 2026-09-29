'''4.	Find the second largest element in a list'''
list1 = list(map(int, input("Enter numbers separated by space: ").split()))
largest=0
second=0
for i in list1:
    if i>largest:
        second=largest
        largest=i
    elif i>second and i!=largest:
        second=i
print("Second largest element is:", second)    
