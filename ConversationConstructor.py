import random
import string


def constructConversations():
    helpQuestions = ["I need help",
                     "help me",
                     "I require assistance",
                     "I have a question",
                     "help",
                     "I'm stuck",
                     "I can't login",
                     "I lost my account",
                     "I'm having trouble with my account",
                     "I am locked out",
                     "I have a problem",
                     "Can you help",
                     "Can you help me",
                     "Assist me",
                     "Help me log in",
                     "Help me with my account",
                     "Can you fix my account",
                     "Fix my account",
                     "I need technical support",
                     "I forgot my password",
                     "I do not have credentials",
                     "My credentials are not working",
                     "Account help",
                     "Account",
                     "My password is not working",
                     "My email is wrong",
                     "I am not able to log in",
                     "I can't access my account"]
    conversations = []
    for question in helpQuestions:
        conversation = []
        conversation.append(question)
        conversation.append("Do not worry, I can help you with that. What is the email associated with your account?")
        emailProviders = ["@yahoo.com", "@gmail.com", "@icloud.com", "@outlook.com", "@hotmail.com",
                          "@oakland.edu", "@aol.com", "@protonmail.com"]
        emailAddress = ""
        for i in range(random.randint(5, 15)):
            emailAddress = emailAddress + str((random.choice(string.ascii_letters)))
        emailAddress = emailAddress + str((random.choice(emailProviders)))
        conversation.append(emailAddress)
        conversation.append("We couldn't find an account with that information. Could you provide your first and last name?")
        conversations.append(conversation)
    return conversations

emailProviders = ["@yahoo.com", "@gmail.com", "@icloud.com", "@outlook.com", "@hotmail.com",
                          "@oakland.edu", "@aol.com", "@protonmail.com"]

print(constructConversations())
