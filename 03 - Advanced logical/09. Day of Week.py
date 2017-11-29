day=int(input())
if day not in range(1,8):
    print("Error")
    exit()
daysOfWeek=("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print(daysOfWeek[day-1])
