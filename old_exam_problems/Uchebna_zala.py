w=float(input("w /m/: "))
while w < 2.99 or w > 100.01:
    print("Моля, въведете коректно h (3 <= h <=100)")
    w = float(input("h: "))
    round(w,2)
h=float(input("h /m/: "))
round(h,2)
while h < 2.99 or h > 100.01:
    print("Моля, въведете коректно h (3 <= h <=100)")
    h = float(input("h: "))
    round(h,2)
while w < (h-0.01):
    print("Моля, въведете коректно w (w>h)")
    h = float(input("h: "))
    round(h, 2)

columns = int(w // 1.2)
rows = int((h-1) // 0.7 )
banks = columns*rows-3
print(banks)









