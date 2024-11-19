import random
import datetime

def read_quotes(file_path):
    """Reads quotes from a text file and returns them as a list."""
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            quotes = [line.strip() for line in file if line.strip()]
        return quotes
    except FileNotFoundError:
        print("Error: quotes.txt file not found.")
        return []

def display_quote():
    """Displays a motivational quote depending on the day of the week."""
    today = datetime.datetime.now().strftime("%A")
    quotes = read_quotes("quotes.txt")
    
    if today == "Monday":
        if quotes:
            quote = random.choice(quotes)
            print("It's Monday! Time for some motivation!")
            print("💡 Motivational Quote of the Day 💡")
            print(f'{quote}')
        else:
            print("No quotes available. Add some to your quotes.txt!")
    else:
        print(f"Today is {today}!")

if __name__ == "__main__":
    display_quote()
