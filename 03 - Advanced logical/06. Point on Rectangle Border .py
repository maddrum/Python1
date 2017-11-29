x1=float(input())
y1=float(input())
x2=float(input())
y2=float(input())
x=float(input())
y=float(input())
checker = "Inside / Outside"
if x>=x1 and x <= x2:
    if y>=y1 and y<=y2:
        if x in (x1, x2) or y in (y1, y2):
            checker = "Border"
    else:
        checker = "Inside / Outside"

print(checker)
