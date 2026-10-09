"""
Python Voice Assistant — simple terminal version.

This script supports typed commands so it can run in a regular Python terminal.
The notebook version provides browser microphone recording in Google Colab.
"""
import datetime
import threading
import time
import webbrowser
from urllib.parse import quote_plus

CUSTOM_COMMANDS = {
    "what is python": "Python is a readable, general-purpose programming language.",
    "who created python": "Python was created by Guido van Rossum.",
}

def speak(text):
    print("Assistant:", text)

def set_reminder(seconds, message):
    def notify():
        time.sleep(seconds)
        speak("Reminder: " + message)
    threading.Thread(target=notify, daemon=True).start()
    speak(f"Reminder set for {seconds} seconds.")

def handle_command(command):
    command = command.lower().strip()

    if any(word in command for word in ("stop assistant", "exit", "quit")):
        speak("Goodbye!")
        return False

    if any(word in command for word in ("hello", "hi", "hey")):
        speak("Hello! How can I help you?")
    elif "time" in command:
        speak("The current time is " + datetime.datetime.now().strftime("%I:%M %p"))
    elif "date" in command or "today" in command:
        speak("Today's date is " + datetime.datetime.now().strftime("%d %B %Y"))
    elif "search" in command or command.startswith("google "):
        query = command.replace("search for", "").replace("search", "").replace("google", "").strip()
        if query:
            webbrowser.open("https://www.google.com/search?q=" + quote_plus(query))
            speak("Opening your web search.")
        else:
            speak("Please tell me what to search for.")
    elif "remind me in" in command:
        try:
            parts = command.split("remind me in", 1)[1].strip().split()
            seconds = int(parts[0])
            message = " ".join(parts[2:]) if len(parts) > 2 and parts[1].startswith("second") else "your reminder"
            if seconds < 1:
                raise ValueError
            set_reminder(seconds, message)
        except (ValueError, IndexError):
            speak("Please type a reminder like: remind me in 10 seconds to stretch.")
    elif command in CUSTOM_COMMANDS:
        speak(CUSTOM_COMMANDS[command])
    else:
        speak("I don't know that command yet. Try hello, time, date, search, or a reminder.")
    return True

def main():
    speak("Hello! Welcome to the Python Voice Assistant.")
    while True:
        try:
            command = input("You (type a command): ")
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if not handle_command(command):
            break

if __name__ == "__main__":
    main()
