

def convert_temperature(value, scale):
    if scale.lower() == "c":
        return (value * 9/5) + 32  # Celsius to Fahrenheit
    elif scale.lower() == "f":
        return (value - 32) * 5/9  # Fahrenheit to Celsius
    else:
        return "Invalid scale! Use 'C' or 'F'."

temp = float(input("Enter temperature value: "))
scale = input("Enter scale (C/F): ")
print("Converted value:", convert_temperature(temp, scale))
