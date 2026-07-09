from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class car(Vehicle):
    def start(self):
        print("Car starts with a key")

car1 = car()
car1. start()