import string
from time import sleep
ask = input("Do you want to play the game? (Yes/No) ").lower()
if ask == "yes":
    print("Awesome! Let's start the game!")
elif ask == "no":
    another = input("Are you sure you want to leave? (YES/NO) ").lower()
else:
    print("Not understood.")
if another == "yes":
   print("That's a pity.")
   quit(True)
elif another == "no":
     print("Awesome! Let's start the game!")
else:
    print("Command not understood.")
