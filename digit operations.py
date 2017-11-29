N1=int(input())
N2=int(input())
opp=input()
if  N2==0:
    if opp in ("/", "%"):
        print("Cannot divide {} by zero".format(N1))
        exit()
if opp in("+","-","*"):
    if opp =="+":
        result = N1+N2
    elif opp=="-":
        result = N1-N2
    else:
        result = N1*N2
    if result%2==0:
        check = "even"
    else:
        check = "odd"
    print("{} {} {} = {} - {}".format(N1, opp, N2, result, check))
if opp == "/":
    result = N1/N2
    print("{} / {} = ".format(N1,N2)+"{0:.2f}".format(result))
if opp == "%":
    result = N1%N2
    print("{} % {} = {}".format(N1,N2,result))