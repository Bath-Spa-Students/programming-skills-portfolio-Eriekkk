print("Chapter 4: \nExercise 1: Alien Colors\n")

#asking the user for the color
print("green")
print("yellow")
print("red\n")
alien_color = input("Please select one of the 3 colors: ")

#a conditional statement if alien_color equals to green you earn 5 points
if alien_color.casefold() == "green":
    print("Congrats! You have earned 5 points")


