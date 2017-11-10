n=int(input())
red=n*4+3
kol=n*2+3
print("."*(n+1)+"_"*(red-2*(n+1))+"."*(n+1))
for i in range(0,n):
    print("."*(n-i)+"//"+"_"*(red-2*(n-i+2))+"\\"*2+"."*(n-i))
print("//"+"_"*((red-9)//2)+"STOP!"+"_"*((red-9)//2)+"\\"*2)
for i in range(0,kol-(n+3)):
    print("." * (i) + "\\"*2 + "_" * (red - (2 *i + 4)) + "//"  + "." * (i))
