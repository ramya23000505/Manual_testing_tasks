'''5.	Count frequency of characters in a string'''

str = input("Enter a string: ")
freq={}
for ch in str:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)