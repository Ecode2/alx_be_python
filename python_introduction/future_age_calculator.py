# future_age_calculator.py

def main():
    # Prompt the user for their current age
    current_age = int(input("How old are you? "))
    
    # Calculate the age in the year 2050
    age_in_2050 = current_age + 27  # Since 2050 is 27 years from 2023
    
    # Print the result
    print(f"In 2050, you will be {age_in_2050} years old.")

if __name__ == "__main__":
    main()
