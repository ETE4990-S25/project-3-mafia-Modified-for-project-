#Mafia game with imports
#intro

input( "press enter to start:")
print ( "wire sounds ")
print (" flashing lights")
print ( " woow you are spining out of control" )
print ( " try to stop the spining")
input (" press your enter to stop")

print ( " it seems like you have entered a time machine " )
print ( " Welcome, or should I say good luck..." )
## player selection
input("press enter to continue:")
print(" my name is Fern. I am the all seeing eye... I will be the narrator of this story")
print ("I dont often see many new people around this town...Lets find out who you are")
choice = input ( "Press 1 for Murder or 2 for Detective enter:")
if choice == '1':
  print ("ooo scary a murder is in town")
  print ( " Your goal is to go 3 nights without being caught...")
elif choice == '2':
  print (" so theres a new sherif in town then...")
  print ('your goal is to catch the murder before the third night')
else:
  print("Pick again 1 or 2.:")


  #the killer
    # calling invetory
  from mafia_chara import playKiller
import mafia_items

Pillow = mafia_items.basicItems("pillow","Night night it is... number of uses",2)
Knife = mafia_items. basicItems("knife","Didn't anyone ever tell you to be careful running around with knives? Number of uses", 2)
Gun = mafia_items. basicItems ("gun","Ah, a classic one and done kind of deal. Number of uses",3)
 
killer= playKiller ( "Joe", "killer","alive")
killer.killInv =[Pillow, Knife, Gun]
killer.checkInv_k()

# input here 
# murder pick who  save input as a varible call
townperson_list = [ "Joe", "Eve", "Max", "Ari","Jack","Bob"]
print(f"Our victim options are:" ,townperson_list)
victim_name = input ("Enter victim name here: ").strip().lower()

townperson_list = [ "Joe", "Eve", "Max", "Ari","Jack","Bob"]
print(f"Our victim options are:" ,townperson_list)

victim_name = input ("Enter victim name here: ").strip().lower()
killmethodinput = input("What weapon will you use? ").strip()

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
    return None                                                 #

kill_target = get_target_by_name(victim_name, townperson_list)          #
kill_method = get_method_by_name(killmethodinput, killer)   #This block was created with AI assistance (Deepseek) {end}

killer.killTown(kill_target,kill_method )

#imported doc roll below

print(f" But who did the doctor save?")
 #doctor here picks who to save
 #Importing the classes from mafia_chara.py
from mafia_chara import Townperson, Doctor

 # Create a list of townspeople (instances of the townperson class
townslist = [
    Townperson("Max", "Townsman", "Injured", 1),
    Townperson("Eve", "Townsman", "Alive", 2),
    Townperson("Bob", "Townsman", "Injured", 3),
    Townperson("Jack", "Townsman", "Alive", 4),
    Townperson("Ari", "Townsman", "Alive", 5)
]

  # Create a doctor (instance of the Doctor class)
doctor = Doctor("Dr. Smith", "Doctor", "Alive")

  # Simulate the doctor trying to heal someone
print("The doctor is trying to heal a townsperson...")
doctor.heal(townslist)

# Optionally, print the status of all townspeople after the doctor attempts to heal
print("\nCurrent statuses of all townspeople:")
for person in townslist:
    print(f"{person.name}: {person.status}")
#newday
print(f" A New Day has dawned ")
print (f"There is a dectective on your trail... try not to get caught ")

#detective roll here
detective= mafia_chara.playDetective( "Ana", "Detective","alive")
Suspect = mafia_chara.mafia_items.basicItems("Suspect","who is the most sus here...",2)
Follow = mafia_chara.mafia_items.basicItems("Follow","ooo follow those steps ...", 2)
Jail = mafia_chara.mafia_items.basicItems ("Jail","Ah,straigth to jail...",3)
 
detective.dectInventory=[Suspect,Follow,Jail]
detective.checkInv()
npctestkiller=mafia_chara.NPCKiller("Jake","Murderer","Alive")
dectoptionsel = input("Which option will you choose ").strip()
townliststr=[npctestkiller.name] 
for item in townylist:
    townliststr.append(item.name)
townylistdect=list(townylist)
townylistdect.append(npctestkiller)
def get_suspect_by_name(name, townylistdect):                        #
    for chara in townylistdect:                                    #
        if chara.name.lower() == name.strip().lower():         #
            return chara                                       #
    return None     

if dectoptionsel==Suspect.Itemname:
    print(f"Here is a list of the townspeople: {str(townliststr)}")


if dectoptionsel==Jail.Itemname:
    jailselect=input("Who do you think is the killer?: ")
    sus_target = get_suspect_by_name(jailselect, townylistdect)          #
    detective.declareSuspect(sus_target)




# night two 
print (f"Welcome to night two.")

# call the kill options
victim_name = input ("Enter victim name here: ").strip().lower()
killmethodinput = input("What weapon will you use? ").strip()
kill_target = get_target_by_name(victim_name, townperson_list)          #
kill_method = get_method_by_name(killmethodinput, killer)   #This block was created with AI assistance (Deepseek) {end}

killer.killTown(kill_target,kill_method )

#doc roll 
print(f" But who did the doctor save?")
 #doctor here picks who to save
 #Importing the classes from mafia_chara.py

print("The doctor is trying to heal a townsperson...")
doctor.heal(townslist)

# Optionally, print the status of all townspeople after the doctor attempts to heal
print("\nCurrent statuses of all townspeople:")
for person in townslist:
    print(f"{person.name}: {person.status}")

print (f"Good Morning, killer let's find out if your luck has run its course!")

# detective roll here
detective= mafia_chara.playDetective( "Ana", "Detective","alive")
Suspect = mafia_chara.mafia_items.basicItems("Suspect","who is the most sus here...",2)
Follow = mafia_chara.mafia_items.basicItems("Follow","ooo follow those steps ...", 2)
Jail = mafia_chara.mafia_items.basicItems ("Jail","Ah,straigth to jail...",3)
 
detective.dectInventory=[Suspect,Follow,Jail]
detective.checkInv()
npctestkiller=mafia_chara.NPCKiller("Jake","Murderer","Alive")
dectoptionsel = input("Which option will you choose ").strip()
townliststr=[npctestkiller.name] 
for item in townylist:
    townliststr.append(item.name)
townylistdect=list(townylist)
townylistdect.append(npctestkiller)
def get_suspect_by_name(name, townylistdect):                        #
    for chara in townylistdect:                                    #
        if chara.name.lower() == name.strip().lower():         #
            return chara                                       #
    return None     

if dectoptionsel==Suspect.Itemname:
    print(f"Here is a list of the townspeople: {str(townliststr)}")


if dectoptionsel==Jail.Itemname:
    jailselect=input("Who do you think is the killer?: ")
    sus_target = get_suspect_by_name(jailselect, townylistdect)          #
    detective.declareSuspect(sus_target)



# call the kill options
victim_name = input ("Enter victim name here: ").strip().lower()
killmethodinput = input("What weapon will you use? ").strip()
kill_target = get_target_by_name(victim_name, townperson_list)          #
kill_method = get_method_by_name(killmethodinput, killer)   #This block was created with AI assistance (Deepseek) {end}

killer.killTown(kill_target,kill_method )

#doc roll 
print(f" But who did the doctor save?")
 #doctor here picks who to save
 #Importing the classes from mafia_chara.py

print("The doctor is trying to heal a townsperson...")
doctor.heal(townslist)

# Optionally, print the status of all townspeople after the doctor attempts to heal
print("\nCurrent statuses of all townspeople:")
for person in townslist:
    print(f"{person.name}: {person.status}")

print(f"Wow you made it to night 3 ... now lets see who makes it out alive...")

# detective roll here
detective= mafia_chara.playDetective( "Ana", "Detective","alive")
Suspect = mafia_chara.mafia_items.basicItems("Suspect","who is the most sus here...",2)
Follow = mafia_chara.mafia_items.basicItems("Follow","ooo follow those steps ...", 2)
Jail = mafia_chara.mafia_items.basicItems ("Jail","Ah,straigth to jail...",3)
 
detective.dectInventory=[Suspect,Follow,Jail]
detective.checkInv()
npctestkiller=mafia_chara.NPCKiller("Jake","Murderer","Alive")
dectoptionsel = input("Which option will you choose ").strip()
townliststr=[npctestkiller.name] 
for item in townylist:
    townliststr.append(item.name)
townylistdect=list(townylist)
townylistdect.append(npctestkiller)
def get_suspect_by_name(name, townylistdect):                        #
    for chara in townylistdect:                                    #
        if chara.name.lower() == name.strip().lower():         #
            return chara                                       #
    return None     

if dectoptionsel==Suspect.Itemname:
    print(f"Here is a list of the townspeople: {str(townliststr)}")


if dectoptionsel==Jail.Itemname:
    jailselect=input("Who do you think is the killer?: ")
    sus_target = get_suspect_by_name(jailselect, townylistdect)          #
    detective.declareSuspect(sus_target)



# call the kill options
victim_name = input ("Enter victim name here: ").strip().lower()
killmethodinput = input("What weapon will you use? ").strip()
kill_target = get_target_by_name(victim_name, townperson_list)          #
kill_method = get_method_by_name(killmethodinput, killer)   #This block was created with AI assistance (Deepseek) {end}

killer.killTown(kill_target,kill_method )

#doc roll 
print(f" But who did the doctor save?")
 #doctor here picks who to save
 #Importing the classes from mafia_chara.py

print("The doctor is trying to heal a townsperson...")
doctor.heal(townslist)

# Optionally, print the status of all townspeople after the doctor attempts to heal
print("\nCurrent statuses of all townspeople:")
for person in townslist:
    print(f"{person.name}: {person.status}")

print(f" Congrats you wiped out most of the town and got away with it...")
print (f"wire SPARKS ")
print(f" flashing lights ")
print (f"Go be a pest in your own time line!!!")



#Player 2 
# Detective
if choice == '2':
  print (f"well detective it seems like you have your work cut out for ")
  print(f"Night is falling...")
  # roll for the murder call from file
  #auto pick
  from Murder_rolls import dice_roll
  name= dice_roll
  print(f"The murder has struck...{name} was attacked.")

 #import doc roll here
  print(f" But who did the doctor save?")
 #doctor here picks who to save

 #doctor here picks who to save
# Simulate the doctor trying to heal someone
  print("The doctor is trying to heal a townsperson...")
  doctor.heal(townslist)

# Optionally, print the status of all townspeople after the doctor attempts to heal
  print("\nCurrent statuses of all townspeople:")
  for person in townslist:
    print(f"{person.name}: {person.status}")


print(f"With day light comes new clues day 1 ")

# import detective and course of action
from mafia_chara import playDetective
import mafia_items
 
detective= playDetective ( "Ana", "Detective","alive")

Suspect = mafia_items.basicItems("Suspect","who is the most sus here...",2)
Follow = mafia_items.basicItems("Follow","ooo follow those steps ...", 2)
Jail = mafia_items.basicItems ("Jail","Ah,straigth to jail...",3)
 
detective.dectInventory=[Suspect,Follow,Jail]
detective.checkInv()

detective.dectInventory=[Suspect,Follow,Jail]
detective.checkInv()

dectoptionsel = input("Which option will you choose ").strip()
townliststr=[testkiller.name] 
for item in townylist:
    townliststr.append(item.name)
if dectoptionsel==Suspect.Itemname:
    print(f"Here is a list of the townspeople: {str(townliststr)}")



print(f"welcome to night two may you find the murder for the sake of the town...")

 # roll for the murder call from file
from Murder_rolls import dice_roll
name= dice_roll
print(f"The murder has struck...{name} was attacked.")

 #imported doc roll below
print(f" But who did the doctor save?")
 #doctor here picks who to save
# Simulate the doctor trying to heal someone
print("The doctor is trying to heal a townsperson...")
doctor.heal(townslist)
# Optionally, print the status of all townspeople after the doctor attempts to heal
print("\nCurrent statuses of all townspeople:")
for person in townslist:
    print(f"{person.name}: {person.status}")

print(f" Another day another donut... how got killed this time... day 2")
 #import detective and course of action
 
detective= playDetective ( "Ana", "Detective","alive")

Suspect = mafia_items.basicItems("Suspect","who is the most sus here...",2)
Follow = mafia_items.basicItems("Follow","ooo follow those steps ...", 2)
Jail = mafia_items.basicItems ("Jail","Ah,straigth to jail...",3)
 
detective.dectInventory=[Suspect,Follow,Jail]
detective.checkInv()

detective.dectInventory=[Suspect,Follow,Jail]
detective.checkInv()

dectoptionsel = input("Which option will you choose ").strip()
townliststr=[testkiller.name] 
for item in townylist:
    townliststr.append(item.name)
if dectoptionsel==Suspect.Itemname:
    print(f"Here is a list of the townspeople: {str(townliststr)}")


print(f"THe killer is still on the lamb")
 # roll for the murder call from file
from Murder_rolls import dice_roll
name= dice_roll
print(f"The murder has struck...{name} was attacked.")

 #imported doc roll below
print(f" But who did the doctor save?")
 #doctor here picks who to save
# Simulate the doctor trying to heal someone
print("The doctor is trying to heal a townsperson...")
doctor.heal(townslist)
# Optionally, print the status of all townspeople after the doctor attempts to heal
print("\nCurrent statuses of all townspeople:")
for person in townslist:
    print(f"{person.name}: {person.status}")


print(f"The rampage continues this is your last chance...day 3")
 #import detective and course of action
 
detective= playDetective ( "Ana", "Detective","alive")

Suspect = mafia_items.basicItems("Suspect","who is the most sus here...",2)
Follow = mafia_items.basicItems("Follow","ooo follow those steps ...", 2)
Jail = mafia_items.basicItems ("Jail","Ah,straigth to jail...",3)
 
detective.dectInventory=[Suspect,Follow,Jail]
detective.checkInv()

detective.dectInventory=[Suspect,Follow,Jail]
detective.checkInv()

dectoptionsel = input("Which option will you choose ").strip()
townliststr=[testkiller.name] 
for item in townylist:
    townliststr.append(item.name)
if dectoptionsel==Suspect.Itemname:
    print(f"Here is a list of the townspeople: {str(townliststr)}")

print(f" Day 3... the trail has gone cold maybe they got away with it...")
# the end of the game 