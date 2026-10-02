print("====================================")
print("      Welcome to My AI Chatbot")
print("====================================")
print("Type 'bye', 'exit', or 'quit' to stop.\n")

while True:
    user_input = input("You: ").lower().strip()

    if user_input in ["hello", "hi", "hey"]:
        print("Bot: Hello! How can I help you?")

    elif user_input in ["how are you", "how are you?"]:
        print("Bot: I'm doing great! Thanks for asking.")

    elif user_input in ["what is ai", "what is ai?"]:
        print("Bot: AI stands for Artificial Intelligence. It enables machines to perform tasks that normally require human intelligence.")

    elif user_input in ["what can you do", "what can you do?"]:
        print("Bot: I can answer a set of predefined questions using rule-based logic.")

    elif user_input in ["who are you", "who are you?"]:
        print("Bot: I'm a simple rule-based AI chatbot created using Python.")

    elif user_input in ["thanks", "thank you"]:
        print("Bot: You're welcome!")

    elif user_input in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a great day!")
        break

    else:
        print("Bot: Sorry, I don't understand that. Please try another question.")