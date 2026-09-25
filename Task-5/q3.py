'''3. Rainwater Collection System
A city installs buildings of different heights along a straight road. During rainfall, 
water gets collected between taller buildings. 
The engineering team needs to calculate the total amount of water that can remain trapped after heavy rainfall based on the heights of the buildings.
'''

def trap(height):
    left = 0
    right = len(height) - 1

    left_max = 0
    right_max = 0
    water = 0

    while left < right:

        if height[left] <= height[right]:

            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]

            left += 1

        else:

            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]

            right -= 1

    return water

height = list(map(int, input("Enter heights: ").split()))

print("Trapped water:", trap(height))