n=int(input())
doctor=7
treated=0
untreated=0
for i in range(1,n+1):
    p=int(input())
    if i%3==0 and treated<untreated:
        doctor+=1
    if p>=doctor:
        treated+=doctor
        untreated+=(p-doctor)
    else:
        treated+=p
print("Treated patients: {}.".format(treated))
print("Untreated patients: {}.".format(untreated))

