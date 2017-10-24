points = int(input())

if points <= 100:
    bonusPoints = 5
elif points >100 and points <=1000:
    bonusPoints = points*0.2
else:
    bonusPoints = 0.1*points
checker = points %2
checker5 = points %5
checker10 = points %10

if checker ==0:
    bonusPoints = bonusPoints+1

if checker5 ==0 and checker10 !=0:
    bonusPoints = bonusPoints +2

print(bonusPoints)
totalPoints = bonusPoints+points
print(totalPoints)
