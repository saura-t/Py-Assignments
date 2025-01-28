'''Single Inheritance'''
class PremierLeague:
    def __init__(self, name):
        self.name = name
    
    def rank(self):
        return f"{self.name} Not in Premier League"

class Team(PremierLeague):
    def rank(self, position):
        return f"Rank of {self.name} is {position}"

'''Multiple Inheritance'''
class Swimmer:
    def swim(self):
        return "Swimming"

class Runner:
    def run(self):
        return "Running"

class Cyclist:
    def cycle(self):
        return "Cycling"
    
class triAthlete(Swimmer, Runner, Cyclist):
    def compete(self):
        return f"Triathlon includes: {self.swim()}, {self.cycle()} and {self.run()}"

'''Multilevel Inheritance'''
class Vehicle:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        return "Vehicle started"

class Car(Vehicle):
    def __init__(self, engine, num_doors):
        super().__init__(engine)
        self.num_doors = num_doors
    
    def drive(self):
        return "Car driving"

class ElectricCar(Car):
    def __init__(self, engine, num_doors, battery_capacity):
        super().__init__(engine, num_doors)
        self.battery_capacity = battery_capacity

    def charge(self):
        return "Electric car charging"

#Example usage
league = PremierLeague("Real Madrid")
team = Team("Manchester City")
print(league.rank())
print(team.rank(6))

athlete = triAthlete()
print(athlete.compete())

vehicle = Vehicle("Gasoline")
car = Car("Gasoline", 4)
electric_car = ElectricCar("Electric", 4, "100 kWh")
print(vehicle.start())
print(car.drive())
print(electric_car.charge())