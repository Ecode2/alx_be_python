FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    conversion = FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit - 32)
    print(f"{fahrenheit}°F is {conversion}°C")

def convert_to_fahrenheit(celsius):
    conversion = (CELSIUS_TO_FAHRENHEIT_FACTOR*celsius) + 32
    print(f"{celsius}°C is {conversion}°F")

if __name__=="__main__":
    temprature = int(input("Enter the temperature to convert: "))
    tempType = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()

    match tempType:
        case "c":
            convert_to_fahrenheit(temprature)
        case "f":
            convert_to_celsius(temprature)
        case _:
            print("Conversion type not supported")
