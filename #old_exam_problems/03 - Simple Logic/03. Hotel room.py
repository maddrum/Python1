month = input().lower()
n = int(input())

if month in("may", "october"):
    studio = n*50
    app = n*65
    if n in range(8,15):
        studio = studio*0.95
    elif n >14:
        studio = studio*0.70
elif month in ("june", "september"):
    studio=75.20*n
    app=68.70*n
    if n>14:
        studio = studio*0.8
else:
    studio = 76*n
    app=77*n

if n>14:
    app=0.9*app

print("Apartment: "+"{0:.2f}".format(app)+" lv.")
print("Studio: "+"{0:.2f}".format(studio)+" lv.")

