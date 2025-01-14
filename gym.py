class WorkoutSession:
    def __init__(self, sets, reps, weight):
        self.sets = sets
        self.reps = reps
        self.weight = weight

    def __str__(self):
        return f"{self.sets} sets of {self.reps} reps at {self.weight} kg"


class Exercise:
    def __init__(self, name):
        self.name = name
        self.workouts = []

    def add_workout(self, workout):
        self.workouts.append(workout)

    def get_progress(self):
        if not self.workouts:
            return f"No progress for {self.name} yet."
        progress = [f"Session {i+1}: {workout}" for i, workout in enumerate(self.workouts)]
        return f"Progress for {self.name}:\n" + "\n".join(progress)


class GymTracker:
    def __init__(self):
        self.exercises = {}

    def add_exercise(self, name):
        if name.lower() in self.exercises:
            print(f"Exercise {name} already exists.")
        else:
            self.exercises[name.lower()] = Exercise(name)
            print(f"Added exercise: {name.capitalize()}")

    def log_workout(self, name, sets, reps, weight):
        exercise = self.exercises.get(name.lower())
        if not exercise:
            print(f"Exercise {name} not found. Please add it first.")
        else:
            workout = WorkoutSession(sets, reps, weight)
            exercise.add_workout(workout)
            print(f"Logged {workout} for {exercise.name.capitalize()}.")

    def view_progress(self):
        if not self.exercises:
            print("No exercises found. Please add some first.")
            return
        for exercise in self.exercises.values():
            print(exercise.get_progress())

    def show_menu(self):
        while True:
            print("\nGym Tracker Options:")
            print("1. Add Exercise")
            print("2. Log Workout")
            print("3. View Progress")
            print("4. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                name = input("Enter exercise name: ").strip()
                self.add_exercise(name)

            elif choice == "2":
                name = input("Enter exercise name: ").strip()
                try:
                    sets = int(input("Enter number of sets: "))
                    reps = int(input("Enter number of reps: "))
                    weight = float(input("Enter weight in kg: "))
                    self.log_workout(name, sets, reps, weight)
                except ValueError:
                    print("Invalid input. Please enter numeric values for sets, reps, and weight.")

            elif choice == "3":
                self.view_progress()

            elif choice == "4":
                print("Exiting Gym Tracker. Goodbye!")
                break

            else:
                print("Invalid option. Please try again.")


if __name__ == "__main__":
    tracker = GymTracker()
    tracker.show_menu()
