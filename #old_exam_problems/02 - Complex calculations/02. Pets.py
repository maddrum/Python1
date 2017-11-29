from math import floor as f
days=int(input())
food=int(input())
dog=float(input())
cat=float(input())
turtle=float(input())
turtle=turtle/1000
foodNeeded=days*(dog+cat+turtle)
foodAbs=abs(f(food-foodNeeded))
if food>=foodNeeded:
    print("{} kilos of food left.".format(foodAbs))
else:
    print("{} more kilos of food are needed.".format(foodAbs))
    