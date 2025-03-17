import random
import mafia_items

class Character:
    """Creates a base class for all game characters""" #created new seperate base to rectify attribute issues
    def __init__(self, name, role, status):
        self.name = name
        self.role = role
        self.status = status  # 'alive', 'injured', 'dead'

class Townperson(Character):
    """Create the base model of a townsperson""" 
    def __init__(self, name, role,status,charnumber):
        self.name=name
        self.role=role #Either Villager, Detective, Murderer, or Doctor
        self.status=status #will be either "Alive","Injured",and "Dead"
        self.charnumber=charnumber #used in dice roll decision making for NPC actions


class playDetective(Character):
    """Creates the player version of the detective character"""
    def __init__(self, name, role,status):
        super.__init__(self, name, role,status)
        self.dectInventory=[]
    def checkInv():
        for item in self.dectInventory:
            print(f'{item},')

    def lookClues():


     def declareSuspect(self,target):
      if target.role== "Murderer":
         print(f"Congratulations, you have found {target.name} to be the murderer!")
        
         return True #
     

class Doctor(Character):
    def __init__(self, name, role,status):
        super.__init__(self, name, role,status)

    def heal(self,townslist): #must remember to create townslist in main file, this is just list of townspeople for various functions
        diceroll1= random.randint(1,2)
        if diceroll1==1: #heal process start
            dcroll2= random.randint(1,5) #selection of who to try to heal
            for Townperson in townslist:
                if Townperson.charnumber==dcroll2:
                    if Townperson.status == "Injured":
                        Townperson.status = "Alive" #Should reset their status to "Alive" if successful
                        print("The doctor was able to successfully save a Townsperson tonight")
                        break
                    else:
                        print("The doctor failed to save any Townsperson tonight")
                        break

    