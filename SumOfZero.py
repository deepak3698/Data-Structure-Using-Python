from time import time
a=[1,4,5,-6,2,3,-5,-4,7]*10000
time1=time()
sum1=0
maxLen=0
for i in range(0,len(a)):
    sum1=0
    for j in  range(i,len(a)):
        sum1+=a[j]
        if sum1==0:
            if j-i+1>maxLen:
                maxLen=j-i+1
               
print(f"Max Length of For {maxLen}")
time2=time()
print(f"time for loop solution {time2-time1} ")
# time3=time()
# sum2=0
# dict1={}
# maxValueD=0
# for index,value in enumerate(a):
#     sum2+=value
#     if sum2==0:
#         maxValueD=index+1
#     else:
#         if sum2 in dict1:
#             if (index+1-dict1[sum2]) > maxValueD:
#                 maxValueD=index+1-dict1[sum2]
#         else:
#             dict1[sum2]=index+1


# print(f"Max Length of For {maxValueD}")
# time4=time()

# print(f"time for dict solution {time4-time3} ")