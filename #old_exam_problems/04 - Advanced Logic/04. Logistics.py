n=int(input())
bus=0
truck=0
train=0
sum=0
for i in range(0,n):
    t=int(input())
    sum+=t
    if t<4:
        bus+=t
    elif t<12:
        truck+=t
    else:
        train+=t
mean=(bus*200+truck*175+train*120)/sum
print("{0:.2f}".format(mean))
print("{0:.2f}%".format(bus/sum*100))
print("{0:.2f}%".format(truck/sum*100))
print("{0:.2f}%".format(train/sum*100))

