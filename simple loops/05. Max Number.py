n = int(input())
numbers=[]
min =0
for i in range(0,n):
    num = int(input())
    if i ==0:
        min=num
    elif num>min:
        min=num

print(min)

