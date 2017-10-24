hour=int(input())
minute=int(input())

minuteCheck=minute+15
if minuteCheck > 59:
    hour = hour +1
    if hour == 24:
        hour = 0
    resultMinute = minuteCheck - 60
    if resultMinute // 10 == 0:
        print(str(hour)+":0"+str(resultMinute))
    else:
        print(str(hour)+":"+str(resultMinute))

else:
    resultMinute = minuteCheck
    if resultMinute // 10 == 0:
        print(str(hour)+":0"+str(resultMinute))
    else:
        print(str(hour)+":"+str(resultMinute))

