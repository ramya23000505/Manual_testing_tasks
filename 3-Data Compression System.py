'''22. Data Compression System
A communication system wants to reduce the size of repeated information before transmission.
When the same character appears continuously several times, 
it should be represented using the character and the number of repetitions.
Develop a solution that produces the compressed representation of the original data.
'''

def run_length_encode(s):
    result = ""
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result += s[i - 1] + str(count)
            count = 1

    if s:
        result += s[-1] + str(count)

    return result


s = input("Enter a string: ")
print("Encoded string:", run_length_encode(s))