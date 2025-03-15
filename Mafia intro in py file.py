# Mafia intro in py file

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
elif choice == '2':
  print (" so theres a new sherif in town then...")
else:
  print("Pick again 1 or 2.")
  
## inventory 
if choice == '1':
 ##   print('murder inventory')
  choice = input("Pick your murder method: p for pillow, k for knife, g for gun: ")

  if choice == 'p':
    print("Night night it is...")
  elif choice == 'k':
    print("Didn't anyone ever tell you to be careful running around with knives?")
  elif choice == 'g':
    print("Ah, a classic one and done kind of deal.")
  else:
    print("Invalid choice. Please choose either p, k, or g.")

if choice == '2':
    ## PRINT (DECTETIVE INVENTORY)
       choice = input (" pick your method of pursuit: s for picking a suspect, f to follow tracks, l look for clues, w wait out the perp: ").strip()

       if choice.lower () == 's':
              print ("who is the most sus here")
       elif choice.lower() == 'f':
              print ("ooo follow those steps")
       elif choice.lower() == 'l':
              print ("take out your magnifying glass.")
       elif choice.lower() == 'w':
              print(" ok then keep waiting...")
       else:
              print("Invalid choice. Please choose from 's', 'f', 'l', or 'w'.")
#### charator list  method will pull from file 
if choice ==  's':
    my_list = [ "Joe", "Eve", "Max", "Ari","Jack","Bob"]
print (f" suspect options are:{my_list}")
suspect_name = input("Who do you pick...:").strip().lower()
print("Our the supect is:",suspect_name)






## the death of a charator and removal
## these are the town people 
my_list = [ "Joe", "Eve", "Max", "Ari","Jack","Bob"]
victim_name = input ("Enter victim name here: ").strip().lower()



if victim_name in [name.lower() for name in my_list]:
    my_list = [name for name in my_list if name.lower() != victim_name]
    print("status updates... the living are:", my_list)

else:
    print(f"{victim_name} was not found.")
