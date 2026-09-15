import re
import tkinter as tk
from datetime import datetime

# ─────────────────────────────────────────
#  Rule-Based Chatbot - GUI Version
#  Bubble-style chat, typing effect, timestamps
# ─────────────────────────────────────────

RULES = [
    # Greetings
    (re.compile(r"\b(hi|hello|hey|howdy|hola|good morning|good evening|good afternoon)\b", re.I),
     "Hey there! How can I help you today?"),

    # How are you
    (re.compile(r"how are you|how r u|what'?s up|wassup|hows it going|how do you do", re.I),
     "I'm doing great! What about you?"),

    # Name
    (re.compile(r"what'?s your name|who are you|your name|aap kaun ho|tumhara naam", re.I),
     "I'm RuleBot - a simple rule-based chatbot built in Python."),

    # Age
    (re.compile(r"how old are you|what'?s your age|teri umar|tumhari umar", re.I),
     "I was born the moment this script ran, so I'm pretty young!"),

    # Creator
    (re.compile(r"who (made|created|built|developed) you|kisne banaya", re.I),
     "I was built by a Python developer as a rule-based chatbot project."),

    # Help
    (re.compile(r"\bhelp\b|what can you do|kya kar sakte ho|madad karo", re.I),
     "I can do the following:\n- Greet you\n- Tell jokes\n- Answer basic questions\n- Tell time and date\n- Chat about Python and AI\n\nJust type anything!"),

    # Time - dynamic
    (re.compile(r"what time|current time|time hai|time kya hai|kitne baje", re.I),
     None),  # handled dynamically in get_response

    # Date - dynamic
    (re.compile(r"what.?s the date|today.?s date|what day|aaj kya date|date kya hai", re.I),
     None),  # handled dynamically in get_response

    # Weather
    (re.compile(r"\bweather\b|\btemperature\b|mausam|garmi|sardi", re.I),
     "I can't check live weather, but try weather.com!"),

    # Jokes
    (re.compile(r"joke|funny|hasao|hasa do|make me laugh|something funny", re.I),
     "Why do programmers prefer dark mode?\nBecause light attracts bugs!"),

    # Compliment to bot
    (re.compile(r"you are (good|great|awesome|nice|cool|smart)|acha hai|badhiya", re.I),
     "Thank you so much! That means a lot to me!"),

    # Feeling sad
    (re.compile(r"i am (sad|upset|depressed|unhappy|bored)|mujhe bura lag raha|dukhi", re.I),
     "I'm sorry to hear that. I hope talking to me cheers you up a little!"),

    # Feeling happy
    (re.compile(r"i am (happy|great|good|excited|awesome)|mujhe acha lag raha|khush", re.I),
     "That's wonderful! Glad to hear you're doing well!"),

    # Thanks
    (re.compile(r"thank(s| you)|thx|\bty\b|shukriya|dhanyawad", re.I),
     "You're welcome! Anything else I can help with?"),

    # Bye
    (re.compile(r"\b(bye|goodbye|see you|cya|alvida|baad mein milte hain)\b", re.I),
     "Goodbye! Have a great day!"),

    # Python
    (re.compile(r"\bpython\b", re.I),
     "Python is awesome! I was built using Python and tkinter."),

    # AI
    (re.compile(r"what is (ai|artificial intelligence)|ai kya hai", re.I),
     "AI is the simulation of human intelligence by machines. I'm a simple rule-based version of it!"),

    # Are you a bot
    (re.compile(r"are you (a )?(bot|robot|human|real)|kya tum insaan ho", re.I),
     "I'm a bot! A rule-based chatbot to be precise."),

    # Favorite color
    (re.compile(r"fav(ou?rite)? colou?r|pasandida rang", re.I),
     "I love purple - as you can see from my theme!"),

    # Love
    (re.compile(r"i love you|i like you|mujhe tumse pyaar|tum acha lagte", re.I),
     "Aww, that's sweet! I like you too!"),

    # Meaning of life
    (re.compile(r"meaning of life|zindagi ka matlab|purpose of life", re.I),
     "42! (According to The Hitchhiker's Guide to the Galaxy)"),

    # Can you help
    (re.compile(r"can you help|kya aap help|mujhe help chahiye", re.I),
     "Of course! Tell me what you need help with."),
]

FALLBACK = "Hmm, I'm not sure about that. Try asking something else or type 'help'."


def get_response(user_input):
    for pattern, response in RULES:
        if pattern.search(user_input):
            # Dynamic time response
            if response is None:
                if re.search(r"time", user_input, re.I):
                    return f"Current time is: {datetime.now().strftime('%I:%M %p')}"
                else:
                    return f"Today is: {datetime.now().strftime('%A, %d %B %Y')}"
            return response
    return FALLBACK


# ── Colors ───────────────────────────────
BG        = "#0f0f1a"
HEADER_BG = "#6d28d9"
BOT_BG    = "#1e1b4b"
USER_BG   = "#6d28d9"
BOT_FG    = "#e0e7ff"
USER_FG   = "#ffffff"
INPUT_BG  = "#1e1e2e"
INPUT_FG  = "#e2e8f0"
TIME_FG   = "#6b7280"
SEND_BG   = "#7c3aed"
SEND_HOV  = "#5b21b6"


class ChatApp:
    def __init__(self, root):
        self.root = root
        root.title("RuleBot")
        root.geometry("500x680")
        root.resizable(False, False)
        root.configure(bg=BG)

        self._build_header()
        self._build_chat()
        self._build_input()

        # Show welcome after window loads
        root.after(300, lambda: self._type_bot_msg(
            "Hello! I'm RuleBot.\nType 'help' to see what I can do, or just say hi!"
        ))

    # ── Header ───────────────────────────
    def _build_header(self):
        hdr = tk.Frame(self.root, bg=HEADER_BG, pady=14)
        hdr.pack(fill="x")

        tk.Label(hdr, text="RuleBot", font=("Segoe UI", 17, "bold"),
                 bg=HEADER_BG, fg="white").pack()
        self.status_lbl = tk.Label(hdr, text="Online", font=("Segoe UI", 9),
                                   bg=HEADER_BG, fg="#c4b5fd")
        self.status_lbl.pack()

    # ── Scrollable canvas chat area ───────
    def _build_chat(self):
        container = tk.Frame(self.root, bg=BG)
        container.pack(fill="both", expand=True, padx=0, pady=(6, 0))

        self.canvas = tk.Canvas(container, bg=BG, bd=0, highlightthickness=0)
        scrollbar = tk.Scrollbar(container, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)

        # Inner frame holds all message bubbles
        self.msg_frame = tk.Frame(self.canvas, bg=BG)
        self.canvas_window = self.canvas.create_window(
            (0, 0), window=self.msg_frame, anchor="nw", width=484
        )

        self.msg_frame.bind("<Configure>", self._on_frame_configure)
        self.canvas.bind("<Configure>", self._on_canvas_configure)
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def _on_frame_configure(self, e):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def _on_canvas_configure(self, e):
        self.canvas.itemconfig(self.canvas_window, width=e.width)

    def _on_mousewheel(self, e):
        self.canvas.yview_scroll(int(-1 * (e.delta / 120)), "units")

    # ── Input bar ────────────────────────
    def _build_input(self):
        bar = tk.Frame(self.root, bg="#16162a", pady=10)
        bar.pack(fill="x", side="bottom")

        # Clear button
        clear_btn = tk.Button(
            bar, text="Clear", font=("Segoe UI", 9),
            bg="#2d2d44", fg="#9ca3af", relief="flat",
            padx=10, cursor="hand2", command=self._clear_chat,
            activebackground="#3d3d5c", activeforeground="white"
        )
        clear_btn.pack(side="left", padx=(10, 4), ipady=6)

        self.entry = tk.Entry(
            bar, font=("Segoe UI", 12), bg=INPUT_BG, fg=INPUT_FG,
            insertbackground="white", relief="flat", bd=0
        )
        self.entry.pack(side="left", fill="x", expand=True, ipady=8, padx=(0, 6))
        self.entry.bind("<Return>", self.send)
        self.entry.focus()

        self.send_btn = tk.Button(
            bar, text="Send", font=("Segoe UI", 11, "bold"),
            bg=SEND_BG, fg="white", relief="flat",
            padx=18, cursor="hand2", command=self.send,
            activebackground=SEND_HOV, activeforeground="white"
        )
        self.send_btn.pack(side="left", padx=(0, 10), ipady=6)

    # ── Bubble builder ───────────────────
    def _add_bubble(self, text, is_user):
        side   = "e" if is_user else "w"
        bg     = USER_BG if is_user else BOT_BG
        fg     = USER_FG if is_user else BOT_FG
        anchor = "e" if is_user else "w"
        padx   = (60, 10) if is_user else (10, 60)

        outer = tk.Frame(self.msg_frame, bg=BG)
        outer.pack(fill="x", pady=(4, 0))

        bubble = tk.Label(
            outer, text=text, font=("Segoe UI", 11),
            bg=bg, fg=fg, wraplength=320,
            justify="left", padx=14, pady=10,
            relief="flat", anchor="w"
        )
        bubble.pack(anchor=anchor, padx=padx)

        time_str = datetime.now().strftime("%I:%M %p")
        tk.Label(outer, text=time_str, font=("Segoe UI", 8),
                 bg=BG, fg=TIME_FG).pack(anchor=anchor, padx=padx)

        self._scroll_bottom()

    def _scroll_bottom(self):
        self.root.update_idletasks()
        self.canvas.yview_moveto(1.0)

    # ── Typing indicator ─────────────────
    def _show_typing(self):
        self.typing_frame = tk.Frame(self.msg_frame, bg=BG)
        self.typing_frame.pack(fill="x", pady=(4, 0))
        self.typing_lbl = tk.Label(
            self.typing_frame, text="RuleBot is typing...",
            font=("Segoe UI", 9, "italic"),
            bg=BG, fg="#6b7280"
        )
        self.typing_lbl.pack(anchor="w", padx=14)
        self._scroll_bottom()

    def _hide_typing(self):
        if hasattr(self, "typing_frame"):
            self.typing_frame.destroy()

    def _type_bot_msg(self, msg):
        self._show_typing()
        # Simulate typing delay based on message length
        delay = min(400 + len(msg) * 10, 1200)
        self.root.after(delay, lambda: (self._hide_typing(), self._add_bubble(msg, False)))

    # ── Clear chat ───────────────────────
    def _clear_chat(self):
        for widget in self.msg_frame.winfo_children():
            widget.destroy()
        self._type_bot_msg("Chat cleared! How can I help you?")

    # ── Send ─────────────────────────────
    def send(self, event=None):
        user_input = self.entry.get().strip()
        if not user_input:
            return
        self.entry.delete(0, "end")
        self._add_bubble(user_input, is_user=True)

        # Disable input while bot is "typing"
        self.entry.config(state="disabled")
        self.send_btn.config(state="disabled")

        response = get_response(user_input)
        self._type_bot_msg(response)

        # Re-enable after bot responds
        delay = min(400 + len(response) * 10, 1200) + 100
        self.root.after(delay, lambda: (
            self.entry.config(state="normal"),
            self.send_btn.config(state="normal"),
            self.entry.focus()
        ))


if __name__ == "__main__":
    root = tk.Tk()
    ChatApp(root)
    root.mainloop()
