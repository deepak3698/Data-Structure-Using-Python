from time import time
n=10000000

list1=[]
for item in range(1,n+1):
    list1.append(item)

list1[98765]=3476526

time1=time()
dict1={}
repNum=0
sum1=0
for item in list1:
    if item in dict1:
        repNum=item
    dict1[item]=item

for item in dict1.keys():
    sum1+=item
print(f"Repetive number is {repNum}")
print(f"Missing number is {(n*(n+1)//2)-sum1} ")

print(f"first time taken is {time()-time1}")


