from time import time
list1=[100,99,101,102,5,4,3,2,1,87,135,543]*20000

time1=time()
maxVal=0
for i in list1:
    j=1
    while True:
        if i+j in list1:
            j+=1
        else:
            break
    if j>maxVal:
        maxVal=j

print(maxVal)
time2=time()
print(f"time taken by for loop method is {time2-time1}")

time3=time()
maxValOfSet=0
for i in list1:
    if i-1 in list1:
        continue
    else:
        j=1
        while True:
            if i+j in list1:
                j+=1
            else:
                break
        if j>maxValOfSet:
            maxValOfSet=j
print(maxValOfSet)
time4=time()
print(f"Time taken by for loop by set method is {time4-time3}")





