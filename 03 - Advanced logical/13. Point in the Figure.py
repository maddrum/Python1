h=int(input())
x=int(input())
y=int(input())

result = "outside"

if x>=0 and x<h and y>=0 and y<=h:
    result = "inside"
if x>=h and x<=2*h and y>=0 and y<=h*4:
    result ="inside"
if x>(2*h) and x<=(3*h) and y>=0 and y<=h:
    result = "inside"

if result == "inside":

    if x==0:
       result ="border"
    if y == 0:
        result = "border"
    if x>0 and x<h and y == h:
        result = "border"
    if x == h and y>=h:
        result = "border"
    if x>h and x<2*h and y == 4*h:
        result = "border"
    if x==2*h and y>=h:
        result = "border"
    if x>2*h and x <3*h and y==h:
        result = "border"
    if x==3*h:
        result = "border"

print(result)
