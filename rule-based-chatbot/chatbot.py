import re
import tkinter as tk
from tkinter import scrolledtext

# ─────────────────────────────────────────
#  Rule-Based Chatbot - GUI Version
#  Uses tkinter for a clean chat interface
# ─────────────────────────────────────────

RULES = [
    (re.compile(r"\b(hi|hello|hey|howdy|hola)\b", re.I),
     "Hey there! 👋 How can I help you today?"),
    (re.compile(r"\bhow are you\b|\bhow r u\b|\bwhat's up\b|\bwassup\b", re.I),
     "I'm doing great! What about you? 😊"),
    (re.compile(r"\bwhat('s| is) your name\b|\bwho are you\b", re.I),
     "I'm RuleBot 🤖 — a simple rule-based chatbot built in Python."),
    (re.compile(r"\bhow old are you\b|\bwhat('s| is) your age\b", re.I),
     "I was born the moment this script ran, so I'm pretty young! 😄"),
    (re.compile(r"\bwho (made|created|built) you\b", re.I),
     "I was built by a Python developer as a rule-based chatbot project."),
    (re.compile(r"\bhelp\b|\bwhat can you do\b", re.I),
     "I can chat about greetings, answer basic questions, and tell jokes! Try saying hi 😊"),
    (re.compile(r"\bwhat time is it\b|\bwhat('s| is) the time\b", re.I),
     "I don't have a clock ⏰, but your device can tell you!"),
    (re.compile(r"\bwhat('s| is) (today's |the )?date\b|\bwhat day is (it|today)\b", re.I),
     "Check your calendar 📅 — I'm not connected to live data!"),
    (re.compile(r"\bweather\b|\btemperature\b", re.I),
     "I can't check live weather 🌤️, try weather.com!"),
    (re.compile(r"\btell me a joke\b|\bsay something funny\b|\bjoke\b", re.I),
     "Why do programmers prefer dark mode? Because light attracts bugs! 🐛😂"),
    (re.compile(r"\bthank(s| you)\b|\bthx\b|\bty\b", re.I),
     "You're welcome! 😊 Anything else?"),
    (re.compile(r"\b(bye|goodbye|see you|cya)\b", re.I),
     "Goodbye! Have a great day! 👋"),
]

FALLBACK = "Hmm, I'm not sure about that 🤔. Try asking something else or type 'help'."


def get_response(user_input):
    for pattern, response in RULES:
        if pattern.search(user_input):
            return response
    return FALLBACK


# ── GUI ──────────────────────────────────

class ChatApp:
    def __init__(self, root):
        root.title("RuleBot - Chat")
        root.geometry("480x620")
        root.resizable(False, False)
        root.configure(bg="#1e1e2e")

        # ── Header ──
        header = tk.Frame(root, bg="#7c3aed", pady=12)
        header.pack(fill="x")
        tk.Label(header, text="🤖  RuleBot", font=("Segoe UI", 16, "bold"),
                 bg="#7c3aed", fg="white").pack()
        tk.Label(header, text="Rule-Based Chatbot", font=("Segoe UI", 9),
                 bg="#7c3aed", fg="#ddd6fe").pack()

        # ── Chat area ──
        self.chat_area = scrolledtext.ScrolledText(
            root, wrap=tk.WORD, state="disabled",
            font=("Segoe UI", 11), bg="#13131f", fg="#e2e8f0",
            bd=0, padx=12, pady=12, cursor="arrow",
            insertbackground="white"
        )
        self.chat_area.pack(fill="both", expand=True, padx=10, pady=(10, 0))

        # Tag colors for bot vs user bubbles
        self.chat_area.tag_config("user_name", foreground="#a78bfa", font=("Segoe UI", 9, "bold"))
        self.chat_area.tag_config("user_msg",  foreground="#e2e8f0", font=("Segoe UI", 11))
        self.chat_area.tag_config("bot_name",  foreground="#34d399", font=("Segoe UI", 9, "bold"))
        self.chat_area.tag_config("bot_msg",   foreground="#e2e8f0", font=("Segoe UI", 11))
        self.chat_area.tag_config("gap",       font=("Segoe UI", 4))

        # ── Input row ──
        input_frame = tk.Frame(root, bg="#1e1e2e", pady=10)
        input_frame.pack(fill="x", padx=10)

        self.entry = tk.Entry(
            input_frame, font=("Segoe UI", 12), bg="#2d2d44", fg="white",
            insertbackground="white", relief="flat", bd=8
        )
        self.entry.pack(side="left", fill="x", expand=True, ipady=6)
        self.entry.bind("<Return>", self.send)
        self.entry.focus()

        send_btn = tk.Button(
            input_frame, text="Send", font=("Segoe UI", 11, "bold"),
            bg="#7c3aed", fg="white", relief="flat", padx=16, pady=6,
            activebackground="#6d28d9", activeforeground="white",
            cursor="hand2", command=self.send
        )
        send_btn.pack(side="left", padx=(8, 0))

        # Welcome message
        self._append_bot("Hello! I'm RuleBot 🤖 Type something to get started. Type 'help' to see what I can do!")

    def _append_bot(self, msg):
        self.chat_area.config(state="normal")
        self.chat_area.insert("end", "RuleBot\n", "bot_name")
        self.chat_area.insert("end", f"{msg}\n", "bot_msg")
        self.chat_area.insert("end", "\n", "gap")
        self.chat_area.config(state="disabled")
        self.chat_area.see("end")

    def _append_user(self, msg):
        self.chat_area.config(state="normal")
        self.chat_area.insert("end", "You\n", "user_name")
        self.chat_area.insert("end", f"{msg}\n", "user_msg")
        self.chat_area.insert("end", "\n", "gap")
        self.chat_area.config(state="disabled")
        self.chat_area.see("end")

    def send(self, event=None):
        user_input = self.entry.get().strip()
        if not user_input:
            return
        self.entry.delete(0, "end")
        self._append_user(user_input)
        response = get_response(user_input)
        self._append_bot(response)


if __name__ == "__main__":
    root = tk.Tk()
    ChatApp(root)
    root.mainloop()
