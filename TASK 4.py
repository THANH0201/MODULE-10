import random
from tabulate import tabulate


class Car:
    def __init__(self,reg_num, max_speed):
        self.registration_number = reg_num
        self.maximum_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

# Change speed
    def accelerate(self,speed_change):
        self.current_speed = speed_change
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        if self.current_speed < 0:
            self.current_speed = 0

#time drive
    def drive(self, time):
        self.travelled_distance += round((self.current_speed * time)) #(d=v.t)


class Race:
    def __init__(self, name,distance,cars):
        self.name = name
        self.cars = cars
        self.distance = distance

    def hour_passed(self):
        for car in self.cars:
            car.accelerate(random.randint(-15,10))
            car.drive(1.)

    def print_status(self):

        car_data2 = []
        for car in cars:
            car_data2.append([car.registration_number, car.maximum_speed, car.travelled_distance])

        headers = ["Registration_number", "Maximum_speed(km/h)", "Travelled_distance(km)"]
        print(tabulate(car_data2, headers=headers, tablefmt="grid", ))

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
            return False

cars = []
for i in range(10):
    cars.append(Car("ABC-" + str(i + 1), random.randint(100,200)))
race = Race("2024 RACE",8000.,cars)
#START
car_data1 = []
for car in cars:
    car_data1.append([car.registration_number,car.maximum_speed])
print(race.name)
print("THE LIST OF CAR:")
headers = ["Registration_number", "Maximum_speed(km/h)"]
print(tabulate(car_data1, headers=headers, tablefmt="grid", ))

#RESULT
n = 0
while not race.race_finished():
    race.hour_passed()
    n = n + 1
    if n%100 == 0:
        print(race.name)
        print(f"AFTER {n} hours")
        race.print_status()
#FINISH
print(race.name)
print(f"THE FINAL RESULTS AFTER {n} hours:")
race.print_status()




