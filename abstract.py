from abc import*

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod

    def stop(self):
        pass

class vehicle(Vehicle):

    def go(self):
        print("goooo")

    def stop(self):
        print("stopppp")

car = vehicle()

car.go()
car.stop()
