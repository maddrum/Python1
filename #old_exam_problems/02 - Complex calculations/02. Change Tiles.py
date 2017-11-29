import math
money=float(input())
lenght=float(input())
width=float(input())
trSize=float(input())
trHeight=float(input())
sPrice=float(input())
masterPr=float(input())
area=lenght*width
plNumber=math.ceil(area/(trHeight*trSize/2))+5
price = masterPr+plNumber*sPrice
if money >=price:
    print("{0:.2f} lv left.".format(money-price))
else:
    print("You'll need {0:.2f} lv more.".format(price-money))

