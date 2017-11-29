import datetime

dateInput=input()

day=int(dateInput[:2])
month=int(dateInput[3:5])
year=int(dateInput[-4:])


date1 = datetime.date(year, month, day)
date2=str(date1 - datetime.timedelta(days=-999))
print(date2[-2:]+"-"+date2[5:7]+"-"+date2[:4])



