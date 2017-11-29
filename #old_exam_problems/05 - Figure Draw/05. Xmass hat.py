n=int(input())
red = 2*n+5
kolona = 4*n+1
pat1=(kolona-3)//2
print("."*((kolona-3)//2)+"/|"+"\\"+"."*((kolona-3)//2))
print("."*((kolona-3)//2)+"\|"+"/"+"."*((kolona-3)//2))
for i in range(0,2*n):
    print("."*(pat1-i)+"*"+"-"*i+"*"+"-"*i+"*"+"."*(pat1-i))
print("*"*kolona)
print("*."*(kolona//2)+"*")
print("*"*kolona)


