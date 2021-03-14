import math
str1=""
def permutation(list1,n,k):
    global str1
    if len(list1)==0:
        return
    else:
        fact1=math.factorial(n)
        val=fact1/n
        position=math.ceil(k/val)
        reminder=k%val
        list1[0],list1[position-1]=list1[position-1],list1[0]
        str1+=str(list1[0])
        list1.pop(0)
        return permutation(list1,n-1,reminder)

permutation(['A','B','C','D','E'],5,50)
print(str1)




# import math
# list2=[]
# def permutation(list1,n,k):
#     if len(list1)==0:
#         return
#     else:
#         fact1=math.factorial(n)
#         val=fact1/n
#         position=math.ceil(k/val)
#         reminder=k%val
#         list1[0],list1[position-1]=list1[position-1],list1[0]
#         list2.append(list1[0])
#         print(list2)
#         list1.pop(0)
#         permutation(list1,n-1,reminder)

# permutation([1,2,3,4],4,13)




        

