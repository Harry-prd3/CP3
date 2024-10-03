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

    # Create a way to readably print our objects to show they exist
    def __str__(self):
        return f"\nName: {self.name}\nAge: {self.age}\nSpecies: {self.species}\nGender: {self.gender}\nRarity: {self.rarity}"

# Creating our object
# We generally store objects in variables (indibidually or in a list) so we can use it
cat = Animal("Tom", "meow meow", 21, "no thanks", "Epic")
frog = Animal("Jarrod", "Poisin Dart Frog", 500, "Feminane", "Legendary")


print(cat)
print(frog)

# Creating the new argument for the fuction deaths
cat.deaths = 0
frog.deaths = 0

# To call methods you put the name of the object.name of the method(arguments)
print("")
print(cat.fight(frog))
print(cat.deaths)

# Reasinging the name of the cat
cat.name = "Thomas"

print("")
print(cat.fight(frog))
print(cat.deaths)
print(frog.deaths)

# Deleating tom cause he is a stupid little baby
cat = None
print(cat)