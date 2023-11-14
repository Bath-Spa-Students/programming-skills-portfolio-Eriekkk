print("Exercise 5: No Pastrami\n")

sandwich_orders = ["grilled cheese", "pastrami", "egg", "chicken", "nutella", "pastrami", "ham", "pastrami", "pastrami"]
finished_sandwiches = []

print("Sorry we cant make a pastrami sandwhich because we are out of pastrami.\n")

#making a nested loop to remove all the pastrami and moving all the sandwich_orders to finished_standwhices
while sandwich_orders:
    while "pastrami" in sandwich_orders:
        sandwich_orders.remove("pastrami")
            
    current_orders = sandwich_orders.pop(0)
    print(f"Your {current_orders} sandwiched is done, come pick it up!")
    finished_sandwiches.append(current_orders)

#printing all the finsihed orders
print("\nHere are the finished orders: ")
for i in finished_sandwiches:
    print(i)