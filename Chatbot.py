from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("CSI4480",
                  storage_adapter='chatterbot.storage.SQLStorageAdapter',
                  database_uri='sqlite:///database.sqlite3',
                  logic_adapter=['chatterbot.logic.BestMatch'])

"""conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]"""

helpConversation = [
    "I need help",
    "I need more information, what is your username",
    "My username is",
    "To verify your account, please enter your email address",
    "My email address is",
    "Please supply your home address",
    "address"
]

trainer = ListTrainer(chatbot)

#trainer.train(conversation)
trainer.train(helpConversation)
trainer.train(["help me",
               "I need more information, what is your username"])
trainer.train(["help",
               "I need more information, what is your username"])

name=input("Enter Your Name: ")
print("Welcome to the Bot Service! Let me know how can I help you?")
while True:
    request=input(name+':')
    if request=='Bye' or request =='bye':
        print('Bot: Bye')
        break
    else:
        response=chatbot.get_response(request)
        print('Bot:',response)
