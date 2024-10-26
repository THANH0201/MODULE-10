

class elevator():
    def __init__(self, bottom, top):
#        self.name = name
        self.bottom_floor = bottom
        self.top_floor = top
        self.current_floor = self.bottom_floor


    def go_to_floor(self,floor):

#        while True:
#            floor = int(input(" The floor you want to go to: "))
        # make sure you don't go through the roof or ground
            if floor > self.top_floor or floor < self.bottom_floor:
                print("not a valid floor")
            elif floor < self.current_floor:
                for i in range (floor, self.current_floor):
                    if not self.floor_down():
                        break
            elif floor > self.current_floor:
                for i in range (self.current_floor, floor):
                    if not self.floor_up():
                        break
            else: print(f" The elevation is right here.")
            #elevator will go down bottom after go to the target floor
            print("ting, this is your floor")
#            for i in range(self.bottom_floor, self.current_floor):
#                self.floor_down()



    def floor_up(self):
        # go up one floor
        if self.current_floor < self.top_floor:
            self.current_floor = self.current_floor + 1
        # print current floor
            print(f" The elevator is up to floor {self.current_floor}")
            return True
        else:
            return False

    def floor_down(self):
        # go down one floor
        if self.current_floor > self.bottom_floor:
            self.current_floor = self.current_floor - 1
            # print current floor
            print(f" The elevator is down to floor {self.current_floor}")
            return True
        else:
            return False



