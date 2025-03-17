#murder_roll
import random

dice_roll = random.randint (1,6)
if dice_roll == 1 :
    name = "Max"
elif dice_roll == 2  :
    name = "Eve"
elif dice_roll == 3:
    name = "Bob"
elif dice_roll == 4 :
    name = "Jack"
elif dice_roll == 5:
    name = "Ari"
elif dice_roll == 6:
    name = "drew"


print(f"The murder has struck...{name} was attacked.")