class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = .15 if price > 1000 else 0.12

    def display_all(self):
        print "Price:", self.price
        print "Speed:", self.speed
        print "Fuel:", self.fuel
        print "Mileage:", self.fuel
        print "Tax:", self.tax
        print

car1 = Car(1000, "35mph", "Full1", "15mpg")
car2 = Car(2000, "5mph", "Not Full","105mpg")
car3 = Car(4000, "15mph", "Kind of Full", "95mpg")
car4 = Car(5000, "25mph", "Empty", "25mph")
car5 = Car(20000, "45mph", "Empty", "25pmg")

car1.display_all()
car2.display_all()
car3.display_all()
car4.display_all()
car5.display_all()
