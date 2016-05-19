
from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
# Phase 0: fix the typos/bugs 5 or so of them...!
# Phase 1: Comment this code!
# Phase 2: Build out the game further, make the armies attack one another!
# Phase 3: Set it up some that if a member of an army has less than 0 health remove it from the army
# Phase 4: Set up the battles so that different army types fight differently!
import random
class Human(object):
   #creating a new human, the default clan is none
   def __init__(self, clan = None):
       super(Human, self).__init__()
       print 'New Human!!!'
       self.health = 100
       self.strength = 3
       self.intelligence = 3
       self.stealth = 3
       self.clan = clan

   def taunt(self):
       print "You want a piece of me?"
       return self

   def attack(self,target):
       self.taunt()
       luck = round(random.random() * 100)
       attack = self.strength
       if (self.clan):
           # future arguments for determine what to do if your clan is...
           # maybe this should go in to the game class..
           # and there is something else wrong here... but since we aren't using this if statement...
           if(luck > 50):
               if(luck * self.stealth > 150):
                   print 'attacking!'
                   target.health -= attack
                   target.reporthealth()
                   return True
               else:
                   print 'attack failed'
                   return False
           else:
               self.health -= self.strength
               print "attack failed"
       return False

   def reporthealth(self):
       if self.health > 0:
           print "I am not dead yet!"
       else:
           print "AAAaah you've killed me"


class Ninja(Human):
   def __init__(self, clan = 'Ninja'):
       super(Ninja, self).__init__(clan)
       self.health = 70
       self.stealth = 30
       print 'I am a Ninja'

class Warrior(Human):
   def __init__(self, clan = 'Warrior'):
       super(Warrior, self).__init__(clan)
       self.health = 130
       self.strength = 30
       print 'I am warrior'

class Wizard(Human):

   def __init__(self, clan = 'Wizard'):
       super(Wizard, self).__init__(clan)
       self.health = 50
       self.intelligence = 6
       print 'I am wizard'

class Game(object):
   """docstring for Game"""
   def __init__(self):
       super(Game, self).__init__()
       self.armies = []

   def buildArmy(self, clan = None):
       clanMap = {"Wizard": Wizard, "Ninja": Ninja, "Warrior": Warrior}
       army = []
       if clan:
           for human in range(random.randint(5,10)):
               army.append(clanMap[clan]())
       else:
           for human in range(random.randint(5,10)):
               army.append(Human())
       self.armies.append(army)

game = Game()
print game.armies
game.buildArmy('Ninja')
game.buildArmy('Wizard')
# print game.armies[1][0]
# print game.armies[0][0]
firstWizard = game.armies[1][0]
firstNinja = game.armies[0][0]

print firstNinja.health
print firstWizard.health

# firstNinja.taunt()
firstNinja.attack(firstWizard)

print firstWizard.health


# game.buildArmy('Warrior')
# joe = Human()
# fred = Human()
