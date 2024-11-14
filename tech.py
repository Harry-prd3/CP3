class Tech:
    def __init__(self, name, storage):
        self.name = name
        self.storage = storage

class Phone(Tech):
    def __init__(self, color):
        self.color = color
    
    def __str__(self):
        pass

class Phone(Tech):
    def __init__(self, color, name, storage):
        self.color = color
        self.name = name
        self.storage = storage
    
    def __str__(self):
        return(f"A {self.color} {self.name} with {self.storage}GB of storage.")

    def __repr__(self):
        print(f"Phone({self.name},{self.storage},{self.color})")

class Laptop(Tech):
    def __init__(self, size, name, storage):
        self.size = size
        self.name = name
        self.storage = storage
    
    def __str__(self):
        return(f"{self.size}-inch {self.name} with {self.storage}GB of storage.")

    def __repr__(self):
        print(f"Laptop({self.name},{self.storage},{self.size})")



l1 = Laptop(15, "Macbook", 256)
p1 = Phone("sage", "Pixel 5", 128)
print(p1)
print(l1)
p1.__repr__()
l1.__repr__()