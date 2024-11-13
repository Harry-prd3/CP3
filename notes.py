# Classes

# We start classes with keyword class and we name them using PascalCase 
class Animal:
    
    # We start with the constructor (defines all the attribute of the object being created)
    def __init__(self, name, species, age, gender, rarity):
        
        # Do self.(argument) = argument to make it so we can use just the name of the argument as a variable instead of self.(argument) every time
        self.name = name
        self.species = species
        self.age = age
        self.gender = gender
        self.rarity = rarity
    
    # Methods are functions inside of the class!
    # This one returns the name of the one with the longest name 
    def fight(self, other):
        if len(self.name) > len(other.name):
            other.deaths += 1
            return self.name
        elif len(self.name) < len(other.name):
            self.deaths += 1
            return other.name
        else:
            other.deaths += 1
            self.deaths += 1
            return "they both died"

    def get_name(self):
        return self.name

    # Create a way to readably print our objects to show they exist
    def __str__(self):
        return f"\nName: {self.name}\nAge: {self.age}\nSpecies: {self.species}\nGender: {self.gender}\nRarity: {self.rarity}"

# Creating our object
# We generally store objects in variables (indibidually or in a list) so we can use it
cat = Animal("Tom", "meow meow", 21, "no thanks", "Epic")
frog = Animal("Jarrod", "Poisin Dart Frog", 500, "Feminane", "Legendary")


#print(cat)
#print(frog)

# Creating the new argument for the fuction deaths
#cat.deaths = 0
#frog.deaths = 0

# To call methods you put the name of the object.name of the method(arguments)
"""""
print("")
print(cat.fight(frog))
print(cat.deaths)
"""""

# Reasinging the name of the cat
cat.name = "Thomas"
"""""
print("")
print(cat.fight(frog))
print(cat.deaths)
print(frog.deaths)
"""""
# Deleating tom cause he is a stupid little baby
cat = None
# print(cat)




#Methods

class pokemon:
    def __init__(self, name, hp, typ, lvl):
        self.name = name
        self.hp = hp
        self.type = typ
        self.lvl = lvl
    
    def combat(self, other):
        if self.lvl > other.lvl:
            return(f"{self.name} yippee")
        elif self.lvl < other.lvl:
            return(f"aw {self.name} lost to {other.name}, hp is 0 now :(")
        else:
            return(f"both {self.name} and {other.name} dead. cry about it.")
    
    def __str__(self):
        return(f""" 
                Name: {self.name}
                Type : {self.type}
                Level: {self.lvl}
                HP: {self.hp}
""")
    
    # @classmethods make methods that can not affect instance variables of an object
    def lvl_up(self):
        self.lvl += 1
        self.hp = int(self.hp *1.5)

    @classmethod
    def pikachu(self):
        return(pokemon(input("give me a name: "), 50, "-eletric", -9999))
    
    #static methods do not require self or class
    def hp_update(poke):
        return poke.hp - 100




"""
eevee = pokemon("JayRod", 37, "normal", 2)
electivire = pokemon("bobsive", 1, "electric", 36.872)
pika = pokemon.pikachu()
"""
"""
print(eevee.lvl_up)
print(eevee)
pika.hp = pokemon.hp_update(pika)
print(pika)
"""

#UML diagrams
#what uml stand for
#the two different catagories
#the types of diagrams in those catagories
"""
Unified Modeling Language
the two cattagories are:structual diagrams and behavioral
stuctural has composit, depoyment, package, profile, object, and component
behavioral has activity, use, state, machine, interaction
interaction has sequence, communication, interaction overveiw, communication, and timming
"""
"""
the first par is the attrabutes (values)

the default value isnt requred, the data type is required
the + and the - at the start of the attribute shows if it is public or private
if there is a # instead it is protected and can not be changed
protected are visible for the class its in AND subclases

+ attribute1:type = defaultValue

ex 
__________________
| pokemon        |
|________________|
|+ public: string|
|- hp: int       |
|+ type: string  |
|+ rarity: string|
|+ level: int    |
|________________|

the second part of the diagram is the operations(methods)

this also has public and private + and -
they can have a return type which will be void if nothing is returned otherwise a var type

+ operation1(params):returnType

ex
_______________________
| pokemon             |
|_____________________|
|+ fight(other):string| 
|_____________________|


lines between classes are called relationships/ association
* means infinite (0...* is setting a range from 0 - infinity)
ittalics means abstract(implied class, kinda acts like a catagory for other classes, dont acctually make)
aggrigation is set with a solid diamon, assentually one class cant exist without the other

dependendcy, if one thing changes it does not affect the other, so event doesnt affect window
compositoin is if one thing dies then the other one dies
dependedncy and aggregation are different cause the boards could exist and not be open monitor
aggation can not exist without the other.
notes are recatnalges with a dog ear coner, they are just like comments
"""

#subclasses
class PetStore:
    name = "pet man place"
    def __init__(self, id_number):
        self.id_number = id_number
        self.animals = []
        self.featuredPet = None

    def addPet(self,animal):
        # isinstance checks if the fisrt value is the is an instance of the class as the second value 
        assert isinstance(animal, Animal)
        self.animals.append(animal)

    def removePet(self, animal):
        try:
            self.animals.remove(animal)
        except:
            print("No amicables")
        else:
            print(animal, " removed")
    
    def feature(self, name):
        for pet in self.animals:
            if pet.name == name:
                self.featuredPet = name
                pet("featured pet. . . ", name)
                break
        else:
            print("There is not a pet with that name :3")
    
    def getFeatured(self):
        return(self.featuredPet)
    
    def feed(self):
        for pet in self.animals:
            pet.eat()
    
    def getMammals(self):
        return self.getByType(Mammal)
    
    def getReptiles(self):
        return self.getByType(Reptile)
    
    def getByType(self, typ):
        return [pet for pet in self.animals if isinstance(pet, typ)]

class Animals :
    def __init__ (self,name):
        self.name = name
    
    def __str__(self):
        return(f"my name is: {self.name}")

    def eat(self):
        print(self.name, "eating", self.diet)

class Bird(Animals):
    pass

class pigdeon(Bird):
    diet = "street food"

class flamingo(Bird):
    diet = "shrimp"

class Amphibian(Animals):
    pass

class Frog(Amphibian):
    diet = "Flies"

class newt(Amphibian):
    diet = "worm"

class Fish(Animals):
    pass

class koi(Fish):
    diet = "algae"

class parana(Fish):
    diet = "human"

class Mammal(Animals):
    pass

class human(Mammal):
    diet = "idk man"

class Cat(Mammal):
    def __init__(self, name, diet):
        super().__init__(name)
        self.diet = diet
    diet = "jerry"

class Dog(Mammal):
    diet = "cat"

class Reptile(Animals):
    pass

class Snake(Reptile):
    diet = "dog"

class Turtle(Reptile):
    diet = "plastic straws"


store = PetStore(1)
"""
store.addPet(Turtle("Sherbert"))
store.addPet(Cat("Tom"))
store.addPet(Turtle("IceCream"))
store.addPet(Snake("Ramen"))
"""

"""
print("Reptiles: ")
for pet in store.getReptiles():
    print(pet)

store.feature("Tom")
"""


#polymorphism
#when fuctions or methods can do multiple things baded on the given input
import math
from abc import ABC, abstractmethod

#give the shape ABC(abstract class) meaning there will never be an instance of this class
class Shape(ABC):
    def __init__(self,value):
        self.value = value

    @abstractmethod
    def area(self):
        return 0

class Square(Shape):
    def area(self):
        return self.value * self.value

class Circle(Shape):
    def area(self):
        return round(math.pi * self.value**2,2)

class Rectangle(Shape):
    def __init__(self, value, value2):
        super().__init__(value)
        self.value2 = value2
    
    def area(self):
        return self.value * self.value2


shapes = [Square(4),Circle(4),Rectangle(5,3),"this", Rectangle(8,2)]

"""
for shape in shapes:
    if isinstance(shape, Shape):
        print(shape.area())
"""

#exceptions
#ways we handle erros that are given by users in a way that doesnt break the code
#zero division,file not found, value error, type error, index error
# ^ these are set to be found by the comupter 

class NegativeNumberError:
    pass
"""
while True:
    try:
        num = int(input("Tell me a number: "))
        
    except ValueError:
        print("that wasnt a whole number love")
        continue

    else:
        break

while True:
    try:
        numTwo = int(input("Tell me another number: "))
        if numTwo <= 0:
            raise NegativeNumberError("cant be a negative number")
    except (ValueError):
        print("that wasnt a whole number love")
        continue
    except  NegativeNumberError as e:
        print(e)
        continue

    else:
        try:
            print(f"{str(num)} over {str(numTwo)} equals {num / numTwo}")
            break
        except ZeroDivisionError:
            print("you cant divide by 0 b*tch, give it another go")
            continue
        #runs no matter what, even if error
        finally:
            print("thanks for playing!")
        

"""

