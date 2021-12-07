
#Added into new branch
def conv(n):
    list1=['']*n
    k=2**n
    for i in range(0,len(list1)):
        j=2**i
        while len(list1[i])<k:
            list1[i]=list1[i]+("0"*j)+("1"*j)
    finalList=[]
    str1=""
    for item in range(0,k):
        for item2 in list1:
            str1=str1+item2[item]
        finalList.append(str1)
        str1=""
    print(finalList)




n=int(input("Enter a number for which you want to make the combination of 1,0:-   "))


conv(n)
