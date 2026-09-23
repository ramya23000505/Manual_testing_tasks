a = input()
letter =0
digit=0
for ch in a:
    if ch.isalpha():
        letter+=1
    else:
        digit +=1    

print("LETTERS " + str(letter))
print("DIGITS " + str(digit))