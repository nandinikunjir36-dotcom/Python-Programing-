#class vehicle:
class Vehicle:
    def __init__(self):
        print("The vehicle is moving")
         
#Subclass Car
class Car(Vehicle):
    def move (self):
        print("Driving on road")


#Subclass Bicycle 
class Bicycle(Vehicle):
    def move(self):
        print("Pedaling on road")


#DDemonstrating polymorphism
Vehicle=[Car(),Bicycle()]

for v in Vehicle:
    v.move()


