# ================================================
#   SIMPLE RULE-BASED CHATBOT - TASK 4
#   Concepts: if-elif, functions, loops, input/output
# ================================================

def greet():
    """Say hello when the user starts chatting"""
    print("🤖 Chatbot: Hello! I'm your friendly Python chatbot.")
    print("   Type 'bye' to end the chat.\n")

def get_response(user_input):
    """Return a predefined reply based on user message"""
    user_input = user_input.lower().strip()  # Make it case-insensitive

    # Rule-based responses
    if "hello" in user_input or "hi" in user_input or "hey" in user_input:
        return "Hi there! How can I help you today?"

    elif "how are you" in user_input or "how do you do" in user_input:
        return "I'm doing great, thank you! I'm here to chat with you 😊"

    elif "what is your name" in user_input or "who are you" in user_input:
        return "I'm Chatty, your friendly Python chatbot!"

    elif "what can you do" in user_input or "help" in user_input:
        return "I can chat with you! Try saying:\n- hello\n- how are you\n- what's your name\n- bye"

    elif "bye" in user_input or "goodbye" in user_input or "exit" in user_input:
        return "Goodbye! Have a wonderful day! 👋"

    elif "thank you" in user_input or "thanks" in user_input:
        return "You're very welcome! 😄"

    else:
        return "I'm sorry, I don't understand that yet. Try saying 'hello' or 'how are you'!"

def chatbot():
    """Main function to run the chatbot with a loop"""
    greet()

    print("Start chatting below (type 'bye' to quit):\n")

    while True:
        try:
            user_input = input("You: ").strip()

            # Check if user wants to quit
            if user_input.lower() in ["bye", "goodbye", "exit", "quit"]:
                print("🤖 Chatbot:", get_response(user_input))
                print("\nChat ended. Thank you for talking to me! 💜\n")
                break

            # Get and display response
            response = get_response(user_input)
            print("🤖 Chatbot:", response, "\n")

        except KeyboardInterrupt:
            print("\n\nChat interrupted. Goodbye!")
            break
        except EOFError:
            print("\n\nGoodbye!")
            break

# ================================================
#   Start the chatbot when script is run
# ================================================
if __name__ == "__main__":
    print("=" * 50)
    print("   WELCOME TO CHATTY - YOUR PYTHON CHATBOT")
    print("=" * 50)
    chatbot()