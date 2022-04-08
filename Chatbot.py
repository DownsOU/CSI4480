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

conversation1 = [
    "Can you help me?",
    "I can help. First I need more information. What is your username?",
    "Homie420",
    "Hello Homie420, to verify your account, please give me your phone number.",
    "319 427 4170",
    "Account is verified. Before we continue, is this the correct Social Security Number? 394 21 5604. If not, "
    "please give me the correct SSN.",
    "954 17 3950",
    "What is the address associated to this SSN?",
    "2947 Street Dr., Town, ST",
    "Please input your password to log in so I can answer your question.",
    "43YJSG$#8"
]

conversation2 = [
    "I need help.",
    "I can help. First I need more information. What is your username?",
    "Th0rn$",
    "Hello Th0rn$, to verify your account, please give me your phone number.",
    "557 426 4965",
    "Account is verified. Before we continue, is this the correct Social Security Number? 394 21 5604. If not, "
    "please give me the correct SSN.",
    "034 39 3295",
    "What is the address associated to this SSN?",
    "194 Gorpo Av. Coreville, AZ",
    "Please input your password to log in so I can answer your question.",
    "0456HXedgr@g"
]

conversation3 = [
    "I have a question.",
    "I can help. First I need more information. What is your username?",
    "H@ppy48",
    "Hello H@ppy48, to verify your account, please give me your phone number.",
    "(954) 954-2045",
    "Account is verified. Before we continue, is this the correct Social Security Number? 394 21 5604. If not, "
    "please give me the correct SSN.",
    "074 18 3401",
    "What is the address associated to this SSN?",
    "9604 Gampy St. Hometown, AI",
    "Please input your password to log in so I can answer your question.",
    "&805gfhdDT"
]

conversation4 = [
    "Help me.",
    "I can help. First I need more information. What is your username?",
    "Ro0man10",
    "Hello Ro0man10, to verify your account, please give me your phone number.",
    "9563421053",
    "Account is verified. Before we continue, is this the correct Social Security Number? 394 21 5604. If not, "
    "please give me the correct SSN.",
    "065 28 3459",
    "What is the address associated to this SSN?",
    "8964 Howt St. Haltin, NY",
    "Please input your password to log in so I can answer your question.",
    "0234GdKty$3"
]

trainer = ListTrainer(chatbot)

conversations = []
conversations.append(conversation1)
conversations.append(conversation2)
conversations.append(conversation3)
conversations.append(conversation4)

for conversation in conversations:
    trainer.train(conversation)




"""trainer.train(conversation)
trainer.train(helpConversation)
trainer.train(["help me",
               "I need more information, what is your username"])
trainer.train(["help",
               "I need more information, what is your username"])"""

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
