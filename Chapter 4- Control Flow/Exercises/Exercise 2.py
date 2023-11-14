print("Exercise 2: alien Color #2\n")

#asking the user for the color
print("green")
print("yellow")
print("red\n")
alien_color = input("Please select one of the 3 colors: ").casefold()

#conditional statement to check the color of the alian
if alien_color == "green":
    print("Congrats! You have earned 5 points for shooting the alien\n")
else:
    print("Congrats! You have just earned 10 points\n")

