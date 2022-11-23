class Car:
    def __init__(self):
        self.speed = 0
        self.isMoving = False
        self.color = "red"

    def setSpeed(self, newSpeed):
        self.speed = newSpeed
        if self.speed != 0:
            self.isMoving = True
        else: 
            self.isMoving = False

    def stopCar(self):
        if self.speed == 0: 
            pass
        else:
            self.isMoving = False 
            self.speed = 0

    def gradualStop(self):
        while abs(self.speed) != 0: 
            if self.speed > 0:     
                self.speed = self.speed - 1
            else: 
                self.speed = self.speed + 1 
            if self.speed == 0: 
                self.isMoving = False
            print(self.speed,self.isMoving)
    
    def gradualAccel(self, target): 
        while self.speed != target: 
            if self.speed > target: 
                self.speed = self.speed - 1 
            else: 
                self.speed = self.speed + 1 
            print(self.speed, target)

    def setColor(self, color):
        self.color = color
            
    def __str__(self):
        return "speed: " + str(self.speed) + " isMoving: " + str(self.isMoving) + " color: " + str(self.color)


green_car = Car()
print(green_car)

green_car.setSpeed(-10)
print(green_car)

green_car.gradualStop()
print(green_car)

green_car.gradualAccel(10)
print(green_car)

# green_car.setSpeed(5)
# print(green_car)

# green_car.setSpeed(3)
# print(green_car)

# green_car.setColor("green")
# print(green_car)

# green_car.stopCar()
# print(green_car) 




