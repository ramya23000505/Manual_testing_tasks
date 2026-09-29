'''7.	Remove duplicates from a list'''
'''
list1 = list(map(int, input("Enter numbers separated by space: ").split()))
res = list(set(list1))
print("Unique numbers:", res)
'''
list1 = list(map(int, input("Enter numbers separated by space: ").split()))
res=[]
for i in list1:
    if i not in res:
        res.append(i)
print("Unique numbers:", res)