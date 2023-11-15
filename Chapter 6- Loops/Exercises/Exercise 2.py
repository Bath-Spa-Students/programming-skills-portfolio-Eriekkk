print("Chapter 6: \nExercise 2: Movie Tickets\n")
#using a while loop to contiue asking the user for there age
while True:
    age = input("Please enter your age (to get your ticket price type 'quit'): ").lower()
    if age == "quit":
        break
    #converting a string to an integer
    num_age = int(age)
    #using if statemetn to determine the pirce of the tickets
    if num_age < 3:
        price = 0
    elif num_age >= 3 and num_age < 13:
        price = 10
    else:
        price = 15
    #printing the cost of the tickets
    print(f"The movie ticket cost is ${price}")

