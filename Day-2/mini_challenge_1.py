#Challenge 1 — Temperature
#Ask the user for Celsius and convert it to Fahrenheit.
#Formula: F = (C × 9/5) + 32

print("Temperature Converter")
celsius = int(input("Enter the temperature in celsius: "))
fahrenheit = (celsius*9/5) + 32
print("Temperature:", fahrenheit,"F")