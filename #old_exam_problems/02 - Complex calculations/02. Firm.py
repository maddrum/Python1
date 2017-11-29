import math
neededHours=int(input())
days=int(input())
staff=int(input())

workHours=math.floor(0.9*days*8+staff*2*days)
check=neededHours-workHours
checkType=math.floor(check)
if check <=0:
    result="Yes!{} hours left.".format(abs(checkType))
else:
    result="Not enough time!{} hours needed.".format(checkType)
print(result)

