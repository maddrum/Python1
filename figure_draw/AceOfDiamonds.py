c = int(input("въведете нечетно число, различно от 1:"))
#проверка на въведеното число и въвеждане на коректно число
while c%2 == 0 or c == 1:
    c = int(input("моля въведете НЕЧЕТНО число, КОЕТО НЕ Е 1:"))
med = int(((c-2) / 2) + 0.5)
print(med)
if c == 3:
    print("*"*3)
    print("*@*")
    print("*"*3)
else:

    print("*"*c)
    for j in range(1,med):
        print("*", end="")
        k = int(((c-2)-(2*j-1))/2)
        print("-"*k, end="")
        print("@"*(2*j-1), end="")
        print("-" * k, end="")
        print("*")
    print("*", end="")
    print("@"*(c-2), end="")
    print("*")

    for j in range(1,med):
        print("*", end="")
        k = (c - 2) - 2*j
        print("-" * j, end="")
        print("@" * k, end="")
        print("-" * j, end="")
        print("*")

    print("*" * c)







