print("Exercise 2: alien Color #3\n")

#asking the user for a color
print("green")
print("yellow")
print("red\n")
alien_color = input("Please select one of the 3 colors: ").casefold()

#conditional statement to check the color of the alien
if alien_color == "green":
    print("Congrats! You have earned 5 points!\n")
elif alien_color == "yellow":
    print("Congrats! You have earned 10 points!\n")
elif alien_color == "red":
    print("Congrats! You have earned 15 points!\n")
else:
    print("Please enter an appropriate color alien")
