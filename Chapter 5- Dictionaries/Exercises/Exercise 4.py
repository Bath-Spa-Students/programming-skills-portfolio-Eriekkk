print("Chapter 5: \nExercise 4: Rivers\n")

#dictionary of ricers and countries
rivers = {
    "Davao River": "Philippines",
    "Amazon River": "Brazil",
    "Ganges River": "India"
}
#using loop to print a sentece about each of the river
for i,x in rivers.items():
    print(f"the {i} is located in the country of {x}.")
#using loop to print only the names of the river
print("\nRivers:")
for i in rivers.keys():
    print(i)
#using loop to print only the names of the contries
print("\nCountries:")
for i in rivers.values():
    print(i)