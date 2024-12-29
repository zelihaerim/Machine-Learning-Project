#%% Write class
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from dataclasses import dataclass
import math

@dataclass
class Owner:
    name: str
    age: int
    gender: str

animal_list = []

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
    
    def _insert_animal_list(self):
        animal_list.append(self)
        

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
        self._insert_animal_list()
        
    
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
        self._insert_animal_list()
        
    def walk(self): 
        print("paw_paw")

    def eat(self): 
        print("cat food")

    def speak(self): 
        print("meow meow")
    
    def run(self):
        print("cat is running")
    def toString(self):
        return "You called Cat Overriding toString method."

owner_zeliha = Owner("Zeliha", math.inf, "Woman")

#%% Run Program
b1 = Bird(None, None)
b2 = Bird("cicikus", owner_zeliha)
c1 = Cat(None, None)
c2 = Cat("boncuk", owner_zeliha)
c3 = Cat("minnos", None)

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

print("--------------------------------")
print("Num of created object from static method: ")
Animal.print_count()
print(f"Num of created object from global variable: {len(animal_list)}")

for i in animal_list:
    print(i.toString())

"""
-> Output:
bird is created. owner: Owner(name='nature', age=inf, gender='no_gender')
bird with name : cicikus, owner: Owner(name='Zeliha', age=inf, gender='Woman')
cat is created.  owner: Owner(name='nature', age=inf, gender='no_gender')
cat with name : boncuk,  owner: Owner(name='Zeliha', age=inf, gender='Woman')
cat with name : minnos,  owner: Owner(name='nature', age=inf, gender='no_gender')
Message from cat object : we are derived from Animal class.
Message from bird object : we are derived from Animal class.
**************************
worm
flutter
cat food
cat is running
meow meow
meow meow
**************************
You called Bird Overriding toString method.
You called Animal override method str method.
**************************
Show Cat class methods:  {'__module__': '__main__', '__init__': <function Cat.__init__ at memory_address>, 'walk': <function Cat.walk at memory_address>, 'eat': <function Cat.eat at memory_address>, 'speak': <function Cat.speak at memory_address>, 'run': <function Cat.run at memory_address>, 'toString': <function Cat.toString at memory_address>, '__doc__': None, '__abstractmethods__': frozenset(), '_abc_impl': <_abc._abc_data object at memory_address>} 


Show cat object variables:  {'_owner': Owner(name='nature', age=inf, gender='no_gender'), 'name': None}
--------------------------------
Num of created object from static method: 
Number of created animal is 5
Num of created object from global variable: 5
You called Bird Overriding toString method.
You called Bird Overriding toString method.
You called Cat Overriding toString method.
You called Cat Overriding toString method.
You called Cat Overriding toString method.
"""
