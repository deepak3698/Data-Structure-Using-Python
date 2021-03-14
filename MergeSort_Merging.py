
def mergeSort(list1):
    if len(list1)<=1:
        return list1
    mid=len(list1)//2
    left_list=list1[:mid]
    right_list=list1[mid:]
    left_list=mergeSort(left_list)
    right_list=mergeSort(right_list)
    return Merge_Two_Sorted_Array(left_list,right_list)


def Merge_Two_Sorted_Array(a,b):
    i=0
    j=0
    finalOutput=[]
    while i<len(a) and j<len(b):
        if a[i]<=b[j]:
            finalOutput.append(a[i])
            i+=1
        else:
            finalOutput.append(b[j])
            j+=1
    while i<len(a):
        finalOutput.append(a[i])
        i+=1
    while j<len(b):
        finalOutput.append(b[j])
        j+=1  
    return finalOutput

if __name__=="__main__":
    # list1=[9,3,7,5,1,5]
    list1=[6,43,65,87,7,5,30,31]
    output=mergeSort(list1)
    print(output)

