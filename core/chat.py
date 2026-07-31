from gemini import ask_gemini

print("=" * 50)
print("🤖 AETHER AI v0.3")
print("Owner : Bhanu")
print("Type 'exit' to quit")
print("=" * 50)

while True:
    user = input("\nBhanu > ")

    if user.lower() == "exit":
        print("\nAETHER > Goodbye Bhanu 👋")
        break

    try:
        reply = ask_gemini(user)
        print("\nAETHER >", reply)

    except Exception as e:
        print("\nError:", e)
