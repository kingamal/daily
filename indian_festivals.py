import datetime

festivals = {
    "Diwali": "11-01",
    "Holi": "03-25",
    "Navratri": "10-03",
    "Raksha Bandhan": "08-19",
    "Eid": "04-10",
    "Pongal": "01-14",
}

def indian_festival_reminder(days_ahead=50):
    today = datetime.datetime.now()
    today_str = today.strftime("%m-%d")
    upcoming_festivals = []
    
    for festival, date in festivals.items():
        festival_date = datetime.datetime.strptime(f"{today.year}-{date}", "%Y-%m-%d")
        delta_days = (festival_date - today).days 
        
        if 0 <= delta_days <= days_ahead:
            upcoming_festivals.append((festival, delta_days))
    
    if upcoming_festivals:
        for festival, days in upcoming_festivals:
            if days == 0:
                print(f"Today is {festival} festival.")
            else:
                print(f"{festival} festival is coming up in {days} day(s). Get ready!")
    else:
        print("No festival coming up soon.")

if __name__ == "__main__":
    indian_festival_reminder()