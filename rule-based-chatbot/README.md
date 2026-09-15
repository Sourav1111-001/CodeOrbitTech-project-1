# Rule-Based Chatbot 🤖

A simple Python chatbot that responds to user input using predefined keyword rules — no ML or APIs needed.

## Features
- Handles greetings, common questions, jokes, and farewells
- Pattern matching with Python `re` (regex)
- Clean fallback for unknown input
- Fully commented code explaining every decision

## Project Structure
```
rule-based-chatbot/
├── chatbot.py        # Core chatbot logic
├── README.md         # This file
└── demo/
    └── chatbot-demo.mp4  # Screen recording of the chatbot in action
```

## How It Works
1. User types a message.
2. The input is matched against a list of regex patterns (top-to-bottom).
3. The **first matching rule** returns its response.
4. If **no rule matches**, a fallback message is shown.

## Run Locally
```bash
# No dependencies — uses Python standard library only
python chatbot.py
```

## Sample Conversation
```
You: hello
RuleBot: Hey there! 👋 How can I help you today?

You: tell me a joke
RuleBot: Why do programmers prefer dark mode? Because light attracts bugs! 🐛😂

You: what's the weather?
RuleBot: I can't check live weather, but try weather.com or just look outside! 🌤️

You: bye
RuleBot: Goodbye! Have a great day! 👋
```

## Supported Keywords / Topics
| Topic | Example Input |
|-------|--------------|
| Greetings | hi, hello, hey |
| Status | how are you, what's up |
| Identity | what's your name, who are you |
| Help | help, what can you do |
| Jokes | tell me a joke |
| Time/Date | what time is it, what's the date |
| Weather | weather, temperature |
| Farewell | bye, exit, quit |

## Tech Stack
- Python 3.x
- `re` module (standard library)
