print("Chapter 4: \nExercise 4: Stages of Life\n")

#asking the user's age
age = int(input("Please enter your age: "))

#using conditional statement to determine the person's state of life
if age < 2:
    print("You are a baby")
elif age >= 2 and age < 4:
    print("You are a toddler")
elif age >= 4 and age < 13:
    print("You are a kid")
elif age >= 13 and age < 20:
    print("You are a teenager")
elif age >= 20 and age < 65:
    print("You are an adult")
else:
    print("You are an elder")
