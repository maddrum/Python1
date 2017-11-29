speed=float(input())
exitStatemets = ["slow", "average", "fast", "ultra fast", "extremely fast"]
if speed <= 10:
    print(exitStatemets[0])
elif speed >10 and speed <= 50:
    print(exitStatemets[1])
elif speed > 50 and speed<=150:
    print(exitStatemets[2])
elif speed > 150 and speed <=1000:
    print(exitStatemets[3])
else:
    print(exitStatemets[4])
