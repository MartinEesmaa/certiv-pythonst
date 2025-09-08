# Task 3

"""
The cyber security department for Eesti kunstimuuseum (Estonia Art Museum) 
wants to know the temperature of Tallinn in immutable list for a specific purpose.

They have certain criterions to solve this problem.
The criterions are given below:

SLNO	Requirement Specification

1	    Provide an option where they can take temperature in either Fahrenheit or Celsius scale
2	    Need to collect five temperature from user and add them to the immutable list
3	    Convert the temperature from the Celsius to Fahrenheit or vice versa
4	    Delete the last value. You can convert the tuple to list to do this.
5	    Display the result in tuple 

The Conversion Formula for Fahrenheit to Celsius is given below:

T(°C) = (T(°F)  - 32) × 5/9  Here T(°C)  refers to the temperature in Celsius and T(°F)  
is defined for Fahrenheit temperature.

The Conversion formula for Celsius to Fahrenheit is given below:

T(°F) = T(°C) × 9/5 + 32 Here T(°C)  refers to the temperature in Celsius and T(°F)  
is defined for Fahrenheit temperature.


User can prefer to choose to convert from Celsius to Fahrenheit or Fahrenheit to Celsius.
"""

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

print("Choose conversion direction:")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
choice = input("Enter 1 or 2: ").strip()

if choice == '1':
    scale = 'C'
    convert_func = celsius_to_fahrenheit
    convert_msg = "Temperatures in Fahrenheit (after removing the last value):"
elif choice == '2':
    scale = 'F'
    convert_func = fahrenheit_to_celsius
    convert_msg = "Temperatures in Celsius (after removing the last value):"
else:
    print("Invalid choice.")
    exit()

# Step 2: Collect 5 temperatures and store in tuple
temperatures = []
for i in range(5):
    temp = float(input(f"Enter temperature {i+1} in {scale}: "))
    temperatures.append(temp)
temperatures_tuple = tuple(temperatures)

# Step 3: Convert all temperatures
converted_temps = tuple(convert_func(temp) for temp in temperatures_tuple)

# Step 4: Delete the last value
temps_list = list(converted_temps)
temps_list.pop()
final_temps_tuple = tuple(temps_list)

# Step 5: Display the result
print(convert_msg, final_temps_tuple)