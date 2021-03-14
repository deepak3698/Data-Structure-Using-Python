

a=[1,4,5,-6,2,3,-5,-4,7]

sum1=0
maxLen=0
for i in range(0,len(a)):
    sum1=0
    for j in  range(i,len(a)):
        sum1+=a[j]
        if sum1==5:
            maxLen+=1
               
print(f"Max Length of For {maxLen}")

sum2=0
dict1={}
maxValueD=0
for index,value in enumerate(a):
    sum2+=value
    if sum2==5:
        maxValueD+=1
        dict1[sum2]=index+1
    else:
        if sum2-5 in dict1:
            maxValueD+=1
        else:
            dict1[sum2]=index+1


print(f"Max Length of For {maxValueD}")
