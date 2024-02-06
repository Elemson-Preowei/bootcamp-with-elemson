class Vehicle:
    def __init__(self, type, engine_num, colour):
        self.type = type
        self.engine_num = engine_num
        self.colour = colour 
        self.mileage = 0

    def drive(self, speed):
        if speed < 20:
            return False
        else:
          #  self.mileage = speed * 3
            return True        

    def reverse(self):
        self.mileage -= 1    

class Car(Vehicle):
    def __init__(self, type, engine_num, colour, door):
        super().__init__(type, engine_num, colour)
        self.door = door

    def front_wheel(self, speed):
        movement = super().drive(speed)
        if movement:
            self.mileage = speed * 3
        return movement         

test = Car("Toyota", 2233, "Red", 4)
print(test.type)

print(test.front_wheel(40))

print(test.mileage)