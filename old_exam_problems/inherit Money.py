inherit=float(input())
inherit1=inherit
year=int(input())
delta=year-1800
for i in range(0,delta+1):
    if i%2 ==0:
        inherit1-=12000
    else:
        inherit1-=(12000+50*(18+i))

if inherit1>=0:
    print("Yes! He will live a carefree life and will have {0:.2f} dollars left.".format(inherit1))
else:
    print("He will need {0:.2f} dollars to survive.".format(abs(inherit1)))

