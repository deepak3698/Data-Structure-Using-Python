

def uniquePaths(m,n):
    uSide=m+n-2
    if m>n:
        dSide=n-1
    else:
        dSide=m-1
        
    finalVal=1
    for i in range(1,dSide+1):
        finalVal=finalVal*((m+n-1-i)/i)
        print(finalVal)
        


uniquePaths(9,8)