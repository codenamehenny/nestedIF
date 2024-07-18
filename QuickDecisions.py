# Task 1: Code Correction You are provided with a Python script that is supposed to help in event planning, but it has errors. Identify and fix them.

attendees = int(input("Enter number of attendees: ")) # established type of value to integer
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

#Task 2: Venue Selection - Based on the corrected code from Task 1, further enhance your code to recommend additional things like "audio system" or "projector" based on the number of attendees.
if attendees > 100:
    media = "audio system"
elif attendees < 100:
    media = "projector"

print("Based on the number of antendees, you'll need a", media)

#Task 3: Catering Choices -Ask the user if they want "vegetarian" food. Recommend "Veggie Delight Caterers" if yes, otherwise recommend "Gourmet Meals Caterers".

foodChoice = input("Would you like vegetarian food? ")
if foodChoice == "yes":
    print("Veggie Delight Caterers is recommended")
else:
    print("Gourmet Meals Caterers is recommended")