import time
import mafia_items
import random
from mafia_chara import Townperson, Doctor, playDetective, npcDetective, playKiller, NPCKiller
input( "press enter to start:")
print ( "wire sounds ")
time.sleep(1) # Add a delay in seconds
print (" flashing lights")
time.sleep(1) # Add a delay in seconds
print ( " woow you are spining out of control" )
print ( " try to stop the spining")
input (" press your enter to stop")
# print("Wire sounds...\nFlashing lights...\nWoow, you're spinning out of control!\nTry to stop the spinning!")

print ( " it seems like you have entered a time machine " )
time.sleep(1) # Add a delay in seconds
print ( " Welcome, or should I say good luck..." )
## player selection
input("press enter to continue:")
print(" my name is Fern. I am the all seeing eye... I will be the narrator of this story")
print ("I dont often see many new people around this town...Lets find out who you are")
Game_choice = input ( "Press 1 for Murder or 2 for Detective enter:")
if Game_choice == '1':
  print ("ooo scary a murder is in town")
  time.sleep(1) # Add a delay in seconds
  print ( " Your goal is to go 3 nights without being caught...")
  playerK=playKiller("Player","Murderer","Alive")
elif Game_choice == '2':
  print (" so theres a new sherif in town then...")
  time.sleep(1) # Add a delay in seconds
  print ('your goal is to catch the murder before the third night')
  playerD=mafia_chara.playDetective("Player","Detective",'Alive')

else:
  print("Pick again 1 or 2.:")

#General setup and functions
def get_target_by_name(name, townylist):                        #This block was created with AI assistance (Deepseek) {start}
    for townie in townylist:                                    #
        if townie.name.lower() == name.strip().lower():         #
            return townie                                       #
    return None                                                 #
                                                                #These two functions are helper functions meant to convert the user input  
def get_method_by_name(name, killer):                           #from strings into the proper objects to be fed into the class method below
    for item in killer.killInv:                                 #
        if item.Itemname.lower() == name.strip().lower():       #
            return item                                         #
    return None      

kill_target = get_target_by_name(victim_name, townperson_list)          #
kill_method = get_method_by_name(killmethodinput, killer)
# Create a list of townspeople (instances of the townperson class
townslist = [
    Townperson("Max", "Townsman", "Alive", 1),
    Townperson("Eve", "Townsman", "Alive", 2),
    Townperson("Bob", "Townsman", "Alive", 3),
    Townperson("Jack", "Townsman", "Alive", 4),
    Townperson("Ari", "Townsman", "Alive", 5)
]
Ktownperson_list = ["Eve", "Max", "Ari","Jack","Bob"] #created for easier NPC viewing 
Dtownperson_list = [ "Joe", "Eve", "Max", "Ari","Jack","Bob"]

  # Create a doctor (instance of the Doctor class)
doctor = Doctor("Dr. Smith", "Doctor", "Alive")  

#game state handling                                    #
daycounter=1


#killer setup
Pillow = mafia_items.basicItems("pillow","Night night it is... number of uses",2)
Knife = mafia_items.basicItems("knife","Didn't anyone ever tell you to be careful running around with knives? Number of uses", 2)
Gun = mafia_items.basicItems("gun","Ah, a classic one and done kind of deal. Number of uses",3)
playerK.killInv=[Knife,Pillow,Gun]

GameOver=False
if Game_choice==1: #setting up the killer game type
    
    while daycounter<4:
    #while GameOver==False:
        while GameOver==False:
        #while daycounter<4:
            print (f"Welcome to night {daycounter}.")
            print (f"There is a detective on your trail... try not to get caught ")
            print("\nCurrent statuses of all townspeople:")
            for person in townslist:
                print(f"{person.name}: {person.status}")
            selecting = True
            while selecting == True:
                print(f"What will you do?\n 1.Check Inventory, 2.Kill)")
                optionselect=input("Please enter only the number of your choice")
                if optionselect=="1":
                    playerK.checkInv_k()
                elif optionselect=="2":
                    killmethodinput = input("What weapon will you use? ").strip()
                    victim_name = input("Enter victim name here: ").strip().lower()
                    kill_target = get_target_by_name(victim_name, townperson_list)          #
                    kill_method = get_method_by_name(killmethodinput, killer)   #This block was created with AI assistance (Deepseek) {end}
                    playerK.killTown(kill_target,kill_method )
                    selecting==False
                else:
                    print("Invalid Input")
            print("The doctor is trying to heal a townsperson...")
            doctor.heal(townslist)
            #"Detective" rolls to catch a suspect (simplified here)
            npcdecroll=random.randint(1,6)
            if npcdecroll==6:
                print("The detective has caught the Murderer! Game Over")
                GameOver=True
            else:
                print("The detective failed to catch the killer")
            time.sleep(5)
            daycounter+=1
