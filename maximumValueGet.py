N=3
W=70
values=[60,100,120,100]
weight=[10,20,30,40]
sum1=0
totalPrice=0
for item in range(0,len(values)):
    if sum1+weight[item]<W:
        totalPrice=totalPrice+values[item]
        sum1+=weight[item]
    elif sum1+weight[item]==W:
        totalPrice=totalPrice+values[item]
        break
    else:
        totalPrice=totalPrice+(values[item]/weight[item])*(W-sum1)
        break
print(totalPrice)

    


