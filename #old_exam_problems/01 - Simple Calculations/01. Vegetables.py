vegetablePrice = float(input())
fruitPrice = float(input())
totalVegetables = float(input())
totalFruit = float(input())


totalRevLv=vegetablePrice*totalVegetables + fruitPrice*totalFruit
totalRevEur=round((totalRevLv/1.94),13)
print(totalRevEur)
