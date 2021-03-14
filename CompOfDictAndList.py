
from time import time
list1=[]
dict1={}

time1=time()
for i in range(0,10000000):
    dict1[i]=i
time2=time()
print(f"time taken by dict creation is {time2-time1}")
time3=time()

for i in range(0,10000000):
    list1.append(i)
time4=time()
print(f"time taken by list creation is {time4-time3}")

time5=time()


if 9999013 in dict1:
    print("yes")


time6=time()
print(f"time taken by dict search is {time6-time5}")

time7=time()

if 9999013 in list1:
    print("yes")

time8=time()
print(f"time taken by list search is {time8-time7}")


