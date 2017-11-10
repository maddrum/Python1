p1=int(input())
p2=int(input())
battle=int(input())
count=0
for i in range(1,p1+1):
    for j in range(1,p2+1):
        if count ==battle:
            exit()
        else:
            print("({} <-> {})".format(i,j),end=" ")
            count+=1

