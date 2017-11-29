checkerOdd=0
while checkerOdd==0:
   n = input()
   try:
      k = float(n)
   except:
      n = input()
   if k%1==0 and k%2==0:
      checkerOdd=1

print("Even number entered: {}".format(int(n)))
