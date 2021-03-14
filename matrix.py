
##Rotate 90 deg right to a matrix
#-------------------------#
list1=[[1,2,3],[4,5,6],[7,8,9]]
    
# finalList=[[0]*3]*3
# # finalList=[[0,0,0],[0,0,0],[0,0,0]]
# for i in range(0,3):
#     for j in range(0,3):
#         finalList[j][2-i]=list1[i][j]
#         print(finalList)

# print(finalList)

#-------------------------#

# First transpose to the Matrix

# for i in range(0,3):
#     for j in range(i,3):
#         list1[i][j],list1[j][i]=list1[j][i],list1[i][j]
# print(list1)

# Reverse to the element( row wise) to get the 90 deg value

# print(len(list1))

# for i in range(0,3):
#     for j in range(0,len(list1)//2):
#         list1[i][j],list1[i][2-j]= list1[i][2-j], list1[i][j]

# print(list1)


### Searching in Matric when it is sorted by row as well as by column


list2=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]



i=0
j=len(list2[0])-1
elementToSearch=98


# while True:
#     try:
#         if list2[i][j]==elementToSearch:
#             print(f"Found at f{i,j}")
#             break
#         elif list2[i][j]>elementToSearch:
#             j-=1
#         else:
#             i+=1
#     except:
#         print("Element is not available")
#         break
print(len(list2))
while (i<=len(list2)-1 and j>=0):
    if list2[i][j]==elementToSearch:
        print(f"Found at f{i,j}")
        break
    elif list2[i][j]>elementToSearch:
        j-=1
    else:
        i+=1
else:
    print("Not available")





