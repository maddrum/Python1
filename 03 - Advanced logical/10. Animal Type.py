animal1 = input().lower()
if animal1=="dog":
    print("mammal")
elif animal1 in ("crocodile", "tortoise", "snake"):
    print("reptile")
else:
    print("unknown")