n=int(input())
for i in range(1,n+1):
    k=i
    r=1
    for j in range(1,n+1):
        if k<=n:
            print(k, end=" ")
        else:
            print(n-r, end = " ")
            r+=1
        k+=1
    print()