sumDollar = float(input("John left /in dollars/ :"))
exRate = float(input("Excgange rate USD/LV:"))
pizzaPrice = float(input("Pizza price/lv/:"))
lsPrice = float(input("Lasagna price/lv/:"))
sandPrice = float(input("Sandwich price/lv/:"))
pizzaQantity = int(input("Pizza wants-to-eat:"))
lsQantity = int(input("Lasagna wants-to-eat:"))
sandQantity = int(input("Sandwich wants-to-eat:"))
sumLv = sumDollar *exRate

totalSum = pizzaPrice * pizzaQantity + lsPrice * lsQantity + sandPrice * sandQantity

if totalSum < sumLv :
    moneyLeft = (sumLv-totalSum)/exRate
    moneyLeft = round(moneyLeft, 2)
    print("Garfield is well fed, John is awesome. Money left: $", moneyLeft,end=".")
else:
    moneyLeft = (totalSum - sumLv) / exRate
    moneyLeft = round(moneyLeft, 2)
    print("Garfield is hungry. John is a badass. Money needed: $", moneyLeft,end=".")








