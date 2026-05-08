print("Simple AI Chatbot")
print("Type 'bye' to exit\n")
while True:
    user = input("You: ").lower()
    if user == "hello":
        print("Bot: Hi!")
    elif user == "how are you":
        print("Bot: I am fine.")
    elif user == "your name":
        print("Bot: I am an AI chatbot.")
    elif user == "bye":
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: I don't understand.")