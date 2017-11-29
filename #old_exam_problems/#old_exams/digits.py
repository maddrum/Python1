n=int(input())
helper=str(n)
x=int(helper[0])
y=int(helper[1])
z=int(helper[2])
N=x+y
M=x+z
for i in range(0,N):
    if i!=0:
        print()
    for j in range(0,M):
        if n%5==0:
            n-=x
        elif n%3==0:
            n-=y
        else:
            n+=z
        print(n,end=" ")


