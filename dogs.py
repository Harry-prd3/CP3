class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def __str__(self):
        return(f"The dog's name is: {self.name} and they are a: {self.breed}")

d1 = Dog("Marceline", "German Shepherd")
d2 = Dog("Cajun", "Belgin Malinois")
d3 = Dog("Daisy", "Border Collie")
d4 = Dog("Rocky", "Golden Retriever")
d5 = Dog("Bella", "Irish Setter")

dogs = [d1, d2, d3, d4, d5]

for dog in dogs:
    print(dog)