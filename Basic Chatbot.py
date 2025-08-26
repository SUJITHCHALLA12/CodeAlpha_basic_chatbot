def chatbot_response(user_input):
    user_input = user_input.lower()  # make input case-insensitive

    if "hello" in user_input:
        return "Hi! How can I help you?"
    elif "how are you" in user_input:
        return "I'm fine, thanks for asking! How are you?"
    elif "i am fine" in user_input or "i'm fine" in user_input:
        return "Glad to hear that!"
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    elif "thank you" in user_input:
        return "You're welcome!"
    else:
        return "Sorry, I don't understand that."

def main():
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("Chatbot:", response)
        if "bye" in user_input.lower():
            break

if __name__ == "__main__":
    main()