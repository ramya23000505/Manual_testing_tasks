'''4.	Reverse a string without using built‑in reverse function'''

str = input("Enter a string: ")
rev = ""
for ch in str:
    rev = ch + rev
print("Reverse:", rev)