import re

# ─────────────────────────────────────────
#  Rule-Based Chatbot
#  Logic: match user input against keyword
#  patterns and return a mapped response.
# ─────────────────────────────────────────

# Each rule is a (compiled regex pattern, response) pair.
# Patterns are checked top-to-bottom; first match wins.
RULES = [
    # Greetings
    (re.compile(r"\b(hi|hello|hey|howdy|hola)\b", re.I),
     "Hey there! How can I help you today?"),

    # How are you
    (re.compile(r"\bhow are you\b|\bhow r u\b|\bwhat's up\b|\bwassup\b", re.I),
     "I'm just a bot, but I'm doing great! What about you?"),

    # Name
    (re.compile(r"\bwhat('s| is) your name\b|\bwho are you\b", re.I),
     "I'm RuleBot -- a simple rule-based chatbot built in Python."),

    # Age
    (re.compile(r"\bhow old are you\b|\bwhat('s| is) your age\b", re.I),
     "I was born the moment this script ran, so I'm pretty young!"),

    # Creator
    (re.compile(r"\bwho (made|created|built) you\b", re.I),
     "I was built by a Python developer as a rule-based chatbot project."),

    # Help
    (re.compile(r"\bhelp\b|\bwhat can you do\b", re.I),
     "I can chat about greetings, answer basic questions, and keep you company! Try saying hi."),

    # Time
    (re.compile(r"\bwhat time is it\b|\bwhat('s| is) the time\b", re.I),
     "I don't have a clock, but your device can tell you the exact time!"),

    # Date
    (re.compile(r"\bwhat('s| is) (today's |the )?date\b|\bwhat day is (it|today)\b", re.I),
     "Check your calendar -- I'm not connected to live data!"),

    # Weather
    (re.compile(r"\bweather\b|\btemperature\b", re.I),
     "I can't check live weather, but try weather.com or just look outside!"),

    # Jokes
    (re.compile(r"\btell me a joke\b|\bsay something funny\b|\bjoke\b", re.I),
     "Why do programmers prefer dark mode? Because light attracts bugs!"),

    # Thanks
    (re.compile(r"\bthank(s| you)\b|\bthx\b|\bty\b", re.I),
     "You're welcome! Anything else I can help with?"),

    # Goodbye
    (re.compile(r"\b(bye|goodbye|see you|cya|quit|exit)\b", re.I),
     "Goodbye! Have a great day!"),
]

# Fallback response when no rule matches
FALLBACK = "Hmm, I'm not sure about that. Try asking something else or type 'help'."


def get_response(user_input):
    # Check each rule in order; return the first matching response
    for pattern, response in RULES:
        if pattern.search(user_input):
            return response
    # No rule matched -> return fallback
    return FALLBACK


def is_exit(user_input):
    # Return True if the user wants to quit
    return bool(re.search(r"\b(bye|goodbye|quit|exit|cya)\b", user_input, re.I))


def main():
    print("=============================================")
    print("  Welcome to RuleBot")
    print("  Type 'bye' or 'exit' to quit.")
    print("=============================================")

    while True:
        user_input = input("\nYou: ").strip()

        # Skip empty input
        if not user_input:
            continue

        response = get_response(user_input)
        print("RuleBot:", response)

        # Exit loop on goodbye keywords
        if is_exit(user_input):
            break


if __name__ == "__main__":
    main()
