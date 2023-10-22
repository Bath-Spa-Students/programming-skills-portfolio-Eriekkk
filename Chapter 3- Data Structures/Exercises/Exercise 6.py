print("Exercise 6: Shrinking Guest List")

guest_list = ["Miyamura Izumi","Thorfinn","Wilbur soot", "Stephen Curry", "JR"]
not_attend = "JR"
print(f"Sadly {not_attend} will not attend due to an emergency")
new = "Eren Yeager"
guest_list.remove(not_attend)
guest_list.append(new)

print("Sorry due to booking difficulty only two people are invited to the dinner party")
while len(guest_list) >2:
        remove = guest_list.pop()
        print(f"I am sorry {remove}, you are no longer invited for the dinner party")


for invited in guest_list:
    letter = f"Hello {invited}, I am glad to invite you for a dinner party later"
    print(letter)

del guest_list[:]
print("Guest list:", guest_list)

