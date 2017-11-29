x1=input().lower()
x2=input().lower()
x3=input().lower()
x1Num=ord(x1)
x2Num=ord(x2)
x3Num=ord(x3)
count=0

for i in range(x1Num,x2Num+1):
    if i == x3Num:
        continue
    for j in range(x1Num,x2Num+1):
        if j == x3Num:
            continue
        for k in range(x1Num,x2Num+1):
            if k == x3Num:
                continue
            print(chr(i)+chr(j)+chr(k), end=" ")
            count+=1
print(count)