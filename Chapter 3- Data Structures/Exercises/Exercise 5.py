print("Exercise 5: Change guest list")

guest_list = ["Miyamura Izumi","Thorfinn","Wilbur soot", "Stephen Curry", "JR"]
not_attend = "JR"

print(f"Sadly {not_attend} will not attend due to an emergency")
new_guest = "Eren Yeager"
guest_list.remove(not_attend)
guest_list.append(new_guest)

for invited in guest_list:
    letter = f"Hello {invited}, I am glad to invite you for a dinner party later"
    print(letter)
