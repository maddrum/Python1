n=int(input())
print("."*n+"*"*(3*n)+"."*n)
j=3*n+2-(n+1)
for i in range(1,n):
    print("."*(n-i)+"*"+"."*(5*n-2*(n-i+1))+"*"+"."*(n-i))
print("*"*5*n)
for i in range(1,j):
    print("."*i+"*"+"."*(5*n-(i+1)*2)+"*"+"."*i)
print("."*(2*n+1)+"*"*(5*n-2*(2*n+1))+"."*(2*n+1))
