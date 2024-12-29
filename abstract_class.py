# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from dataclasses import dataclass
import math

@dataclass
class Owner:
    name: str
    age: int
    gender: str
     
class Animal(ABC): # super class
    
    static_counter = 0
    
    def __init__(self):
        Animal.static_counter += 1
        self._owner = Owner("nature", math.inf, "no_gender") # protected class variable

    @abstractmethod
    def walk(self): pass

    @abstractmethod
    def eat(self): pass

    @abstractmethod
    def speak(self): pass

    @staticmethod
    def print_count():
        print(f"Number of created animal is {Animal.static_counter}")

    def run(self): pass

    def  __call__(self)->str:
        return "we are derived from Animal class."
    
    def toString(self): # Override from object class
        return "You called Animal override method toString method."
    def __str__(self):
        return "You called Animal override method str method."
    

class Bird(Animal): # sub class
    
    def __init__(self, name, owner: Owner):
        super().__init__()
        self.name = name
        if(owner != None):
            self._owner =  owner
        if(name != None):
            print(f"bird with name : {name}, owner: {self._owner}")
        else:
            print(f"bird is created. owner: {self._owner}")
     
    def walk(self): 
        print("flutter")

    def eat(self): 
        print("worm")

    def speak(self): 
        print("cik cik")
        
    def toString(self):
        return "You called Bird Overriding toString method."

class Cat(Animal): # sub class

    def __init__(self, name, owner: Owner):
        super().__init__()
        self.name = name
        if(owner != None):
            self._owner = owner
        if(name != None):
            print(f"cat with name : {name},  owner: {self._owner}")
        else:
            print(f"cat is created.  owner: {self._owner}")
        
    def walk(self): 
        print("paw_paw")

    def eat(self): 
        print("cat food")

    def speak(self): 
        print("meow meow")
    
    def run(self):
        print("cat is running")
    """def toString(self): # Cat to string comes from parent class inhereted.
        pass"""

owner_zeliha = Owner("Zeliha", math.inf, "Woman")


b1 = Bird(None, None)
b2 = Bird("cicikus", owner_zeliha)
c1 = Cat(None, None)
c2 = Cat("boncuk", owner_zeliha)
c3 = Cat("minnos", None)

Animal.print_count()
print(f"Message from cat object : {b1()}")
print("Message from bird object :", c1())

print("**************************")
b1.eat()
b2.walk()
c1.eat()
c2.run()
c2.speak()
c3.speak()
print("**************************")
print(b1.toString()) # overrided from Animal which overrides from object class
print(c1.__str__()) # comes from Animal overrided str method from Object class
print("**************************")
print("Show Cat class methods: ", Cat.__dict__, "\n\n")
print("Show cat object variables: ",c1.__dict__)


