'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum1=0
        max1=nums[0]
        for i in range(0,len(nums)):
            sum1+=nums[i]
            if sum1>max1:
                max1=sum1
            if sum1<0:
                sum1=0
            
            

        return max1

'''
nums=[-2,-1]
finalList=[]
sum1=0
dt=[]
max1=nums[0]
for i in range(0,len(nums)):
    sum1+=nums[i]
    if sum1<0:
        sum1=0
        finalList.clear()
    else:
        finalList.append(nums[i])
    if sum1>max1:
        dt=finalList[:]
        max1=sum1
        # finalList.append(nums[i])

print(dt)
print(finalList)
print(max1)

