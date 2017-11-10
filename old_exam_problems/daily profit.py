wMonths=int(input())
moneyIn=float(input())
usdBg=float(input())
totalMoney=(14.5*wMonths*moneyIn)*0.75
totalMoneyBg=usdBg*totalMoney/365
print("{0:.2f}".format(totalMoneyBg))
