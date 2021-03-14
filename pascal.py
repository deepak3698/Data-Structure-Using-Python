


n=5
list1=[]

list2=[]

def pascal(i1,j1):
    n=1
    r=1
    for i in range(i1,i1-j1,-1):
        n=n*i
    for j in range(1,j1+1):
        r=r*j
    return n//r
a=[]
for i in range(1,6):
    list2.clear()
    for j in range(1,i+1):
        list2.append(pascal(i-1,j-1))
    list1.append(list2[:])

print(list1)





