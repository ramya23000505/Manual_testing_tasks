'''5. Product Sales Analysis
A retail company stores the daily sales quantity of a product for several consecutive days.
Due to seasonal changes, some days may have negative adjustments.
The company wants to identify the period that produced the highest multiplication of sales-related values.
Develop a solution to determine this maximum product.
'''

def max_product(arr):
    current_max = arr[0]
    current_min = arr[0]
    maximum = arr[0]

    for i in range(1, len(arr)):
        x = arr[i]

        if x < 0:
            current_max, current_min = current_min, current_max

        current_max = max(x, current_max * x)
        current_min = min(x, current_min * x)

        maximum = max(maximum, current_max)

    return maximum


sales = list(map(int, input("Enter sales values: ").split()))
print("Maximum product:", max_product(sales))