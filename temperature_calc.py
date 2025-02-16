def celsius_to_fahrenheit(celsius):
    return (celsius * 9/2) +32 

def celsius_to_kelvin(celcius):
    return ( celcius + 237.15)

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_celsius(kelvin):
    return (kelvin - 273.15)

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

def convert_temp():
    print("Welcome to the Temperature Conversion Program!")
    print("Please select the temperature scale you want to convert from: C for Celsius ,F for Fahrenheit ,K for Kelvin ")
    
    choice = input("Enter 'C', 'F', or 'K' to select the scale: ").upper()

    if choice == 'C':
        temp = float(input("Enter the temperature in Celsius: "))
        print(f"{temp}°C is equal to {celsius_to_fahrenheit(temp):.2f}°F and {celsius_to_kelvin(temp):.2f}K")

    elif choice == 'F':
        temp = float(input("Enter the temperature in Fahrenheit: "))
        print(f"{temp}°C is equal to {fahrenheit_to_celsius(temp):.2f}°F and {fahrenheit_to_kelvin(temp):.2f}K")

    elif choice == 'k':
        temp = float(input("Enter the temperature in Kelvin: "))
        print(f"{temp}°C is equal to {kelvin_to_celsius(temp):.2f}°F and {kelvin_to_fahrenheit(temp):.2f}K")

    else:
        print("Invalid choice. Please enter 'C', 'F', or 'K'.")

    # another conversion
    another_conversion = input("Would you like to convert another temperature? (yes/no): ").lower()
    if another_conversion == "yes":
        convert_temp()
    else:
        print("Thank you for using the Temperature Conversion Program! Goodbye.")

convert_temp()
