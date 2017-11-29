n=int(input())
if n%2==0:
    j=2*n
else:
    j=2*n-1
k=j-n//2-n

for i in range(0,n):
    print("-"*3*n+"*"+"-"*i+"*"+"-"*(5*n-(3*n+2+i)))
for i in range(0,k):
    print("*" * 3 * n + "*" + "-" * (n-1) + "*" + "-" * (5 * n - (3 * n + 2 + (n-1))))
l=j-n-k
for i in range(0,k-1):
    print("-" * (3 * n-i) + "*" + "-" * (n+2*i-1) + "*" + "-" * (5 * n - (3 * n-i+n+2*i-1+2)))
i=k-1
print("-" * (3 * n-i) + "*" + "*" * (n+2*i-1) + "*" + "-" * (5 * n - (3 * n-i+n+2*i-1+2)))