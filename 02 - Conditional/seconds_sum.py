a = int(input())
b = int(input())
c = int(input())

secondsSum = a + b +c

minutes = secondsSum //60
seconds = secondsSum - minutes*60

if seconds < 10:
    result = str(minutes)+ ":0" +str(seconds)
else:
    result = str(minutes) + ":" + str(seconds)

print(result)
