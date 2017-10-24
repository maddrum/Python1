valuta1=float(input("Въведете сума : "))
valuta1Type1 = input("Въведете вид валута - BGN, USD, EUR или GBP: ")
convBG1 = 0

while (valuta1Type1 not in("USD", "EUR", "BGN", "GBP")):
    print("Моля въведете коректен тип валута")
    valuta1Type1 = input("Въведете вид валута - BGN, USD, EUR или GBP: ")

valuta1Type2=input("Въведете вид валута, в която искате да получите резултата - BGN, USD, EUR или GBP ")

while (valuta1Type2 not in("USD", "EUR", "BGN", "GBP")):
    print("Моля въведете коректен тип валута")
    valuta1Type2 = input("Въведете вид валута - BGN, USD, EUR или GBP: ")

if valuta1Type1 == "BGN":
    convBG1=valuta1
else:
    if valuta1Type1 == "USD":
        convBG1 = valuta1*1.79549
    if valuta1Type1 == "EUR":
        convBG1 = valuta1 * 1.95583
    if valuta1Type1=="GBP":
        convBG1=valuta1*2.53405
if valuta1Type2 == "BGN":
    result = convBG1
else:
    if valuta1Type2 == "USD":
        result = convBG1 /1.79549
    if valuta1Type2 == "EUR":
        result =  convBG1 / 1.95583
    if valuta1Type2 == "GBP":
        result = convBG1 / 2.53405
result1=round(result, 2)
print(result1, " ", valuta1Type2)








