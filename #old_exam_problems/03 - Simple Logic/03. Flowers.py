hr=int(input())
rose=int(input())
tul=int(input())
season=input().lower()
holiday=input().lower()
if season=="spring" or season=="summer":
    price =  2 * hr + 4.10 * rose + 2.5 * tul
else:
    price = 3.75 * hr + 4.5 * rose + 4.15 * tul
if holiday=="y":
    price = 1.15 * price
if tul > 7 and season == "spring":
    price = price * 0.95
if rose >=10 and season == "winter":
    price = price * 0.9
if hr+rose+tul >20:
    price = price * 0.8
price = price +2
print("{0:.2f}".format(price))

