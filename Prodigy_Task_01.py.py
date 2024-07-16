def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5/9

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin * 9/5) - 459.67

def main():
    print("Temperature Unit Converter")

    # Get input temperature and unit from the user
    temperature = float(input("Enter temperature value: "))
    original_unit = input("Enter original unit (Celsius, Fahrenheit, or Kelvin): ").lower()

    # Perform conversions
    if original_unit == 'celsius':
        fahrenheit = celsius_to_fahrenheit(temperature)
        kelvin = celsius_to_kelvin(temperature)
    elif original_unit == 'fahrenheit':
        celsius = fahrenheit_to_celsius(temperature)
        kelvin = fahrenheit_to_kelvin(temperature)
    elif original_unit == 'kelvin':
        celsius = kelvin_to_celsius(temperature)
        fahrenheit = kelvin_to_fahrenheit(temperature)
    else:
        print("Invalid unit. Please enter Celsius, Fahrenheit, or Kelvin.")
        return

    # Display the converted temperatures
    print(f"\nConverted Temperatures:")
    if original_unit != 'celsius':
        print(f"{temperature} {original_unit.capitalize()} is {celsius:.2f} Celsius.")
    if original_unit != 'fahrenheit':
        print(f"{temperature} {original_unit.capitalize()} is {fahrenheit:.2f} Fahrenheit.")
    if original_unit != 'kelvin':
        print(f"{temperature} {original_unit.capitalize()} is {kelvin:.2f} Kelvin.")

if __name__ == "__main__":
    main()
    print("Hello Everyone")