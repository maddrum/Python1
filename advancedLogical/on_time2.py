examHour=int(input())
examMin=int(input())
arrHour=int(input())
arrMin=int(input())
examTotalMin=examHour*60+examMin
arrTotalMin=arrHour*60+arrMin
diff=examTotalMin-arrTotalMin
hour = abs(diff) // 60
if diff>=0:
    minute = diff - hour * 60
else:
    minute = abs(hour*60+diff)
if examTotalMin-arrTotalMin == 0:
    print("On time")
if examTotalMin<arrTotalMin:
    print("Late")
    if hour>0:
        print("{}:{:02} hours after the start".format(hour, minute))
    else:
        print("{} minutes after the start".format(minute))
if examTotalMin>arrTotalMin:
    if minute<=30 and hour==0:
        print("On time")
        print("{} minutes before the start".format(minute))
    elif hour >0:
        print("Early")
        print("{}:{:02} hours before the start".format(hour, minute))
    else :
        print("Early")
        print("{} minutes before the start".format(minute))

