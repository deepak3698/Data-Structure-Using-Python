#List to store the individual values
a1=[]
a2=[]

#Carry to store the remainder
carry=0
carry2=0

#Numnber's For multiplications
num1='798'
num2='88'

for i in num1[::-1]:
    for j in range(0,2):
        if j==0:
            print(carry)
            if len(str(int(i)*int(num2[-1]) +carry) )>1:
                a1.insert(0,(int(i)*int(num2[-1])+carry)%10)
                carry=(int(i)*int(num2[-1])+carry)//10
            else:
                if carry==0:
                    a1.insert(0,(int(i)*int(num2[-1])))
                else:
                    if len(str((int(i)*int(num2[-1]))+carry))>1:
                        a1.insert(0,(int(i)*int(num2[-1]))%10)
                        carry=(int(i)*int(num2[-1])+carry)//10
                    else:
                        a1.insert(0,(int(i)*int(num2[-1]))+carry)
                        carry=0

        else:
            if len(str(int(i)*int(num2[-2]) +carry2) )>1:
                a2.insert(0,(int(i)*int(num2[-2])+carry2)%10)
                carry2=(int(i)*int(num2[-2])+carry2)//10
            else:
                if carry2==0:
                    a2.insert(0,(int(i)*int(num2[-2])))
                else:
                    if len(str((int(i)*int(num2[-2]))+carry2))>1:
                        a2.insert(0,(int(i)*int(num2[-2]))%10)
                        carry2=(int(i)*int(num2[-2])+carry2)//10
                    else:
                        a2.insert(0,(int(i)*int(num2[-2]))+carry2)
                        carry2=0

if carry!=0:
    a1.insert(0,carry)

if carry2!=0:
    a2.insert(0,carry2)

#For New updated carry
newCarry=0

#Creating array for final addition
newArray=[a1[-1]]

x=-1
for i in range(0,len(a1)-1):
    if len(str(a1[x-1]+a2[x]+newCarry))>1:
        newArray.insert(0,(a1[x-1]+a2[x]+newCarry)%10)
        newCarry=(a1[x-1]+a2[x]+newCarry)//10
    else:
        newArray.insert(0,(a1[x-1]+a2[x]+newCarry))
        newCarry=0
    x-=1

if newCarry!=0:
    if len(str(a2[0]+newCarry))>1:
        newArray.insert(0,(a2[0]+newCarry)%10)
        newArray.insert(0,(a2[0]+newCarry)//10)
    else:
        newArray.insert(0,a2[0]+newCarry)

print(newArray)

        

