from datetime import datetime, timedelta

def calculate_future_date():
    future_date = int(input("Enter the number of days to add to the current date: "))
    return timedelta(days=future_date)

def display_current_datetime():
    current_date = datetime.now()
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")

    days = calculate_future_date()
    future_date = current_date + days
    future_date.strftime('%Y-%m-%d')

    print(f"Future date: {future_date}")

if __name__ == "__main__":
    display_current_datetime()
