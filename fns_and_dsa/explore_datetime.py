from datetime import datetime, timedelta

def calculate_future_date():
    future_date = int(input("Enter the number of days to add to the current date: "))
    return timedelta(days=future_date)

def display_current_datetime():
    current_date = datetime.now()

    days = calculate_future_date()
    new_date = current_date + days
    new_date.strftime('%Y-%m-%d %H:%M:%S')

    print(f"Future date: {new_date.date()}")

if __name__ == "__main__":
    display_current_datetime()
