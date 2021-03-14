
def mergeSort(list1):
    if len(list1)<=1:
        return list1
    mid=len(list1)//2
    left_list=list1[:mid]
    right_list=list1[mid:]
    mergeSort(left_list)
    mergeSort(right_list)
    Merge_Two_Sorted_Array(left_list,right_list,list1)

def Merge_Two_Sorted_Array(a,b,list1):
    i=0
    j=0
    k=0
    while i<len(a) and j<len(b):
        if a[i]<=b[j]:
            list1[k]=a[i]
            i+=1
        else:
            list1[k]=b[j]
            j+=1
        k+=1
    while i<len(a):
        list1[k]=a[i]
        i+=1
        k+=1
    while j<len(b):
        list1[k]=b[j]
        j+=1  
        k+=1

if __name__=="__main__":
    # list1=[9,3,7,5,1,5]
    list1=[6,43,65,87,7,5,30,31]
    mergeSort(list1)
    print(list1)

