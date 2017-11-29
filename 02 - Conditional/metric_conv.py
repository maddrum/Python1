unitValue = float(input())
unitType = input()
unitConv = input()
#дефиниране на масиви за референтни стойности за референтна единица
convChart = [1, 100, 0.000621371192, 39.3700787 , 0.001, 3.2808399, 1.0936133, 1000]
convName = ["m","cm", "mi","in","km","ft","yd", "mm"]
#превръщане на въведената единица в референтна единица
unitToMeter = unitValue/convChart[convName.index(unitType)]

unitConverted = unitToMeter * (convChart[convName.index(unitConv)])
print(str(unitConverted) + " " + unitConv)
