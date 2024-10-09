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





eevee = pokemon("JayRod", 37, "normal", 2)
electivire = pokemon("bobsive", 1, "electric", 36.872)
pika = pokemon.pikachu()

print(eevee.lvl_up)
print(eevee)
pika.hp = pokemon.hp_update(pika)
print(pika)