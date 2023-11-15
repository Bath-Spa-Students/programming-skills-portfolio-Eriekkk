print("Chapter 6: \nExercise 4: Deli\n")

orders = ["grilled cheese", "egg", "chicken", "nutella", "ham"]
finished = []

#loop to move the sandwhich orders to the finished sandwiches and printing the current order
while orders:
    current = orders.pop(0)
    finished.append(current)
    print(f"Your {current} sandwiched is done, come pick it up!")

#printing all the finished orders
print("\nHere are the finished orders: ")
for i in finished:
    print(f"{i} sandwhich")


