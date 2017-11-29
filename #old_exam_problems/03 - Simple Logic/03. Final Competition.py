n=int(input())
p=float(input())
season=input().lower()
place=input().lower()
if place == "bulgaria":
    money=n*p
else:
    money=(n*p)*1.5
if season == "summer":
    if place == "bulgaria":
        money=money*0.95
    else:
        money=money*0.9
else:
    if place == "bulgaria":
        money = money * 0.92
    else:
        money = money * 0.85
charity=0.75*money
left=(money-charity)/n

print("Charity - {0:.2f}".format(charity))
print("Money per dancer - {0:.2f}".format(left))
