from human import Human
class Wizard(Human):
    def __init__(self):
        super(Wizard, self).__init__()   # use super to call the Human __init__ method
        self.intelligence = 10           # every wizard starts off with 10 intelligence
    def heal(self):
        self.health += 10
class Ninja(Human):
    def __init__(self):
        super(Ninja, self).__init__()    # use super to call the Human __init__ method
        self.stealth = 10                # every Ninja starts off with 10 stealth
    def steal(self):
        self.stealth += 5
class Samurai(Human):
    def __init__(self):
        super(Samurai, self).__init__()  # use super to call the Human __init__ method
        self.strength = 10               # every Samurai starts off with 10 strength
    def sacrifice(self):
        self.health -= 5
# create new instance of Wizard, Ninja, and Samurai
harry = Wizard()
rain = Ninja()
tom = Samurai()
print "aaa" *3
# all instances still have human properties because its
# class inherits from the Human class
print harry.health
print harry.intelligence
print rain.health
print tom.health
print "bbb" *3
# yet they are subclasses which mean they can extend the current functionality of Human class
# instances of the Wizard class can perform the heal method
harry.heal()
print harry.health
print "ccc" *3

# instances of the Ninja class can perform the steal method
rain.steal()
print rain.stealth
print "ddd" *3
# instances of the Samurai class can perform the sacrifice method
tom.sacrifice()
print tom.health
print tom.stealth
