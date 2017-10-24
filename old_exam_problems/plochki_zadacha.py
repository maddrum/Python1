N=int(input())
W=float(input())
L=float(input())
M=int(input())
O=int(input())

area = N*N
benchArea = M*O
totalArea = area - benchArea
plateArea = W*L
neededPlate = (totalArea/plateArea)
neededTime = round((neededPlate*.2),2)

print(neededPlate)
print(neededTime)
