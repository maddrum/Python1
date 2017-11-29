n=int(input())
k=1
if n==1:
    print("1")
elif n==2:
    print("1")
    print("2")
else:
    for i in range(1,n):
        if k>n:
            break
        for j in range(0,i):
            print(k, end=" ")
            k+=1
            if k>n:
                break
        print()
