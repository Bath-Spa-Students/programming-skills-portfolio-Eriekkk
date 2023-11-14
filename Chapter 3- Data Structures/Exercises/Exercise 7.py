print("Chapter 3: \nExercise 7: Seeing the world\n")

favorite_place = ["Kyoto", "Tokyo", "Okinawa", "Yukashima", "Hiroshima"]
#print in orginial order
print(f"List not sorted: {favorite_place}\n")
#print in alphabetical order
print(f"List sorted alphabetically: {sorted(favorite_place)}\n")
#back to orginal order
print(f"Original list: {favorite_place}\n")
#print in reverse alphabetical order
print(f"List reverse alphabetically: {sorted(favorite_place, reverse = True)}\n")
#back to original order
print(f"Original list: {favorite_place}\n")
#reverse the list order
favorite_place.reverse()
print(f"list reverse: {favorite_place}\n")
#back to original order
favorite_place.reverse()
print(f"Back to original list: {favorite_place}\n")
#back to alphabetical order
favorite_place.sort()
print(f"Back to alphabetical order: {favorite_place}\n")
#back to reverse alphabetical order
favorite_place.sort(reverse = True)
print(f"Back to reverse alphabetical: {favorite_place}\n")

