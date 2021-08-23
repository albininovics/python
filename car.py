class Cars:
    def __init__(self, name, price, colour):
        self.name = name
        self.price = price
        self.colour = colour

    def start(self):
        print(self.name + "Engine Started")
car1 = Cars("Kia", 25000, "Red")
car2 = Cars("Tata", 15000, "white")
car1.colour = "Blue"
print(car1.name, car1.price, car1.colour)
print(car2.name, car2.price, car2.colour)


car1.start()
car2.start()