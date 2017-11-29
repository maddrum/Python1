n = int(input())
kolona = 5*n
red = 2*n+4
n2=n//2
for i in range(0,n2):
    print("."*n + "."*i + "#"*(kolona - 2*n - 2*i) + "."*i + "."*n)
    k=n+i
for i in range(0,n2+1):
    print("."*(k+1+i) + "#" + "." * (kolona-2*(k+1)-2-2*i) + "#" + "."*(k+1+i))
    j=k+1+i
print("."*j + "#"*(kolona-2*j) +"."*j )
for i in range(0,n2):
    print("."*(2*n - 2) + "#"*(kolona - 4*n + 4) + "."*(2*n - 2))
print("."*((kolona-9)//2) + "D^A^N^C^E^" + "."*((kolona-9)//2))
for i in range(0,n2+1):
    print("."*(2*n - 2) + "#"*(kolona - 4*n + 4) + "."*(2*n - 2))

