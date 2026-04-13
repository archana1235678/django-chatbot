from django.shortcuts import render

def index(request):
    reply = ""

    if request.method == "POST":
        user_input = request.POST.get("message").lower()

        # 👋 Greetings
        if "hello" in user_input or "hi" in user_input:
            reply = "Hello 👋! How can I help you today?"

        # 🙂 How are you
        elif "how are you" in user_input:
            reply = "I'm just code, but I'm running perfectly fine 😊"

        # 🤖 Name
        elif "your name" in user_input:
            reply = "I'm your Django ChatBot 🤖"

        # 🌤️ Weather (fake response)
        elif "weather" in user_input:
            reply = "I can't check live weather yet 🌤️, but it's always good in code world 😄"

        # 💻 Programming
        elif "python" in user_input:
            reply = "Python is awesome 🐍! Great choice for AI, web & automation."

        elif "django" in user_input:
            reply = "Django is a powerful Python web framework 🚀"

        # 😂 Fun
        elif "joke" in user_input:
            reply = "Why do programmers hate nature? It has too many bugs 😂"

        # ❤️ Love
        elif "love" in user_input:
            reply = "Love coding ❤️ and building cool projects!"

        # 👋 Bye
        elif "bye" in user_input:
            reply = "Goodbye 👋! See you soon."

        # ❓ Default reply
        else:
            reply = "🤔 I don't understand that yet. Try asking about Python, Django, or say hello!"

    return render(request, "chat/index.html", {"reply": reply})