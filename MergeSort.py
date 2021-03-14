def mergeSort(list1):
    if len(list1)>1:
        n=len(list1)//2
        leftPart=list1[:n]
        rightPart=list1[n:]
        mergeSort(leftPart)
        mergeSort(rightPart)
        i=j=0
        k=0
        while i< len(leftPart) and j< len(rightPart):
            if leftPart[i]<=rightPart[j]:
                list1[k]=leftPart[i]
                i+=1
                k+=1
            else:
                list1[k]=rightPart[j]
                j+=1
                k+=1
        while i< len(leftPart):
            list1[k]=leftPart[i]
            i+=1
            k+=1
        while j< len(rightPart):
            list1[k]=rightPart[j]
            j+=1
            k+=1

list1=[6,3,10,52,4,1,8,2]

mergeSort(list1)
print(list1)