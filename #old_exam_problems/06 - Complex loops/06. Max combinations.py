x=int(input())
y=int(input())
stop=int(input())
delta=y-x
checker=0
for i in range(x,y+1):
    for j in range(x,y+1):
        print("<{}-{}>".format(i,j),end="")
        checker+=1
        if checker==stop:
            exit()