#Task 1: Code Correction You are provided with a Python script that is supposed to guide a user through an adventure game, but it has some errors. 
# Identify and fix them.

# ask user to choose a place
place = input("Choose a place: forest or cave? ")

if place == "forest": #added another = to compare if values are equal
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree": #added another =
        print("You found a bird's nest!")
    elif action == "cross a river": # removed condition because else is opposite if, no condition needed
        print("You found a boat!")
elif place == "cave": #changed elif to else to be opposite initial if condition
    print("You find a hidden treasure!")
else:
    pass


#Task 2: Setting the Scene
#Based on your corrected code from Task 1, expand the game. 
#If the user chooses "cave", ask them if they want to "light a torch" or "proceed in the dark", and provide outcomes for each decision.

# section for cave input
if place == "cave":
    light = input("Would you like to light a torch or proceed in the dark? ")
    if light == "light a torch":
        print("As you like a torch, bats start to sworm you! Run for your life!")
    elif light == "proceed in the dark":
        print("You proceed in the dark and go unnoticed. You're ready for another adventure.")
else:
    pass
