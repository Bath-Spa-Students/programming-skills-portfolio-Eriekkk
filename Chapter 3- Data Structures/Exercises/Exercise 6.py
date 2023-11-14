print("Chapter 3: \nExercise 6: Shrinking Guest List\n")

#list with guest name
guest_list = ["Miyamura Izumi","Thorfinn","Wilbur soot", "Stephen Curry", "JR"]
not_attend = "JR" #a name in the list that will not attend

#replacing and adding names in the list
print(f"\nSadly {not_attend} will not attend due to an emergency")
new = "Eren Yeager"
guest_list.remove(not_attend)
guest_list.append(new)

#using while loop with a condition to remove 3 guest names
print("\nSorry due to booking difficulty only two people are invited to the dinner party\n")
while len(guest_list) >2:
        remove = guest_list.pop()
        print(f"I am sorry {remove}, you are no longer invited for the dinner party")

#using loop to print an invitation to each guest
for invited in guest_list:
    letter = f"Hello {invited}, I am glad you are still invited for a dinner party later"
    print(letter)

#making an empty list
del guest_list[:]
print("\nGuest list:", guest_list)

