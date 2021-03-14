


list1=[6,2,8,4,1]
list2=[8,3,6,2,9]
dict1={}
for i in range(0,len(list1)):
    dict1[list1[i]]=list2[i]


print(dict1)

a=sorted(dict1.items(),key=lambda x: x[1],reverse=False)
print(a)
print(type(a))
    






