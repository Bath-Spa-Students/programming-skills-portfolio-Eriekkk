print("Chapter 5: \nExercise 5: Pets\n")

#a dictionary with 5 differnet animals and owner
cat = {"animal": "cat", "owner": "Eriel"}
dog = {"animal": "dog", "owner": "Miyamura"}
bird = {"animal": "bird", "owner": "Mikasa"}
fish = {"animal": "fish", "owner": "Armin"}
monkey = {"animal": "monkey", "owner": "Eren"}

#storing the dictionary in one list
pets = [cat, dog, bird, fish, monkey]

#using  loop to print all the information in the list
for i in pets:
    animal = i["animal"]
    owner = i["owner"]
    print(f"{owner} owned a {animal} in his house")