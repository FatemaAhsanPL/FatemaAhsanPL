import random

class ChatBot:
    def __init__(self, name):
        self.name = name

    def greet(self):
        greetings = ["Hello!", "Hi there!", "Greetings!", "Nice to meet you!"]
        return random.choice(greetings)

    def farewell(self):
        farewells = ["Goodbye!", "Farewell!", "See you later!", "Take care!"]
        return random.choice(farewells)

    def respond(self, message):
        if "hello" in message.lower() or "hi" in message.lower():
            return self.greet()
        elif "goodbye" in message.lower() or "bye" in message.lower():
            return self.farewell()
        else:
            return "I'm sorry, I don't understand."

# Example usage
chatbot = ChatBot("Bot")
print(chatbot.greet())

while True:
    user_input = input("User: ")
    response = chatbot.respond(user_input)
    print(f"{chatbot.name}: {response}")

    if "bye" in user_input.lower():
        print(chatbot.farewell())
        break
