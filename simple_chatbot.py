import datetime

responses = {
    "hello": "Hello! How can I help you today?",
    "hi": "Hi there! What’s on your mind?",
    "weather": "I'm not sure about the weather, but it’s always a good day to code!",
    "time": f"The current time is {datetime.datetime.now().strftime('%H:%M')}.",
    "day": f"Today is {datetime.datetime.now().strftime('%A')}.",
    "python": "Python is a versatile programming language, great for web development, data science, and more.",
    "bye": "Bye! Have a great day!",
}

def get_response(user_input):
    user_input = user_input.lower()
    
    for keyword in responses:
        if keyword in user_input:
            return responses[keyword]
    
    return "I'm sorry, I don't understand. Could you ask something else?"


def chatbot():
    print("Chatbot: Hello! I'm here to chat. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "bye":
            print("Chatbot:", responses["bye"])
            break
        
        response = get_response(user_input)
        print("Chatbot:", response)

chatbot()
