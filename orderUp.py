menu = {"drink": "dr.pepper", "drink": "sprite", "soup":"app", "salad":"app","spagetti":"main", "steak":"main", "corn":"side","broccoli":"side","cake":"dessert","sunday":"dessert"}

class order:
    def __init__(self, drink, app, main, side1, side2, dess):
        self.drink = drink
        self.app = app
        self.main = main
        self.side1 = side1
        self.side2 = side2
        self.dess = dess

    def set_drink(self,value):
        self.drink = value
    def set_app(self,value):
        self.app = value
    def set_main(self,value):
        self.main = value
    def set_side1(self,value):
        self.side1 = value
    def set_side2(self,value):
        self.side2 = value
    def set_dess(self,value):
        self.dess = value

    def get_drink(self):
        return(self.drink)
    def get_app(self):
        return(self.app)
    def get_main(self):
        return(self.main)
    def get_side1(self):
        return(self.side1)
    def get_side2(self):
        return(self.side2)
    def get_dess(self):
        return(self.dess)

    def __str__(self):
        return(f"\nYour drink is: {self.drink}\nYour appetizer is: {self.app}\nYour main is: {self.main}\nYour side(s) is: {self.side1},{self.side2}\nYour dessert is: {self.dess}")

def make_order():
    drink = None
    while drink == None:
        drink = input("what would you like to drink?, we have dr.pepper, sprite or if you don't one type no: ")
        print(drink)
    app = None
    while app == None:
        app = input("what would you like as an appitizer?, we have soup, salad or if you don't one type no: ")
    main = None
    while main == None:
        main = input("what would you like as a main?, we have spagetti, steak or if you don't one type no: ")
    side1 = None
    while side1 == None:
        side1 = input("what would you like as your first side?, we have corn, broccoli or if you don't one type no: ")
    side2 = None
    while side2 == None:
        side2 = input("what would you like as your second side?, we have corn, broccoli or if you don't one type no: ")
    dess = None
    while dess == None:
        dess = input("what would you like as your dessert?, we have cake, sunday or if you don't one type no: ")
    
    #make sure they ordered somthing
    if drink and app and main and side1 and side2 and dess == "no":
        print("you didn't order anything, try again.")
        make_order()
    else:
        global user_order
        user_order = order(drink,app,main,side1,side2,dess)
        return user_order

make_order()
print(user_order)