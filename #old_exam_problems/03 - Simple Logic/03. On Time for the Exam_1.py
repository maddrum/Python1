examHour=int(input())
examMin=int(input())
arrHour=int(input())
arrMin=int(input())
hour=examHour-arrHour
if arrMin-examMin >=0:

    minute=arrMin-examMin
else:
    minute=examMin-arrMin
minuteCheck = 60+examMin-arrMin
minuteCheckLate = 60-examMin+arrMin

if hour ==0 and minute ==0:
    print("On time")
if hour==0 and arrMin>examMin:
    print("Late")
    print("{} minutes after the start".format(minute))
if hour==0 and arrMin<examMin:
    print("on time")
    print("{} minutes before the start".format(minute))

if hour == -1 and minuteCheckLate>59:
    print("Late")
    print("{}:{:02} hours after the start".format(abs(hour), minute))
if hour == -1 and minuteCheckLate<59:
    print("Late")
    print("{} minutes after the start".format(minute))
if hour == -1 and minuteCheckLate==59:
    print("Late")
    print("{} minutes after the start".format(minuteCheckLate))
if hour<-1 and minuteCheckLate>59:
    print("Late")
    print("{}:{:02} hours after the start".format(abs(hour), minute))

if hour <-1 and minuteCheckLate<=59:
    print("Late")
    print("{}:{:02} hours after the start".format(abs(hour+1), minuteCheckLate))

if hour >1 and minuteCheck>59:
   print("Early")
   print("{}:{:02} hours before the start".format(hour,minute))
if hour>1 and minuteCheck<=59:
    print("Early")
    print("{}:{:02} hours before the start".format((hour-1), minuteCheck))
if hour==1 and minuteCheck<=59:
    if minuteCheck<=30:
        print("on time")
        print("{} minutes before the start".format(minuteCheck))
    else:
        print("Early")
        print("{} minutes before the start".format(minuteCheck))
elif hour==1 and (60+examMin-arrMin)>59:
    print("Early")
    print("{}:{:02} hours before the start".format(hour, minute))





