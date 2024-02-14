numlist = [1, 4, 5, 2, 9]
d = lambda x, y: x > y 
def find_max(nums, lfunction):
    max = nums[0]
    for i in nums:
        if lfunction(i, max) == True:
            max = i
    return max

print(find_max(numlist, d))
