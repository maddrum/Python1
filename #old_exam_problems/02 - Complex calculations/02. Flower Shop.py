import math
magnolia=int(input())
zumbul=int(input())
rose=int(input())
cactus=int(input())
price=float(input())
total=magnolia*3.25+zumbul*4+rose*3.5+cactus*8
total=0.95*total
if total>=price:
    totalPrint=math.floor(abs(price-total))
    print("She is left with {} leva.".format(totalPrint))
else:
    totalPrint = math.ceil(abs(total-price))
    print("She will have to borrow {} leva.".format(totalPrint))