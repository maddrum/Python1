city = input().lower()
s = float(input())
if s < 0:
    print("error")
    exit()
if city not in ("sofia", "varna", "plovdiv"):
    print("error")
    exit()
salesSofia=("5","7","8","12")
salesVarna=("4.5","7.5","10","13")
salesPlovdiv=("5.5","8","12","14.5")
if city == "sofia":
    if s==0 or s<=500:
        sales = s*float(salesSofia[0])/100
    elif s<=1000:
        sales = s*float(salesSofia[1])/100
    elif s<=10000:
        sales = s*float(salesSofia[2])/100
    else:
        sales = s*float(salesSofia[3])/100
if city == "varna":
    if s==0 or s<=500:
        sales = s*float(salesVarna[0])/100
    elif s<=1000:
        sales = s*float(salesVarna[1])/100
    elif s<=10000:
        sales = s*float(salesVarna[2])/100
    else:
        sales = s*float(salesVarna[3])/100
if city == "plovdiv":
    if s==0 or s<=500:
        sales = s*float(salesPlovdiv[0])/100
    elif s<=1000:
        sales = s*float(salesPlovdiv[1])/100
    elif s<=10000:
        sales = s*float(salesPlovdiv[2])/100
    else:
        sales = s*float(salesPlovdiv[3])/100

print("{0:.2f}".format(sales))

