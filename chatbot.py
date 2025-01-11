def chatbot():
    responses = {
        "hello": "Hi there! How can I assist you today?",
        "hi": "Hello! How can I help you?",
        "how are you": "I'm just a program, but I'm functioning perfectly! How about you?",
        "your name": "I'm your friendly Python chatbot. What's your name?",
        "weather": "I can't provide real-time weather updates, but you can check a weather app!",
        "thank you": "You're welcome! Let me know if there's anything else I can help with.",
        "exit": "Goodbye! Have a great day!"
    }

    print("Chatbot: Hello! I'm here to assist you. Type 'exit' to end the chat.\n")

    while True:
        user_input = input("You: ").strip().lower()
        
        if user_input in responses:
            print(f"Chatbot: {responses[user_input]}")
            
            if user_input == "exit":
                break
        else:
            print("Chatbot: Sorry, I don't understand that. Could you try rephrasing?")
            

chatbot()
