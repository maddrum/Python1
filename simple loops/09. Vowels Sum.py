inputStr=input()
sum=0
a=len(str(inputStr))
for i in inputStr: #range(0,a):
    if i == "a":
        sum = sum+1
    elif i == "e":
        sum=sum+2
    elif i =="i":
        sum=sum+3
    elif i == "o":
        sum=sum+4
    elif i == "u":
        sum = sum+5
print(sum)
