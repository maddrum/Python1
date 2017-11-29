smallest=float(input())
kitchen=float(input())
price=float(input())
bath=0.5*smallest
second=1.1*smallest
third=1.1*second
total=(smallest+kitchen+bath+second+third)*1.05
print("{:g}".format(total*price))
print(total*price)


