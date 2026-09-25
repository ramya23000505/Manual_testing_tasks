'''2. Online Shopping Price Analysis
An online shopping application stores the prices of products viewed by a customer during a browsing session. 
The customer wants to identify a continuous range of products that provides the maximum possible total discount value.
Given the discount values, determine the maximum value that can be obtained from any continuous range.
'''
def max_discount(discounts):
    current_sum=discounts[0]
    max_sum=discounts[0]

    for i in range(1,len(discounts)):
        current_sum = max(current_sum, discounts[i]+current_sum)
        max_sum = max(max_sum, current_sum)
    return max_sum

discounts= list(map(int, input().split()))
print("Maximum Discounts: ", max_discount(discounts))    


