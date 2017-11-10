age=float(input())
sex=input().lower()

if sex == "m" and age<16:
    print("Master")
elif sex =="m" and age >=16:
    print("Mr.")
elif sex =="f" and age >=16:
    print("Ms.")
else:
    print("Miss")

