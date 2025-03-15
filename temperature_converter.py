# Program welcome message
print("Welcome to the Temperature Converter!")
print("Convert between Celsius and Fahrenheit easily.")
print()

def c_to_f(celsius):
    """Converts input (celsius) to fahrenheit"""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
def f_to_c(fahrenheit):
    """Converts input (fahrenheit) to celsius"""
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Main program loop
while True:
    print("Menu:")
    print("1. Convert from Celsius to Fahrenheit")
    print("2. Convert from Fahrenheit to Celsius")
    print("3. Exit")
    
    try:
        userInput = int(input("Enter your choice (1-3): "))
        print()

        
        if userInput == 1:
            while True:
                try:
                    celsius = float(input("Enter a temperature to convert to fahrenheit: "))
                    result = round(c_to_f(celsius),1)
                    print(f"{celsius}°C is {result}°F")
                    print()
                    break
                except ValueError:
                    print("Invalid input, please enter a temperature value.")        
        
        elif userInput == 2:
            while True:
                try:
                    fahrenheit = float(input("Enter a temperature to convert to celsius: "))
                    result = round(f_to_c(fahrenheit),1)
                    print(f"{fahrenheit}°F is {result}°C")
                    print()
                    break
                except ValueError:
                    print("Invalid input, please enter a temperature value.") 
        
        elif userInput == 3:
            print("Goodbye")
            break
        
        else:
            print("Please choose a valid menu option (1, 2 or 3)")
    except ValueError:
        print("Invalid input, please try again")
        print()
