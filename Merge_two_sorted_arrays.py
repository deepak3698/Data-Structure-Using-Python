

list1=[1, 5, 9, 10, 15, 20]

list2=[2, 3, 8, 13]
list3=list1+list2
list3.sort()


list1,list2=list3[0:len(list1)],list3[len(list1):]

print(list1,list2)

#Time complexity O(2n)
