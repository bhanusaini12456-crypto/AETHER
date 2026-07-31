from datetime import datetime

class Aether:
    def __init__(self, owner="Bhanu"):
        self.owner = owner
        self.version = "0.1.0"

    def greet(self):
        hour = datetime.now().hour

        if hour < 12:
            greeting = "Good Morning"
        elif hour < 18:
            greeting = "Good Afternoon"
        else:
            greeting = "Good Evening"

        print("=" * 40)
        print("        AETHER AI")
        print("=" * 40)
        print(f"{greeting}, {self.owner}")
        print(f"Version : {self.version}")
        print("Status  : Online")
        print("=" * 40)

    def listen(self):
        command = input("You : ")
        return command

    def think(self, command):
        command = command.lower()

        if "hello" in command:
            return f"Hello {self.owner}."

        elif "time" in command:
            return datetime.now().strftime("%I:%M %p")

        elif "exit" in command:
            return "shutdown"

        else:
            return "I understand your request, but this feature is not implemented yet."

def main():
    aether = Aether()
    aether.greet()

    while True:
        command = aether.listen()
        response = aether.think(command)

        if response == "shutdown":
            print("AETHER : Goodbye Bhanu.")
            break

        print("AETHER :", response)

if __name__ == "__main__":
    main()
