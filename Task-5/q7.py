'''7. Bank Transaction Analysis
A bank stores transaction amounts for a customer's account.
A continuous group of transactions may add up to a specific target amount. 
The auditing system needs to determine how many different continuous transaction groups produce exactly the specified amount.
'''

def subarray_sum(arr, target):
    prefix_sum = 0
    count = 0

    frequency = {0: 1}

    for num in arr:
        prefix_sum += num

        required = prefix_sum - target

        if required in frequency:
            count += frequency[required]

        frequency[prefix_sum] = frequency.get(prefix_sum, 0) + 1

    return count


transactions = list(map(int, input().split()))
target = int(input())

print(subarray_sum(transactions, target))