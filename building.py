from elevator import elevator


class building():
    def __init__(self, bottom, top, elevators):
        self.bottom_floor = bottom
        self.top_floor = top
        self.num_of_elevators = elevators
        self.elevators = []
        for i in range(self.num_of_elevators):
            self.elevators.append(elevator( self.bottom_floor, self.top_floor))

    def run_elevators(self,elevator_num,floor):
#        elevator_num = int(input("Choose the number of elevator: "))
            print(f" Elevator {elevator_num} is moving")
            self.elevators[elevator_num - 1].go_to_floor(floor)

    def fire_alarm(self):
        print("THE FIRE ALARM IS RINGING")
        for e in self.elevators:
            e.go_to_floor(e.bottom_floor)




