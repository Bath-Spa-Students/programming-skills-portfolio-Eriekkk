print("Exercise 1: Pizza Toppings\n")

#using empty list to store pizza toppings 
toppings = []

#Using while loop to continue outputing to continue asking for the pizza 
while True:
    pizza_toppings = input("Please add your pizza toppings (if you are done type 'quit'): ").lower()
    #an if statement if the user is done adding their toppings and a break
    if pizza_toppings == "quit":
        break
    #adding the toppings to the empty list
    toppings.append(pizza_toppings)
    #showing the user that the toppings is added to to the pizza
    print(f"{pizza_toppings} is already added to your pizza")

#printing all the topings you added 
print("\nHere are your pizza toppings: ")
for i in toppings:
    print(i)
    