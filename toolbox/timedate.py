from datetime import datetime,date

def current_time():
    now = datetime.now()
    current_time = now.strftime('%H:%M:%S')

    return current_time

def current_date():
    day = date.today()
    today = day.strftime('%d/%m/%Y')

    return today
