import datetime

def calculate_future_date():
    future_date = int(input("Enter the number of days to add to the current date: "))
    return datetime.timedelta(days=future_date)

def display_current_datetime():
    current_date = datetime.datetime.utcnow()
    print(current_date)

    days = calculate_future_date()
    new_date = current_date + days

    print(f"Future date: {new_date.date()}")

if __name__ == "__main__":
    display_current_datetime()