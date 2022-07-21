#Creatiing a Class called class
class Car:
#Using Class Constructor and giving Class Car It's attributes
    def __init__(self,name,color,tires,seats,doors):
        self.name = name
        self.color = color
        self.tires = tires
        self.seats = seats
        self.doors = doors
##Giving methods 
    def drive_car(self):
        print("Vrooom! Vrooom!! Vrooom!!!")

    def brake_car(self):
        print("You are approaching a dead end,Hit the brake pedal now!")
     
    def refuel_car(self):
        print("You are on Reserve,Stop at the nearest filling station for refueling")

    def openclosedoors_car(self):
        print("Here is a trick, Press a button on the door area to automatically close and open doors!")

    def park_car(self):
        print("You have reached your destination, Park your car at the parking lot.")



        
#first car
first_car = Car(name='Toyota', color='Black', tires=4, seats='four-seat Capacity', doors=4)

print(first_car.name)
print(first_car.color)
print(first_car.tires)
print(first_car.seats)
print(first_car.doors)

#Calling Methods
first_car.drive_car()
first_car.brake_car()
first_car.refuel_car()
first_car.openclosedoors_car()
first_car.park_car()

#second car
second_car = Car(name='Tesla', color='Grey', tires=4, seats='four-seat Capacity', doors=4)

print(second_car.name)
print(second_car.color)
print(second_car.tires)
print(second_car.seats)
print(second_car.doors)

#Calling Methods
second_car.drive_car()
second_car.brake_car()
second_car.refuel_car()
second_car.openclosedoors_car()
second_car.park_car()
