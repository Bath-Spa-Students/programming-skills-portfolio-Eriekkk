print("Chapter 6: \nExercise 5: No Pastrami\n")

orders = ["grilled cheese", "pastrami", "egg", "chicken", "nutella", "pastrami", "ham", "pastrami", "pastrami"]
finished = []

print("Sorry we cant make a pastrami sandwhich because we are out of pastrami.\n")

#making a nested loop to remove all the pastrami and moving all the sandwich_orders to finished_standwhices
while orders:
    while "pastrami" in orders:
        orders.remove("pastrami")
            
    current = orders.pop(0)
    finished.append(current)
    print(f"Your {current} sandwiched is done, come pick it up!")

#printing all the finsihed orders
print("\nHere are the finished orders: ")
for i in finished:
    print(f"{i} sandwhch")