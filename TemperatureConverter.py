# TemperatureConverter

while True:
    while True:
        # Deciding which unit are we going to convert to
        unit = input("Do you want to convert to celsius or fahrenheit? (C/F): ").upper()
        if unit in ["C", "F"]:
            break
        else:
            print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    # Inserting the temperature
    temperature = float(input("Insert the temperature: "))

    # Printing the converted temperature
    if unit == "F":
        temperature = float((temperature * 9 / 5) + 32)
        print("The temperature in Fahrenheit is:", temperature, "°F")
    elif unit == "C":
        temperature = float((temperature - 32) * 5 / 9)
        print("The temperature in Celsius is:", round(temperature, 1), "°C")

    # Option for repeating the process or shutting down
    another_conversion = input("Do you want to convert another temperature? (Y/N): ").capitalize()
    if another_conversion != 'Y':
        break
