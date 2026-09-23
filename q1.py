a = input()
r=a.split(',')
print(r)

for num in r:
    if int(num, 2) % 5 == 0:
        print(num)