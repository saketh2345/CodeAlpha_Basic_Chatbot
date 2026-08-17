"""
Task 4: Advanced Basic Rule-Based Chatbot
Concepts Used:
if-elif, functions, loops, input/output,
basic arithmetic, string handling
"""

from datetime import datetime


# --------------------------------------------------
# CALCULATOR FUNCTION
# --------------------------------------------------

def calculator():
    print("\nCalculator Mode")
    print("Available operations:")
    print("+  Addition")
    print("-  Subtraction")
    print("*  Multiplication")
    print("/  Division")
    print("%  Modulus")
    print("** Power")
    print("Type 'back' to return to chatbot.\n")

    while True:
        expression = input("Calculate: ").strip()

        if expression.lower() == "back":
            print("Returning to chatbot...\n")
            break

        try:
            parts = expression.split()

            if len(parts) != 3:
                print("Please enter like: 10 + 5")
                continue

            num1 = float(parts[0])
            operator = parts[1]
            num2 = float(parts[2])

            if operator == "+":
                result = num1 + num2

            elif operator == "-":
                result = num1 - num2

            elif operator == "*":
                result = num1 * num2

            elif operator == "/":
                if num2 == 0:
                    print("Cannot divide by zero.")
                    continue
                result = num1 / num2

            elif operator == "%":
                result = num1 % num2

            elif operator == "**":
                result = num1 ** num2

            else:
                print("Invalid operator.")
                continue

            # Display integer without .0
            if result.is_integer():
                result = int(result)

            print("Result:", result)

        except ValueError:
            print("Please enter valid numbers.")
            print("Example: 25 * 4")


# --------------------------------------------------
# RESPONSE FUNCTION
# --------------------------------------------------

def get_response(user_input):
    """Returns a predefined response based on user input."""

    text = user_input.lower().strip()

    # Greetings
    if text in ("hello", "hi", "hey", "hai", "hii"):
        return "Hi! Nice to meet you! How can I help you?"

    elif text in ("good morning", "morning"):
        return "Good morning! Have a great day!"

    elif text in ("good afternoon", "afternoon"):
        return "Good afternoon! How is your day going?"

    elif text in ("good evening", "evening"):
        return "Good evening! What can I do for you?"

    # General conversation
    elif text in ("how are you", "how are you?"):
        return "I'm doing great! Thanks for asking."

    elif text in ("what are you doing", "what are you doing?"):
        return "I'm chatting with you and waiting for your next command!"

    elif text in ("who are you", "who are you?"):
        return "I'm a simple rule-based chatbot created using Python."

    elif text in ("what is your name", "what is your name?"):
        return "My name is PyBot!"

    elif text in ("thank you", "thanks", "thank"):
        return "You're welcome! Happy to help."

    elif text in ("nice", "great", "awesome"):
        return "Glad you think so!"

    # Help
    elif text in ("help", "commands", "menu"):
        return (
            "Here are some things I can do:\n"
            "1. Chat with you\n"
            "2. Perform calculations\n"
            "3. Tell the current date and time\n"
            "4. Tell a joke\n"
            "5. Tell you about myself\n"
            "6. Exit the chatbot"
        )

    # Calculator
    elif text in ("calculate", "calculator", "math"):
        calculator()
        return "What else can I do for you?"

    # Date and time
    elif text in ("time", "what time is it", "what is the time"):
        current_time = datetime.now().strftime("%I:%M:%S %p")
        return "The current time is " + current_time

    elif text in ("date", "what is today's date", "today's date"):
        current_date = datetime.now().strftime("%d-%m-%Y")
        return "Today's date is " + current_date

    elif text in ("date and time", "datetime"):
        current_datetime = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
        return "Current date and time: " + current_datetime

    # Jokes
    elif text in ("joke", "tell me a joke", "tell joke"):
        return "Why do programmers prefer dark mode? Because light attracts bugs!"

    elif text == "another joke":
        return "Why was the computer cold? Because it left its Windows open!"

    # Simple knowledge
    elif text in ("what is python", "python"):
        return "Python is a popular programming language known for its simple and readable syntax."

    elif text in ("what is ai", "ai"):
        return "AI stands for Artificial Intelligence. It allows computers to perform tasks that normally require human intelligence."

    # Exit
    elif text in ("bye", "goodbye", "exit", "quit"):
        return "Goodbye! It was nice chatting with you."

    # Empty input
    elif text == "":
        return "Please type something."

    # Unknown input
    else:
        return (
            "Sorry, I don't understand that.\n"
            "Type 'help' to see what I can do."
        )


# --------------------------------------------------
# MAIN CHAT FUNCTION
# --------------------------------------------------

def chat():
    print("=" * 50)
    print("          PYBOT - PYTHON CHATBOT")
    print("=" * 50)

    print("PyBot: Hello! I'm PyBot.")
    print("PyBot: Type 'help' to see my commands.")
    print("PyBot: Type 'bye' to exit.\n")

    while True:

        user_input = input("You: ")

        response = get_response(user_input)

        print("PyBot:", response)

        # Stop chatbot
        if user_input.lower().strip() in (
            "bye",
            "goodbye",
            "exit",
            "quit"
        ):
            break

        print()


# --------------------------------------------------
# START PROGRAM
# --------------------------------------------------

if __name__ == "__main__":
    chat()
