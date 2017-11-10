n=int(input())
red=2*n+3
sp1=n//3
sp2=(n-1)//2
for i in range(1,n+1):
    print("*"*i+"\\"+"-"*(red-(2*i+2))+"/"+"*"*i)
for i in range(0,sp1):
    print("|"+"*"*((n-1)//2)+"*"*i+"\\"+"*"*(red-(4+sp2*2+2*i))+"/"+"*"*i+"*"*((n-1)//2)+"|")
for i in range(1,n+1):
    print("-"*i+"\\"+"*"*(red-(2*i+2))+"/"+"-"*i)
