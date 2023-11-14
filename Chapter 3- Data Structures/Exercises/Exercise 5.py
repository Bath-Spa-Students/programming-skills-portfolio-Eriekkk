print("Chapter 3: \nExercise 5: Change guest list\n")

#list with guest name
guest_list = ["Miyamura Izumi","Thorfinn","Wilbur soot", "Stephen Curry", "JR"]
not_attend = "JR" #a name in the list that will not attend

#replacing and adding names in the list
print(f"Sadly {not_attend} will not attend due to an emergency")
new = "Eren Yeager"
guest_list.remove(not_attend)
guest_list.append(new)

#using loop to print an invitation to each guest
for invited in guest_list:
    letter = f"Hello {invited}, I am glad to invite you for a dinner party later"
    print(letter)
