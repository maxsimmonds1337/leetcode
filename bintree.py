import math, time

nums = [2,5]
target = 0


### keep track of the lowest and highest points
low = 0
high = len(nums)-1
guess = math.floor((low+high)/2)

while((low != high) & (high > low)):
    guess = math.floor((low+high)/2)

    # if the mid point is less than the target, take midpoint to high
    if(nums[guess] == target):
        break
    elif(nums[guess] < target):
        low = guess + 1
    elif(nums[guess] > target):
        high = guess - 1
    
guess = math.floor((low+high)/2)

if(nums[guess] == target):
    print(guess)
else:
    print(-1)