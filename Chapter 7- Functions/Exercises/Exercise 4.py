print("Chapter 7: \nExercise 4: Large Shirts\n")

#defining a function
def make_shirt(size = "large", message = "I love Python"):
    print(f"I am making a {size} shirt with a message on it saying: {message}")

#calling the function with default message
make_shirt()
#calling the function with medium size shirt with a defualt message
make_shirt(size="medium")
#calling the function with a different size and message
make_shirt(size="small", message="I love coding")
