
def display_quote():
    name = input("Hello! What's your name? ")

    print(f"Hi, {name}! How are you feeling today?")
    print("1. Happy 😄")
    print("2. Stressed 😣")
    print("3. Tired 😴")
    choice = int(input("Choose 1, 2, or 3: "))
    
    if choice == 1:
        print(f"That’s great, {name}! Keep streading your joy")
    elif choice == 2:
        print(f"Take a deep breath, {name}. You're doing amazing!")
    elif choice == 3:
        print(f"Rest up, {name}. Tomorrow is a fresh start!")
    else:
        print("Invalid choice. Please choose a number between 1 and 3.")

if __name__ == "__main__":
    display_quote()
