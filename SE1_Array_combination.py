
from time import time

list1=[1,1,1,2,2,2,0,0,0,1,0,2,1,0,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,2,2,2,2,2,2,0,0]

time1=time()
list2=[0]*list1.count(0)+[1]*list1.count(1)+[2]*list1.count(2)

print(list2)
print(time()-time1)

time2=time()
list3=[]
for i in range(0,3):
    list3+=[i]*list1.count(i)

print(list3)
print(time()-time2)


