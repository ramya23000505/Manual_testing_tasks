'''9. Network Packet Analysis
A network monitoring system receives packet identifiers in chronological order.
The system must determine the longest sequence of consecutive packets whose identifiers form a continuous numerical sequence,
regardless of their original order in the incoming data.
'''

def longest_consecutive(nums):
    numbers = set(nums)
    maximum = 0

    for num in numbers:

        # Start only if num is the beginning
        if num - 1 not in numbers:

            current = num
            length = 1

            while current + 1 in numbers:
                current += 1
                length += 1

            maximum = max(maximum, length)

    return maximum


packets = list(map(int, input().split()))

print(longest_consecutive(packets))