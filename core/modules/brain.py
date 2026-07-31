from datetime import datetime

class Brain:

    def process(self, command, owner):
        command = command.lower().strip()

        if command in ["hello", "hi"]:
            return f"Hello {owner}."

        if "time" in command:
            return datetime.now().strftime("%I:%M %p")

        if "date" in command:
            return datetime.now().strftime("%d %B %Y")

        if "name" in command:
            return "My name is AETHER."

        return None
