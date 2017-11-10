showType=input().lower()
r=int(input())
c=int(input())
total = r*c
if showType =="premiere":
    price = total *12
elif showType =="normal":
    price = total*7.5
else:
    price = 5*total
print("{0:.2f} leva".format(price))
