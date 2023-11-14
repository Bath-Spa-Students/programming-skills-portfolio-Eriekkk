print("Exercise 5: Pets\n")

#a dictionary with 5 differnet animals and owner
pet1 = {"animal": "cat", "owner": "Eriel"}
pet2 = {"animal": "dog", "owner": "Miyamura"}
pet3 = {"animal": "bird", "owner": "Mikasa"}
pet4 = {"animal": "fish", "owner": "Armin"}
pet5 = {"animal": "monkey", "owner": "Eren"}

#storing the dictionary in one list
pets = [pet1, pet2, pet3, pet4, pet5]

#using  loop to print all the information in the list
for i in pets:
    kind = i["animal"]
    owner = i["owner"]
    print(f"{owner} owned a {kind} in his house")