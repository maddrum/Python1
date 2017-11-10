n=int(input())
c=n//2
tire=2*n-(c+2)*2
for i in range(0,n):
    if i ==0:
        print("/"+"^"*c+"\\"+"_"*tire+"/"+"^"*c+"\\")
    elif i==n-2:
        print("|"+" "*(c+1)+"_"*tire+" "*(c+1)+"|")
    elif i==n-1:
        print("\\"+"_"*c+"/"+" "*tire+"\\"+"_"*c+"/")
    else:
        print("|"+" "*(2*n-2)+"|")
