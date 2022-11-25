# Problem Number : 221

def triangularSum( nums):
    n = len(nums)
    for i in range(n-1):
        index = 0
        for j in range(n-i-1):
            s = (nums[j]+nums[j+1])%10
            nums[index] = s
            index += 1
    return nums[0]


arr = [1,2,3,4,5]
print(triangularSum(arr))