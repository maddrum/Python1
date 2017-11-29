n = int(input())
l = int(input())
a=ord("a")

for i in range(1,n):
    for j in range(1,n):
        first=str(i)+str(j)
        for k in range(0,l):
            for x in range (0,l):
                firstLetter=chr(a+k)
                secondLetter=chr(a+x)
                second=firstLetter+secondLetter
                if j>=i:
                    f=j
                else:
                    f=i
                for r in range(1,n-f+1):
                    third = str(r+f)
                    print(first + second + third, end=" ")
