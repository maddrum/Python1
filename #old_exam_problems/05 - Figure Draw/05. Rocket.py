n=int(input())
j=n//2
for i in range(0,n):
    print("."*((3*n-2)//2-i)+"/"+" "*(2*i)+"\\"+"."*((3*n-2)//2-i))
print("."*j+"*"*(3*n-j*2)+"."*j)
for i in range(0,2*n):
    print("."*j+"|"+"\\"*(3*n-2*j-2)+"|"+"."*j)
for i in range(0,n//2):
    print("."*(j-i)+"/"+"*"*(3*n-2*j-2+2*i)+"\\"+"."*(j-i))
