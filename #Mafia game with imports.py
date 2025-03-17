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

#import doc roll here

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



# night two 
print (f"Welcome to night two.")

# call the kill options


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


# call the kill options


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




#player detective
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

# import detective 

