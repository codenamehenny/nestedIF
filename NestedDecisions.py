#Task 1: Code Correction You are provided with a Python script that is supposed to guide a user through an adventure game, but it has some errors. 
# Identify and fix them.

place = input("Choose a place: forest or cave? ")

if place == "forest": #added another = to compare if values are equal
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree": #added another =
        print("You found a bird's nest!")
    else: # removed condition because else is opposite if, no condition needed
        print("You found a boat!")
else: #changed elif to else to be opposite initial if condition
    print("You find a hidden treasure!")