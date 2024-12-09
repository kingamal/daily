import os
import time
from datetime import datetime, timedelta

def get_file_age_category(file_path):
    """
    Categorize a file based on its age relative to the current time.
    """
    file_creation_time = os.path.getctime(file_path)
    file_age_in_seconds = time.time() - file_creation_time

    if file_age_in_seconds < 7 * 24 * 60 * 60:
        return "less_than_a_week"
    elif file_age_in_seconds < 30 * 24 * 60 * 60:
        return "between_a_week_and_a_month"
    else:
        return "older_than_a_month"

def analyze_file_ages(folder_path):
    """
    Analyze the files in the given folder and categorize them by age.
    """
    categories = {
        "less_than_a_week": 0,
        "between_a_week_and_a_month": 0,
        "older_than_a_month": 0
    }
    oldest_file = None
    newest_file = None
    oldest_file_time = float("inf")
    newest_file_time = 0

    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                creation_time = os.path.getctime(file_path)

                if creation_time < oldest_file_time:
                    oldest_file_time = creation_time
                    oldest_file = file_path
                if creation_time > newest_file_time:
                    newest_file_time = creation_time
                    newest_file = file_path

                category = get_file_age_category(file_path)
                categories[category] += 1

            except OSError:
                print(f"Could not access file: {file_path}")

    return categories, oldest_file, newest_file

def format_time(timestamp):
    """
    Convert a timestamp to a human-readable date.
    """
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

def main():
    print("Welcome to File Age Analyzer!")
    folder_path = input("Enter the path of the folder to analyze: ").strip()

    if not os.path.exists(folder_path):
        print("Error: The specified folder does not exist.")
        return

    print("Analyzing file ages. Please wait...\n")

    categories, oldest_file, newest_file = analyze_file_ages(folder_path)

    print("--- File Age Analysis Report ---")
    print(f"Files created less than a week ago: {categories['less_than_a_week']}")
    print(f"Files created between a week and a month ago: {categories['between_a_week_and_a_month']}")
    print(f"Files created more than a month ago: {categories['older_than_a_month']}")
    print()
    if oldest_file:
        print(f"Oldest file: {oldest_file} (Created on {format_time(os.path.getctime(oldest_file))})")
    else:
        print("Oldest file: Not found")
    if newest_file:
        print(f"Newest file: {newest_file} (Created on {format_time(os.path.getctime(newest_file))})")
    else:
        print("Newest file: Not found")

    print("\nAnalysis complete!")

if __name__ == "__main__":
    main()
