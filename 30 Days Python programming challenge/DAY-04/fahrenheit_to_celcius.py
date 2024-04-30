# Constant conversion factor
CONVERSION_FACTOR = 5 / 9

# Take user input for temperature in Fahrenheit
fahrenheit = float(input("Enter the temperature in Fahrenheit: "))

# Convert Fahrenheit to Celsius
celsius = (fahrenheit - 32) * CONVERSION_FACTOR

# Print the temperature in Celsius
print("The temperature in Celsius is:", celsius)
