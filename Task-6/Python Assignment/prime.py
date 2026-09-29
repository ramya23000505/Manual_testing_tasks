'''1.Print all prime numbers between input range (Ex – input 20 50, 
prints all prime numbers between 20 and 50).'''

start=int(input("Start: "))
end=int(input("End: "))

for i in range(start, end+1):
    if i<2:
        continue
    prime=True
    for j in range(2, int(i**0.5)+1):
        if i%j==0:
            prime=False
            break
    if prime:
        print(i , end=" ")