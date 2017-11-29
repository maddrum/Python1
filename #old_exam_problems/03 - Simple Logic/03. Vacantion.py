normal=int(input())
students=int(input())
sleeps=int(input())
transport=input()

if transport=="train":
    if normal+students<50:
        tPriceN=24.99
        tPriceS=14.99
    else:
        tPriceN=24.99*.5
        tPriceS=14.99*.5
elif transport=="bus":
    tPriceN=32.50
    tPriceS=28.50
elif transport=="boat":
    tPriceN=42.99
    tPriceS=39.99
else:
    tPriceN=70.00
    tPriceS=50.00
transportPrice=(tPriceN*normal+tPriceS*students)*2
sleepPrice=sleeps*82.99
totalSum=(transportPrice+sleepPrice)*1.1

print("{0:.2f}".format(totalSum))
