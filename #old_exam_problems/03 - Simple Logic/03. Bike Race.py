junior=int(input())
master=int(input())
type=input()
total=junior+master
if type=="trail":
    price=5.5*junior+master*7
elif type=="cross-country":
    if total>=50:
        price = junior * 8*.75 + master * 9.5*.75
    else:
        price=junior*8+master*9.5
elif type=="downhill":
    price=12.25*junior+13.75*master
elif type=="road":
    price=junior*20+master*21.5
else:
    print("error")
price=0.95*price
price1=round(price,2)
print("{0:.2f}".format(price1))


