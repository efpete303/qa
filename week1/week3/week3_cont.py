# #activity 2 avoiding obstacles
# #ask user for the number of obstacles to avoid
# print("how many obstacles should I avoid?")
# obstacles_to_avoid = int(input())
# #initialize the counter for avoiding obstacles
# avoided_obstacles = 0
# while avoided_obstacles < obstacles_to_avoid:
#     print("Avoiding.",end="")
#     avoided_obstacles += 1
#     print(f".. Done {avoided_obstacles} Obstacles avoided.")
# print("All obstacles has been avoided.")


# #ask the user how many bars to charge
# print("How many bars should I charge?")
# bars_to_charge = int(input())
# charged_bars = 0
# while charged_bars < bars_to_charge:
#     charged_bars += 1
#     print("Charging:","\u2588" * charged_bars)

#repeating words
# ask the user for a phrase
print("Please enter the phrase?")
phrase = input()
#Print "hi" for the number oof characters in the phrase
print(" ".join(" Hi")* len(phrase))