# Create an empty list to store fruits
fruits = []

# Ask the user to enter 5 fruits
for i in range(5):
    fruit = input("Enter a fruit: ")
    fruits.append(fruit)

# Print each fruit in the list using a for loop
print("Fruits entered by the user:")
for fruit in fruits:
    print(fruit)
