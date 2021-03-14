
from time import time

list1=[]

for item in range(1,1000000):
    list1.append(item)


# print(list1)

time1=time()

print(list1.count(1))

print(time()-time1)