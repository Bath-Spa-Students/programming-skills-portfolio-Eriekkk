print("Exercise 4: Deli\n")

sandwich_orders = ["grilled cheese", "egg", "chicken", "nutella", "ham"]
finished_sandwiches = []

#loop to move the sandwhich orders to the finished sandwiches and printing the current order
while sandwich_orders:
    current_orders = sandwich_orders.pop(0)
    print(f"Your {current_orders} sandwiched is done, come pick it up!")
    finished_sandwiches.append(current_orders)

#printing all the finished orders
print("\nHere are the finished orders: ")
for i in finished_sandwiches:
    print(i)


