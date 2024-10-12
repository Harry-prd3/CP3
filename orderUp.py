menu = {"dr.pepper": 1.50, "sprite": 1.50, "soup": 2.00, "salad": 1.50,"spagetti": 6.50, "steak": 8.00, "corn": 1.00,"broccoli": 1.00,"cake": 4.50,"sunday": 4.00, "no": 0}

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

    #static method for getting price
    def price(order):
        price = 0
        price += menu[order.drink]
        price += menu[order.app]
        price += menu[order.main]
        price += menu[order.side1]
        price += menu[order.side2]
        price += menu[order.dess]
        return(price)


    def __str__(self):
        return(f"\nYour drink is: {self.drink}\nYour appetizer is: {self.app}\nYour main is: {self.main}\nYour side(s) is: {self.side1},{self.side2}\nYour dessert is: {self.dess}")

def make_order():
    drink = None
    while drink == None:
        drink = input("what would you like to drink?, we have dr.pepper, sprite or if you don't one type no: ")
        if drink not in menu:
            print("that's not on our menu")
            drink = None
    app = None
    while app == None:
        app = input("what would you like as an appitizer?, we have soup, salad or if you don't one type no: ")
        if app not in menu:
            print("that's not on our menu")
            app = None
    main = None
    while main == None:
        main = input("what would you like as a main?, we have spagetti, steak or if you don't one type no: ")
        if main not in menu:
            print("that's not on our menu")
            main = None
    side1 = None
    while side1 == None:
        side1 = input("what would you like as your first side?, we have corn, broccoli or if you don't one type no: ")
        if side1 not in menu:
            print("that's not on our menu")
            side1 = None
    side2 = None
    while side2 == None:
        side2 = input("what would you like as your second side?, we have corn, broccoli or if you don't one type no: ")
        if side2 not in menu:
            print("that's not on our menu")
            side2 = None
    dess = None
    while dess == None:
        dess = input("what would you like as your dessert?, we have cake, sunday or if you don't one type no: ")
    if dess not in menu:
            print("that's not on our menu")
            dess = None

    #make sure they ordered somthing
    if drink == "no" and app == "no" and main == "no" and side1 == "no" and side2 == "no" and dess == "no":
        print("you didn't order anything, try again.")
        make_order()
    else:
        global user_order
        user_order = order(drink,app,main,side1,side2,dess)
        orderPrint()

def orderPrint():
    print(user_order)
    total = order.price(user_order)
    print(f"your total is: {total}")
    changeOrder()

def changeOrder():
    change = "no"
    while change == "no":
        change = input("would you like to change your order? (yes/no): ")
        if change == "yes":
            keepAsk = "yes"
            while keepAsk == "yes":
                what = input("what would you like to change?(drink, apptizer, main, side1, side2, dessert): ")
                if what != "drink" or "appitizer" or "main" or "side1" or "side2" or "dessert":
                    print("that was not one of your options to change.")
                else:
                    if what == "drink":
                        while drink == None:
                            drink = input("what would you like to drink?, we have dr.pepper, sprite or if you don't one type no: ")
                            if drink not in menu:
                                print("that's not on our menu")
                                drink = None
                    if what == "appitizer":
                        while app == None:
                            app = input("what would you like as an appitizer?, we have soup, salad or if you don't one type no: ")
                            if app not in menu:
                                print("that's not on our menu")
                                app = None
                    if what == "main":
                        while main == None:
                            main = input("what would you like as a main?, we have spagetti, steak or if you don't one type no: ")
                            if main not in menu:
                                print("that's not on our menu")
                                main = None
                    if what == "side1":
                        while side1 == None:
                            side1 = input("what would you like as your first side?, we have corn, broccoli or if you don't one type no: ")
                            if side1 not in menu:
                                print("that's not on our menu")
                                side1 = None
                    if what == "side2":
                        while side2 == None:
                            side2 = input("what would you like as your second side?, we have corn, broccoli or if you don't one type no: ")
                            if side2 not in menu:
                                print("that's not on our menu")
                                side2 = None
                    if what == "dessert":
                        while dess == None:
                            dess = input("what would you like as your dessert?, we have cake, sunday or if you don't one type no: ")
                            if dess not in menu:
                                print("that's not on our menu")
                                dess = None

        elif change == "no":
            print("perfect thank you.")
        else:
            print("only type yes or no in lowercase.")
            change == "no"

make_order()