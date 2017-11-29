n=int(input())
j=0
if n%2==0:
    for i in range(0,n//2-1):
        print("-"*(((n-2)//2)-i)+"*"*2+"*"*2*i+"-"*(((n-2)//2)-i))
        j+=1
else:
    for i in range(0, n // 2):
        print("-" * ((n-(2*i+1))//2) + "*"*(2*i+1)+ "-" * ((n-(2*i+1))//2))
        j+=1
print("*"*n)
red=n-j-1
for i in range(0,red):
    print("|"+"*"*(n-2)+"|")
