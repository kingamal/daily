import random

strength_exercises = ["Push-ups", "Squats", "Lunges", "Plank", "Dumbbell Press"]
cardio_exercises = ["Jumping Jacks", "Burpees", "Running in Place", "Jump Rope", "High Knees"]
flexibility_exercises = ["Yoga Stretch", "Hamstring Stretch", "Toe Touches", "Cat-Cow Stretch", "Shoulder Rolls"]

def get_workout_type():
    print("Welcome to the Workout Routine Generator!")
    while True:
        workout_type = input("Enter workout type (strength, cardio, flexibility): ").strip().lower()
        if workout_type in ["strength", "cardio", "flexibility"]:
            return workout_type
        else:
            print("Invalid input. Please enter 'strength', 'cardio', or 'flexibility'.")

def suggest_exercise(workout_type):
    if workout_type == "strength":
        exercise = random.choice(strength_exercises)
    elif workout_type == "cardio":
        exercise = random.choice(cardio_exercises)
    elif workout_type == "flexibility":
        exercise = random.choice(flexibility_exercises)
    
    print(f"Try this exercise: {exercise}")
    print("Stay active and keep moving!")

def main():
    workout_type = get_workout_type()
    suggest_exercise(workout_type)

if __name__ == "__main__":
    main()