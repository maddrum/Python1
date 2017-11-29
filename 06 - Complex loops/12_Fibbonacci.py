n=int(input())
if n<2:
    a=1
else:
    x=1
    y=1
    print("1 1", end=" ")
    for i in range(1,n):
        a=x+y
        x=y
        y=a
        print(a, end=" ")
print()
print(a)
