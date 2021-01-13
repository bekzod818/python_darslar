class Trail():
    def __init__(self, dest, len = 0):
        self.dest = dest
        self.len = len
    def describe_trail(self):
        desc = f"This trail goes to {self.dest}."
        if self.len:
            desc += f"\nThe trail is {self.len}km."
        print(desc)
    def run_trail(self):
        print(f"Running to {self.dest}.")

class Bike_Trail(Trail):
    def __init__(self, dest, len = 0):
        super().__init__(dest, len)
        self.paved = True
        self.bikes_only = True
    def ride_trail(self):
        print(f"Riding to {self.dest}")
    def run_trail(self):
        if self.bikes_only:
            print("You can't run this trail!")
        else:
            super().run_trail()

verst = Trail("Mt. Verstovia", 4)
verst.describe_trail()
verst.run_trail()
print("-" * 25)

ms = Trail("Middle Sister", 10)
ms.describe_trail()
ms.run_trail()
print("-" * 25)

cross = Bike_Trail('Harbor Mountain', 5)
cross.ride_trail()
cross.describe_trail()
cross.run_trail()