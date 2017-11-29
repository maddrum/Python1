weight = float(input())
type = input()
dist = int(input())
price1=0
if weight <= 1:
    price = 0.03
elif weight <= 10:
    price = 0.05
elif weight <+ 40:
    price = 0.10
elif weight <=90:
    price = 0.15
else:
    price = 0.20
if type == "express":
    if weight <= 1:
        price1 = price*0.8
    elif weight <= 10:
        price1 = 0.4*price
    elif weight < + 40:
        price1 = 0.05*price
    elif weight <= 90:
        price1 = 0.02*price
    else:
        price1 = 0.01*price
cost = price*dist+price1*weight*dist
print("The delivery of your shipment with weight of {0:.3f} kg. would cost {1:.2f} lv.".format(weight,cost))
