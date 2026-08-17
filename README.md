# Basic Rule-Based Chatbot 🤖

A simple **Python-based rule-based chatbot** that interacts with users through the command line and provides predefined responses based on their input.

This project is designed for beginners and demonstrates fundamental Python concepts including `if-elif` statements, functions, loops, string handling, and input/output.

## Features

* 🤖 Interactive command-line chatbot
* 👋 Responds to greetings such as `hello`, `hi`, and `hey`
* 💬 Responds to basic questions
* 🏷️ Provides its name when asked
* 🚪 Supports exit commands such as `bye`, `exit`, and `quit`
* 🔤 Normalizes user input by converting it to lowercase and removing extra spaces
* ⚠️ Handles empty or unknown input
* 🔄 Continuously runs until the user chooses to exit

The chatbot normalizes the user's input before checking it against predefined responses.

## Requirements

* Python 3.x
* No external libraries are required.

The chatbot uses only basic Python functionality.

## How to Run

1. Clone this repository:

```bash
git clone https://github.com/your-username/your-repository-name.git
```

2. Navigate to the project directory:

```bash
cd your-repository-name
```

3. Run the chatbot:

```bash
python chatbot.py
```

## How It Works

When the program starts, the chatbot displays a welcome message:

```text
Chatbot: Hello! Type 'bye' to end the chat.
```

The user can then enter a message.

The `get_response()` function checks the user's input and returns a predefined response based on matching conditions.

### Supported Inputs

| User Input             | Chatbot Response                          |
| ---------------------- | ----------------------------------------- |
| `hello` / `hi` / `hey` | `Hi!`                                     |
| `how are you`          | `I'm fine, thanks!`                       |
| `what is your name`    | `I'm a simple chatbot created in Python.` |
| `bye` / `goodbye`      | `Goodbye!`                                |
| `exit` / `quit`        | `Goodbye!`                                |
| Empty input            | `Please type something.`                  |
| Other input            | Displays an "I don't understand" message  |

These responses are defined directly in the `if-elif` logic of the program.

## Example Conversation

```text
Chatbot: Hello! Type 'bye' to end the chat.

You: hello
Chatbot: Hi!

You: how are you
Chatbot: I'm fine, thanks!

You: what is your name
Chatbot: I'm a simple chatbot created in Python.

You: bye
Chatbot: Goodbye!
```

## Input Normalization

Before processing the user's message, the program:

1. Converts the input to lowercase.
2. Removes extra spaces from the beginning and end.

For example:

```text
"  HELLO  "
```

is converted to:

```text
"hello"
```

This allows the chatbot to recognize inputs regardless of capitalization or surrounding spaces.

## Chat Loop

The `chat()` function continuously asks the user for input inside a `while` loop.

After receiving the input, it calls `get_response()` and displays the chatbot's response. The loop continues until the user enters `bye`, `goodbye`, `exit`, or `quit`.

## Project Structure

```text
.
├── chatbot.py
└── README.md
```

* **`chatbot.py`** — Main Python chatbot program.
* **`README.md`** — Project documentation.

## Concepts Demonstrated

This project demonstrates the following Python concepts:

* `if-elif-else` statements
* Functions
* `while` loops
* User input
* Output using `print()`
* String methods
* String comparison
* Input normalization
* Conditional logic

## Limitations

This is a **rule-based chatbot**, so it does not use artificial intelligence or machine learning.

It can only respond to the inputs and variations that have been explicitly defined in the program. Unknown questions receive a predefined fallback response.

## Future Improvements

Possible improvements include:

* Add more conversational responses
* Support more questions and commands
* Use a dictionary for storing responses
* Add random responses for more natural conversations
* Add conversation history
* Connect the chatbot to an AI API
* Create a graphical user interface
* Add voice input and output

## Author

Created as a beginner-friendly Python project for learning **conditional statements, functions, loops, and interactive user input**.

## License

This project is available for educational and personal use.
