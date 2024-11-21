import datetime

def compare_dates():
    deadline = input('Enter the deadline (e.g., 2024-11-15 17:00): ')
    try:
        deadline = datetime.datetime.strptime(deadline, '%Y-%m-%d %H:%M:%S')
    except ValueError:
        try:
            deadline = datetime.datetime.strptime(deadline, '%Y-%m-%d %H:%M')
        except ValueError:
            print("Incorrect data format. Please use 'YYYY-MM-DD HH:MM' or 'YYYY-MM-DD HH:MM:SS'.")
            return
    
    todays_date = datetime.datetime.now()
    if deadline > todays_date:
        days_to_deadline = deadline - todays_date
        full_days = days_to_deadline.days
        print(f'The deadline is in {full_days} day(s). Keep working! 🚀')
    elif deadline < todays_date:
        print(f'The deadline has passed!😢')
    elif deadline == todays_date:
        print('The deadline is now!')
    else:
        print('Incorrect data was provided. Try again!')

compare_dates()
