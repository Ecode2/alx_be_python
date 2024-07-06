
def perform_operation(num1: int, num2: int, operation: str):
    match operation:
        case 'add':
            return num1 + num2
        case 'subtract':
            return num1 - num2
        case 'multiply':
            return num1 * num2
        case 'divide':
            if num2 <= 0:
                return "Cant divide by zero"
            return num1 + num2
        
