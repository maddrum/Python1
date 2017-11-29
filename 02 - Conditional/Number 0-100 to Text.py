a = int(input())
b=a//10
c=a%10
array10=["zero", "one","two","three","four","five","six","seven","eight","nine"]
array20=["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
array30=[0,0,"twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

if a >=0 and a <=100:
    if a in range(0,9):
        print(array10[a])
    elif a in range(10,20):
        print(array20[a-10])
    elif a == 100:
        print("one hundred")
    elif a % 10 == 0:
        print(array30[b])
    else:
        print(str(array30[b])+" "+str(array10[c]))

else:
    print("invalid number")
