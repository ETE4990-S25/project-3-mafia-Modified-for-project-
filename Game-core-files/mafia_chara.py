import random
import mafia_items
Knife=mafia_items.basicItems("Knife","BLABLABLA THIS IS A TEST DESCRIPTION",2)
Gun=mafia_items.basicItems("Gun","BLABLABLA THIS IS A TEST DESCRIPTION",3)
Pillow=mafia_items.basicItems("Pillow","BLABLABLA THIS IS A TEST DESCRIPTION",1)
class Character:
    """Creates a base class for all game characters""" #created new seperate base to rectify issues w/ charnumber
    def __init__(self,name,role,status):
        self.name = name 
        self.role = role  #Either Villager, Detective, Murderer, or Doctor
        self.status = status  #will be either "Alive","Injured",and "Dead"

class Townperson(Character):
    """Create the base model of a townsperson""" 
    def __init__(self,name,role,status,charnumber):
        super().__init__(name, role, status)  
        #self.name=name
        #self.role=role #Either Villager, Detective, Murderer, or Doctor
        #self.status=status #will be either "Alive","Injured",and "Dead"
        self.charnumber=charnumber #used in dice roll decision making for NPC actions


class playDetective(Character):
    """Creates the player version of the detective character"""
    def __init__(self,name,role,status):
        super().__init__(name,role,status)
        self.dectInventory=[]
    def checkInv(self):
        for item in self.dectInventory:
            print(f'Option:{item.Itemname} Description:{item.ItemDesc}')

    #def lookClues():


    def declareSuspect(self,sustarget):
     if sustarget.role== "Murderer":
         print(f"Congratulations, you have found {sustarget.name} to be the murderer!")
        
         return True #


class npcDetective(Character):
    def __init__(self,name,role,status):
        super().__init__(name,role,status)
    def npcdeclareSus(self,townslist):
        npcdecroll=random.randint(1,6)
        if npcdecroll==6:
            asda


class Doctor(Character):
    def __init__(self,name,role,status):
        super().__init__(name,role,status)

    def heal(self,townslist): #must remember to create townslist in main file, this is just list of townspeople for various functions
        #diceroll1= random.randint(1,2)
        #if diceroll1==1: #heal process start   ->thought process here was to add 2nd layer of RNG to make it harder to save injured chara
            dcroll2= random.randint(1,5) #selection of who to try to heal
            for Townperson in townslist:
                if Townperson.charnumber==dcroll2:
                    if Townperson.status == "Injured":
                        Townperson.status = "Alive" #Should reset their status to "Alive" if successful
                        print("The doctor was able to successfully save a Townsperson tonight")
                    
                    else:
                        print("The doctor failed to save any Townsperson tonight")
                    break




class playKiller(Character):
    def __init__(self,name,role,status):
        super().__init__(name,role,status)

        self.killInv=[]  #just set to test the function, will remove once items file is done
    def checkInv_k(self):
        for item in self.killInv:
            print(f'Item name:{item.Itemname} Description:{item.ItemDesc} Uses left:{item.itemUses}')
    def killTown(self,killTarget,killMethod): #Method for player killer to eliminate townsperson
        if killTarget.status == "Alive" and killMethod.itemUses !=0 :
            killTarget.status = "Injured" #Sets NPC status to Injured, which will cause them to die at the end of the night if not healed
            print(f"{killTarget.name}'s fate has been sealed...")

            killMethod.itemUses-=1  #reducing the uses of the different kill methods,
           # if killMethod.itemUses==0:
            #    self.killInv.remove(killMethod) # line here to remove the selected killmethod from the killer's inventory
            #commented that out for now, debating if item should remain in inventory or not, somewhat broken anyway
        else:
            if killMethod.itemUses ==0:
                print("this method is no longer available, please select another")                 
            if killTarget.status == "Injured" or killTarget.status == "Dead":
                print("this target is no longer available, please select another")      
    

class NPCKiller(Character):
    def __init__(self,name,role,status):
        super().__init__(name,role,status)

    def npcKill(self,townslist):
        killerroll=random.randint(1,5) #selection of who to try to kill
        for Townperson in townslist:
            if Townperson.charnumber==killerroll:
                if Townperson.status == "Alive":
                    Townperson.status = "Injured"
                else:
                        print("The killer failed to kill any Townsperson tonight")
                break    