class Animal(object):
    pass

## Dog is-a Animal
class Dog(Animal):
    
    def __init__(self, name):
        ## name has-a object
        self.name = name


## Cat is-a Animal
class Cat(Animal):
    
    def __init__(self, name):
        ## name has-a object
        self.name = name
        
## Person has-a object
class Person(object):
    
    def __init__(self, name):
        
        self.name = name
        
        ## Person has-a pet of some kind
        self.pet = None
        
## Employee is-a person
class Employee(Person):
    
    def __init__(self, name, salary):
        ## hmm what is this strange magic? multpile inheritance - stay away from this!
        super(Employee, self).__init__(name)
        
        self.salary = salary


## Fish has-a object
class Fish(object):
    pass

## Salmon is-a fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is a cat
satan = Cat("Satan")

## Mary is a person
mary = Person("Mary")

## Mary has-a pet

mary.pet = satan

## Frank is-a Employee
frank = Employee("Frank", 120000)

## Frank has-a pet
frank.pet = rover

## A fish has a flipper
flipper = Fish()

## Crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()
