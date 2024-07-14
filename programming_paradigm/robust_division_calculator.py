
def safe_divide(numerator, denominator):
    try:
        float(numerator)
        float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only"
    
    try:
        result = numerator / denominator
        return f"The result of the division is {result}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."