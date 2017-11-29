import math
step=int(input())
dancer=int(input())
days=int(input())
daySteps=math.ceil((step/days)/step*100)
dancerSteps=daySteps/dancer
if daySteps<=13:
    print("Yes, they will succeed in that goal! {0:.2f}%.".format(dancerSteps))
else:
    print("No, They will not succeed in that goal! Required {0:.2f}% steps to be learned per day.".format(dancerSteps))