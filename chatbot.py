# Sample code for a rule-based chatbot in Python

def respond_to_query(user_input):
    if "hello" in user_input:
        return "Hello! How can I assist you today?"
    elif "help" in user_input:
        return "Sure, I'm here to help. What do you need assistance with?"
    elif "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    elif "weather" in user_input:
        return "The weather today is sunny with a high of 75°F."
    elif "news" in user_input:
        return "Here are the latest headlines: [Headline 1], [Headline 2], [Headline 3]"
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase?"

def main():
    print("Welcome to the Chatbot!")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        else:
            response = respond_to_query(user_input.lower())
            print("Chatbot:", response)

if __name__ == "__main__":
    main()