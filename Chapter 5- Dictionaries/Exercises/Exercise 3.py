("Exercise 2: Glossary #2\n")

#dictionary about the progrraming words and the meanings
glossary = {
    "Conditional Statement": "Also know as if, else, and elif statement and it allows you to control the flow of your program based on conditions that you specify.",
    "Variable": "Is a programming term that is a named storage or a serverd memory location to store data.",
    "Strings": "Is a sequence of characters that are inside of quotation marks, it can be either letters, numbers, or symbols.",
    "Integers": "it is a whole number that can be either position or negative and without any deicmal points.",
    "List": "It is a collection of mutltiple items that ar stored in a single variable",
    "Tuple": "It is a collection multiple items like a list but it's immutable",
    "Dictionary": "It is a collection of key-value pairs.",
    "Loops": "It is a control flow statement that allows a repetition of codes.",
    "Comments": "It is a annotation in the source of a computer program that helps the programmer to understand the codes.",
    "Float": "It is a data type composed of a number that is not a whole number and with a decimal point.",
}

print("Five programming terms: \n")
#using loop to print the items in the dictionary
for i,x in glossary.items():
    print(f"{i}: {x}\n")