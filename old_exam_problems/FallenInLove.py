c = int(input("N:"))
koloni = 4*c + 6
redove = 3*c + 1
help1=int((koloni-6)/2)
#1-ви ред
print("#"*2, end = "")
print("."*help1, end="")
print("#"*2, end = "")
print("."*help1, end="")
print("#"*2, end = "")
print()
#първи патерн
for i in range(1,c):
    print("#",end="")
    print("~"*i, end="")
    print("#", end="")
    print("."*(help1-2*i),end="")
    print("#", end="")
    print("."*(2*i),end="")
    print("#", end="")
    print("." * (help1 - 2*i), end="")
    print("#", end="")
    print("~" * i, end="")
    print("#", end="")
    print()
#2-ри патерн
for i in range (1,c+1):
    help2 = 2*i-1
    print("."*help2,end="")
    print("#", end="")
    print("~" * ((c+1)-i), end="")
    print("#", end="")
    print("."*(help1+2-2*i),end = "")
    print("#", end="")
    print("~" * ((c + 1) - i), end="")
    print("#", end="")
    print("."*help2, end="")
    print()
print("."*(help1+1),end="")
print("#"*4,end="")
print("."*(help1+1),end="")
print()
for i in range(1,c+1):
    print("." * (help1 + 2), end="")
    print("#" * 2, end="")
    print("." * (help1 + 2), end="")
    print()







