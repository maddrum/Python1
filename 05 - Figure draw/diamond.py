n=int(input())
j=0
n2=n//2
if n==1:
    print("*")
    exit()
if n%2==0:
    for i in range(0,n2-1):
        print("-"*(((n-2)//2)-i)+"*"+"-"*2*i+"*"+"-"*(n-(((n-2)//2)-i)-2*i-2))
        j+=1
else:
    i= (n-1)//2
    print("-" * i + "*" + "-" * i)
    for i in range(1, n2):
        print("-" * (n2-i) + "*"+"-"*(2*i-1)+"*"+ "-" * (n2-i))
        j+=1
print("*"+"-"*(n-2)+"*")
red=n-j-1
if n%2==0:
    for i in range(n2-2,-1,-1):
        print("-"*(((n-2)//2)-i)+"*"+"-"*2*i+"*"+"-"*(n-(((n-2)//2)-i)-2*i-2))
        j+=1
else:
    for i in range(n2-1,0,-1):
        print("-" * (n2-i) + "*"+"-"*(2*i-1)+"*"+ "-" * (n2-i))
    i = (n - 1) // 2
    print("-" * i + "*" + "-" * i)

