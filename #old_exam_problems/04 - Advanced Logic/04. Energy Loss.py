n=int(input())
a=int(input())
sum=0
for i in range(1,n+1):
    j=int(input())
    if i%2==0 and j%2==0:
        sum+=68*a
    elif i%2!=0 and j%2==0:
        sum+=49*a
    elif i%2==0 and j%2!=0:
        sum+=65*a
    else:
        sum+=30*a

energy=(100*a*n-sum)/n/a
if energy <=50:
    print("They are wasted! Energy left: {0:.2f}".format(energy))
else:
    print("They feel good! Energy left: {0:.2f}".format(energy))

