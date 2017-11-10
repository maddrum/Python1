fruit=input().lower()
day = input().lower()
quantity = float(input())
fruitChart = ("banana", "apple", "orange", "grapefruit", "kiwi", "pineapple", "grapes")
fruitPriceWeek = ("2.50", "1.20", "0.85", "1.45", "2.70", "5.50", "3.85")
fruitPriceWeekend = ("2.70", "1.25", "0.90", "1.60", "3", "5.60", "4.2")
weekday = ()
try:
    i=fruitChart.index(fruit)
except:
    print("error")
    exit()
if day in ("monday","tuesday","wednesday","thursday","friday"):
    price = float(quantity)*float(fruitPriceWeek[i])
    print("{0:.2f}".format(price))
elif day in ("saturday", "sunday"):
    price = float(quantity)*float(fruitPriceWeekend[i])
    print("{0:.2f}".format(price))
else:
    print("error")




