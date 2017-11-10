budget = float(input())
season = input()
if season =="summer" and budget <=1000:
    venueType="Camp"
    if budget <=100:
        destination = "Bulgaria"
        cost = 0.3
    else:
        destination="Balkans"
        cost = 0.4


elif season=="winter" and budget <=1000:
    venueType = "Hotel"
    if budget <=100:
        destination="Bulgaria"
        cost = 0.7
    else:
        destination = "Balkans"
        cost = 0.8
if budget >1000:
    venueType="Hotel"
    destination = "Europe"
    cost=0.9
totalCost=cost*budget
print("Somewhere in {}".format(destination))
print(venueType +" - " + "{0:.2f}".format(totalCost))
