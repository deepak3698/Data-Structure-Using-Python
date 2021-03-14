start1=[50,120,200,550,700,850]
end1=[500,550,600,700,900,1000]

min1=end1[0]
i=0
val=1

for k in range(1,len(start1)):
    if start1[k]<=min1:
        val+=1
    elif start1[k]>min1:
        i+=1
        min1=end1[i]
    else:
        pass

print(val)

# #User function Template for python3

# class Solution:    
#     #Function to find the minimum number of platforms required at the
#     #railway station such that no train waits.
#     def minimumPlatform(self,n,arr,dep):
#         '''
#         :param n: number of activities
#         :param arr: arrival time of trains
#         :param dep: corresponding departure time of trains
#         :return: Integer, minimum number of platforms needed
#         '''
#         # code here
#         arr.sort()
#         dep.sort()
        
#         minVal=dep[0]
#         i=0
#         minPlatform=1
#         for k in range(1,len(arr)):
#             if arr[k]<=minVal:
#                 minPlatform+=1
#             elif arr[k]>minVal:
#                 i+=1
#                 minVal=dep[i]
#             else:
#                 pass
#         return minPlatform

# #{ 
# #  Driver Code Starts
# #Initial Template for Python 3
# import atexit
# import io
# import sys

# #Contributed by : Nagendra Jha


# if __name__ == '__main__':
#     test_cases = int(input())
#     for cases in range(test_cases) :
#         n = int(input())
#         arrival = list(map(str,input().strip().split()))
#         departure = list(map(str,input().strip().split()))
#         ob=Solution()
#         print(ob.minimumPlatform(n,arrival,departure))
# # } Driver Code Ends