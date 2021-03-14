from time import time

list1=[]
for item in range(1,100):
    list1.append(item)
n=97    
time1=time()
res=False
for i in range(0,len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i]+list1[j]==n:
            print(i,j)
            res=True
            break
    if res:
        break
time2=time()
print(f"time taken by list method is {time2-time1}")
dict1={}
for i,j in enumerate(list1):
    if(n-j in dict1):
        print(dict1[n-j],i)
        break
        
    else:
        dict1[j]=i
time3=time()
print(f"time taken by dict method is {time3-time2}")







