budget = float(input())
cat= input().lower()
ppl= int(input())
if ppl <=4:
    cost=0.75
elif ppl in range(5,10):
    cost = 0.6
elif ppl in range(10,25):
    cost = 0.5
elif ppl in range(25,50):
    cost = 0.4
else:
    cost = 0.25
transCost=cost*budget
if cat == "vip":
    money=budget - transCost - 499.99*ppl
else:
    money=budget-transCost-249.99*ppl
if money>=0:
    print("Yes! You have "+"{0:.2f}".format(abs(money))+ " leva left.")
else:
    print("Not enough money! You need "+"{0:.2f}".format(abs(money))+" leva.")
