print("Chapter 7: \nExercise 3: T-Shirt\n")

#defining a function
def make_shirt(size, message):
    print(f"I am making a {size} shirt with a message on it saying: {message}")

#calling the function using positional arguments
make_shirt("large", "I love Basketball")
#calling the function using keyword arguments
make_shirt(size = "small", message = "I love Volleyball")