n=int(input())
koloni=3*n+6
red=3*n+1
for i in range(0,n):
    print(" "*n+"~ ~ ~")
print("="*(koloni-1))
if n==3:
    print("|" + "~" * n + "JAVA" + "~" * n + "|" + " " * (n - 1) + "|")
elif (n-3)%2==0:
    for i in range(0,(n-3)//2):
        print("|" + "~"*n + "~"*4 + "~"*n + "|" + " "*(n-1) + "|")
    print("|" + "~" * n + "JAVA" + "~" * n + "|" + " " * (n - 1) + "|")
    for i in range(0, (n-3)//2):
        print("|" + "~" * n + "~" * 4 + "~" * n + "|" + " " * (n - 1) + "|")
else:
    for i in range(0,(n-3)//2+1):
        print("|" + "~"*n + "~"*4 + "~"*n + "|" + " "*(n-1) + "|")
    print("|" + "~" * n + "JAVA" + "~" * n + "|" + " " * (n - 1) + "|")
    for i in range(0, ((n-3)//2)):
        print("|" + "~" * n + "~" * 4 + "~" * n + "|" + " " * (n - 1) + "|")

print("="*(koloni-1)+ " ")
t1=2*n+6
for i in range(0,n):
    print(" "*i + "\\" + "@"*(t1-2*i-2) + "/ " )
print("="*t1)