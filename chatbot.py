"""
Task 4: Basic Rule-Based Chatbot
Concepts used: if-elif, functions, loops, input/output
"""


def get_response(user_input):
    """Takes user input (a string) and returns a predefined reply
    based on simple if-elif matching."""

    # Normalize the input: lowercase + strip extra spaces
    text = user_input.lower().strip()

    if text in ("hello", "hi", "hey"):
        return "Hi!"
    elif text in ("how are you", "how are you?"):
        return "I'm fine, thanks!"
    elif text in ("bye", "goodbye", "exit", "quit"):
        return "Goodbye!"
    elif text in ("what is your name", "what is your name?"):
        return "I'm a simple chatbot created in Python."
    elif text == "":
        return "Please type something."
    else:
        return "Sorry, I don't understand that. Try 'hello', 'how are you', or 'bye'."


def chat():
    """Runs the chatbot loop: keeps taking input until the user says bye/exit/quit."""

    print("Chatbot: Hello! Type 'bye' to end the chat.\n")

    while True:
        user_input = input("You: ")

        response = get_response(user_input)
        print("Chatbot:", response)

        # End the loop when the user wants to leave
        if user_input.lower().strip() in ("bye", "goodbye", "exit", "quit"):
            break


if __name__ == "__main__":
    chat()
