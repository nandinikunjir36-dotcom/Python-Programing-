from Temperature import celsius_to_fahrenheit
from Temperature import fahrenheit_to_celsius
from Temperature import celsius_to_kelvin

def main():
    while True:
        print("\nTemperature Conversion Program.")
        print("1.Celsius to Fahrenheit.")
        print("2.Fahrenhiet to Celsius.")
        print("3.Celsius to Kelvin.")
        print("4.Exit.")
    
        try:
            choice = int(input("Enter your choice(1-4):"))
        
            if choice == 1:
                c = float(input("Enter Temperature in Celsius:"))
                print("Fahrenheit:", celsius_to_fahrenheit.convert(c))
            elif choice == 2:
                f = float(input("Enter Temperature in Fahrenheit:"))
                print("Celsius:", fahrenheit_to_celsius.convert(f))
            elif choice == 3:
                c = float(input("Enter Temperature in Celsius:"))
                print("Kelvin:", celsius_to_kelvin.convert(c))
            elif choice == 4:
                print("Exiting Program...")
                break
            else:
                print("Invalid choice! Please try again.")
        except ValueError:
            print("Invalid value! Please enter numeric values.")
if __name__=="__main__":
    main()