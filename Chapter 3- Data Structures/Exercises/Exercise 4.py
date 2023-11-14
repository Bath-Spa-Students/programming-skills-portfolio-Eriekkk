print("Chapter 3: \nExercise 4: Guest list\n")

#list with guest name
guest_list = ["Miyamura Izumi","Thorfinn", "Wilbur soot", "Stephen Curry", "JR"]

#using loop to print an invitation to each guest
for invited in guest_list:
    letter = f"Hello {invited}, I am glad to invite you for a dinner party later"
    print(letter)