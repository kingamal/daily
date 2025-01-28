import random

self_care_activities = [
    "Take a short walk in nature. 🌿",
    "Drink a big glass of water. 💧",
    "Do some deep breathing for 5 minutes. 🧘‍♂️",
    "Listen to your favorite music. 🎵",
    "Write down three things you're grateful for. ✨",
    "Read a chapter from a book you love. 📚",
    "Stretch your body gently. 🤸‍♀️",
    "Spend a few minutes with a pet or a loved one. 🐾",
    "Watch the sunset or sunrise. 🌅"
]

def self_care():
    activity = random.choice(self_care_activities)
    print(activity)

if __name__ == "__main__":
    self_care()