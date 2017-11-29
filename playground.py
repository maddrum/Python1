class animal:
    name=0
    gender=0
    age=0
    type=0
    def __init__(self,name,age,gender):
        animal.name=name
        animal.gender=gender
        animal.age=age
        animal.type=type
    def infoPrint(self):
        print("{} is a {} {} aged {} years".format(animal.name, animal.gender, animal.type, animal.age))
class cats(animal):
    animal.type= "cat"
class dogs(animal):
    animal.type="dog"
class parrot():
    animal.type="parrot"

name=input("name:")
age=int(input("age:"))
gender=input("gender:")
type=input("type:")
if type=="dog":
    etc=dogs(name, age, gender)
    print(etc.infoPrint())
if type=="cat":
    etc=cats(name,age,gender)
    print(etc.infoPrint())




