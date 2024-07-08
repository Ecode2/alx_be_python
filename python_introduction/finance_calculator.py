# finance_calculator.py

def main():
    # Prompt the user for their monthly income
    monthly_income = float(input("Enter your monthly income: "))
    
    # Ask for their total monthly expenses
    total_expenses = float(input("Enter your total monthly expenses: "))
    
    # Calculate monthly savings
    monthly_savings = monthly_income - total_expenses
    
    # Assume a simple annual interest rate of 5%
    annual_interest_rate = 0.05
    
    # Calculate projected savings after one year with interest
    annual_savings = monthly_savings * 12
    projected_savings = annual_savings + (annual_savings * annual_interest_rate)
    
    # Display the results
    print(f"Your monthly savings are ${monthly_savings}.")
    print(f"Projected savings after one year, with interest, is: ${projected_savings}.")

if __name__ == "__main__":
    main()
