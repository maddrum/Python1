hDays=int(input())
workDays=int(365-hDays)
minutesPlay=hDays*127+workDays*63
deltaTime=abs(minutesPlay-30000)
hour = deltaTime//60
minutes = deltaTime-60*hour
if minutesPlay>30000:
    print("Tom will run away")
    result = "{} hours and {} minutes more for play".format(hour,minutes)
else:
    print("Tom sleeps well")
    result="{} hours and {} minutes less for play".format(hour,minutes)
print(result)

