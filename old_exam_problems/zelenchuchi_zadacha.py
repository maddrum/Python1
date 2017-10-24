vegetablePrice = float(input("Цена на кг зеленчуци /лв/:"))
while vegetablePrice < 0.001 or vegetablePrice > 1000.000:
    vegetablePrice = round(float(input("Моля, коректна цена на кг зеленчуци /лв/:")),3)


fruitPrice = float(input("Цена на кг плодове /лв/ :"))
while fruitPrice < 0.001 or fruitPrice > 1000.000:
    fruitPrice = round(float(input("КОРЕКНТА! Цена на кг плодове /лв/ :")), 3)


totalVegetables1 = float(input("Общо зеленчуци /кг/:"))
while totalVegetables1 < 0.001 or totalVegetables1 > 1000.000:
    totalVegetables1 = float(input("КОРЕКТНО Общо зеленчуци /кг/:"))
totalVegetables = int(totalVegetables1)


totalFruit1 = float(input("Общо плодове /кг/:"))
while totalFruit1 < 0.001 or totalFruit1 > 1000.000:
    totalFruit1 = float(input("КОРЕКТНО! Общо плодове /кг/:"))
totalFruit = int(totalFruit1)


totalRevLv=vegetablePrice*totalVegetables + fruitPrice*totalFruit
totalRevEur=round((totalRevLv/1.94),13)
print(totalRevEur)
