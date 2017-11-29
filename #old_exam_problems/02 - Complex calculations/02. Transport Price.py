def taxi(n,time):
    if time =="day":
        trip=0.70+n*0.79
    else:
        trip=0.70+n*0.90
    return trip;

def bus(n):
    trip = 0.09*n
    return trip;
def train(n):
    trip = 0.06*n
    return trip;


n=float(input())
time = input()

if n<20:
    trip = taxi(n,time)
    print(trip)
elif n>=20 and n <100:
    trip = bus(n)
    print(trip)
else:
    trip = train(n)
    print(trip)

