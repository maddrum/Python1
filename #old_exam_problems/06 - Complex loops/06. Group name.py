letter1=input()
letter2=input()
letter3=input()
letter4=input()
number=int(input())
l1Num=ord(letter1)
l2Num=ord(letter2)
l3Num=ord(letter3)
l4Num=ord(letter4)
checker=0
for i in range(ord("A"),l1Num+1):
    for j in range(ord("a"),l2Num+1):
        for k in range(ord("a"),l3Num+1):
            for l in range(ord("a"),l4Num+1):
                for m in range(0,number+1):
                    checker+=1
print(checker-1)
