n = int(input())
red=2*(n-2)+1
kol=2*n-1
for i in range(0,n-2):
    if i % 2 == 0:
        print("*"*(n-2)+"\\ /"+"*"*(n-2))
    else:
        print("-" * (n - 2) + "\\ /" + "-" * (n - 2))
print(" "*(n-1)+"@")
for i in range(0,n-2):
    if i % 2 == 0:
        print("*" * (n - 2) + "/ \\" + "*" * (n - 2))
    else:
        print("-" * (n - 2) + "/ \\" + "-" * (n - 2))


