'''
Write a Python program that accepts a sentence and calculate the number of
letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
'''

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
