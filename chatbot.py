from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot=ChatBot("custmor bot")

trainer=ListTrainer(bot)

trainer.train([
    "Hi",
    "Hello! How can I help you?",

    "What are your working hours",
    "We are open from 9am to 6pm.",

    "How can I place an order",
    "You can order from our website.",

    "How long does delivery take",
    "Delivery takes 3 to 5 days.",

    "Thanks",
    "Welcome!",

    "Bye",
    "Goodbye!"
])

print("Bot is ready! Type bye to exit.")

while True:

    user = input("You: ")

    if user.lower() == "bye":
        print("Bot: Goodbye!")
        break

    response = bot.get_response(user)
    print("Bot:", response)