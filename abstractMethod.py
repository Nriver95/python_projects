
from abc import ABC, abstractmethod     #imports the abstract based class in order to create abstract classes and abstract methods

class Vehicle(ABC): #creates a class that will be an abstract based class

    @abstractmethod #creates an abstract method. This method is told to do something but with no instructions on how or what to do.
    def go(self):
        pass        #so we pass it without any arguments or instructions

class Car(Vehicle): #child class of Vehicle. This class will use the declared method "go()"

    def go(self):   #by defining what go does the class Car can now become an instantiate with the inherited method 
        print("this is a car")

class Motorcycle(Vehicle):

    def go(self):
        print("this is a motorcycle")

#vehicle = Vehicle()   #if you were to try and created an instance of vehicle it would not work because it is an abstract class containing an abstract method
car = Car()     #here we are stating that the variable car is equal to the class "Car()"
motorcycle = Motorcycle()


car.go()    #here we are calling the go() method from the class Car() using the variable "car"
motorcycle.go() #same here but with the class Motorcycle()
