
nums = [-1, 2, 5]

#a=3
for i in range(3, 5):
    nums.append((nums[i-3] + nums[i-2] + nums[i-1]/2))
    #a=a+1

print(nums)
