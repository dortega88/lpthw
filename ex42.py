# Go through the code and replace ##?? comment with a comment that says either is-a or has-a relationship.
### Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a Animal
class Dog(Animal):

    def __init__(self,name):
        ## Dog has-a attribute name
        self.name = name

## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a attribute name
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## Person has-a attribute name
        self.name = name

        ## Person has-a pet
        self.pet = None

## Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## Employee has-a name
        super(Employee, self).__init__(name)
        ## Employee has-a salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass


## Rover is-a Dog
rover = Dog("Rover")

## Satan is-a Cat
satan = Cat("Satan")

## Mary is-a Person
mary = Person("Mary")

## Mary has-a pet named satan?
mary.pet = satan

## Frank is-a employee
frank = Employee("Frank", 120000)

## Frank has-a pet Rover
frank.pet = rover

## Flipper is-a Fish
flipper = Fish()

## Crouse is-a Salmon
crouse = Salmon()

## Harry is-a Halibut
harry = Halibut()
