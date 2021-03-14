N=6
list1=[1,3,0,5,8]
list2=[2,4,6,7,9]

## List2 need to be sorted
dict1={}


# dict1[str(list2[0])+str(i)]=list1[0]
# dict1[str(list2[0])]=list1[1]
# for i in range(0,len(list1)):
#     k=str(list2[i])
#     print(k)
    # dict1[k]=dict1[list1[i]]


MaxPossibleMeetings=0
PosibleIndexPoint=[]
maxAtList=0
for index in range(0,len(list1)):
    if index==0:
        if list1[index]>list2[index]:
            print(f"Meeting not possible for {index+1}")
        else:
            MaxPossibleMeetings+=1
            maxAtList=list2[index]
            PosibleIndexPoint.append(index+1)
    else:
        if list1[index]>list2[index]:
            print(f"Meeting not possible for {index+1}")
        elif list1[index]<maxAtList:
            print(f"Meeting not possible for {index+1}")
        else:
            MaxPossibleMeetings+=1
            maxAtList=list2[index]
            PosibleIndexPoint.append(index+1)

print(f"Total possible meeting are : {MaxPossibleMeetings}")
print(f"Meeting indexes are at the possible meeting : {PosibleIndexPoint}")

