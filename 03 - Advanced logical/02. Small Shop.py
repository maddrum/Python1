product = input().lower()
city = input().lower()
quantity = float(input())
price = 0
if city == "sofia":
    if product == "coffee":
        price = quantity*.5
    elif product == "water":
        price = quantity*0.8
    elif product == "beer":
        price = quantity*1.2
    elif product == "sweets":
        price = quantity*1.45
    else:
        price = quantity*1.60
if city == "plovdiv":
    if product == "coffee":
        price = quantity *0.4
    elif product == "water":
        price = quantity * 0.7
    elif product == "beer":
        price = quantity * 1.15
    elif product == "sweets":
        price = quantity * 1.30
    else:
        price = quantity * 1.50
if city == "varna":
    if product == "coffee":
        price = quantity * 0.45
    elif product == "water":
        price = quantity * 0.7
    elif product == "beer":
        price = quantity * 1.10
    elif product == "sweets":
            price = quantity * 1.35
    else:
        price = quantity * 1.55

print("{:0.2f}".format(price))
