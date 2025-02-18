import time

def get_duration(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

def start_timer(duration, message):
    print(f"{message} for {duration} minutes.")
    time.sleep(duration * 60)
    print(f"{message} is over.")

def main():
    session_duration = get_duration("Enter the duration of the session (in minutes): ")
    break_duration = get_duration("Enter the duration of the break (in minutes): ")
    num_sessions = get_duration("Enter the number of sessions: ")

    for session in range(1, num_sessions + 1):
        print(f"Session {session} of {num_sessions}")
        start_timer(session_duration, "Work session")
        if session < num_sessions:
            start_timer(break_duration, "Break")

    print("All sessions are complete. Great job!")

if __name__ == "__main__":
    main()